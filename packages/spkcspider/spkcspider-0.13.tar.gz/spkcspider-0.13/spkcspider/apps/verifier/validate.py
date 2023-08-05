__all__ = {
    "validate", "valid_wait_states", "verify_download_size",
    "async_validate", "verify_tag", "async_verify_tag"
}

import logging
import binascii
import tempfile
import os

from django.utils.translation import gettext as _
from django.core.files import File
from django.conf import settings
from django.core import exceptions
from django.test import Client

from rdflib import Graph, URIRef, Literal
from rdflib.resource import Resource
from rdflib.namespace import XSD
import requests

from spkcspider import celery_app

from spkcspider.apps.spider.constants import spkcgraph
from spkcspider.apps.spider.helpers import merge_get_url, get_settings_func

from .constants import BUFFER_SIZE
from .functions import get_hashob, get_requests_params, get_anchor_domain
from .models import VerifySourceObject, DataVerificationTag

hashable_predicates = set([spkcgraph["name"], spkcgraph["value"]])

valid_wait_states = {
    "RETRIEVING", "HASHING", "STARTED"
}


def hash_entry(lit):
    h = get_hashob()
    if lit.datatype == XSD.base64Binary:
        h.update(lit.datatype.encode("utf8"))
        h.update(lit.toPython())
    else:
        if lit.datatype:
            h.update(lit.datatype.encode("utf8"))
        else:
            h.update(XSD.string.encode("utf8"))
        h.update(lit.encode("utf8"))
    return h.finalize()


def yield_hashes(graph, hashable_nodes):
    for t in hashable_nodes:
        for t2 in t[spkcgraph["value"]]:
            if t2.datatype == spkcgraph["hashableURI"]:
                continue
            yield hash_entry(t2)


def yield_hashable_urls(graph, hashable_nodes):
    for t in hashable_nodes:
        for t2 in t[spkcgraph["value"]]:
            if t2.datatype != spkcgraph["hashableURI"]:
                continue
            yield t2


def verify_download_size(length, current_size=0):
    if not length or not length.isdigit():
        return False
    length = int(length)
    if settings.VERIFIER_MAX_SIZE_ACCEPTED < length:
        return False
    return True


def validate(ob, hostpart, task=None):
    dvfile = None
    source = None
    session = requests.session()
    if isinstance(ob, tuple):
        dvfile = open(ob[0], "r+b")
        current_size = ob[1]
    else:
        current_size = 0
        dvfile = tempfile.NamedTemporaryFile(delete=False)

        source = VerifySourceObject.objects.get(
            id=ob
        )
        url = source.get_url()
        params, can_inline = get_requests_params(url)
        if can_inline:
            resp = Client().get(url)
            if resp.status_code != 200:
                session.close()
                dvfile.close()
                os.unlink(dvfile.name)
                raise exceptions.ValidationError(
                    _("Retrieval failed: %(reason)s"),
                    params={"reason": resp.reason},
                    code="error_code:{}".format(resp.status_code)
                )

            c_length = resp.get("content-length", None)
            if not verify_download_size(c_length, current_size):
                resp.close()
                session.close()
                dvfile.close()
                os.unlink(dvfile.name)
                raise exceptions.ValidationError(
                    _("Content too big: %(size)s"),
                    params={"size": c_length},
                    code="invalid_size"
                )
            c_length = int(c_length)
            current_size += c_length
            # clear file
            dvfile.truncate(c_length)
            dvfile.seek(0, 0)

            for chunk in resp:
                dvfile.write(chunk)
            dvfile.seek(0, 0)
            resp.close()
        else:
            try:
                with session.get(
                    url, stream=True, **params
                ) as resp:
                    if resp.status_code != 200:
                        session.close()
                        dvfile.close()
                        os.unlink(dvfile.name)
                        raise exceptions.ValidationError(
                            _("Retrieval failed: %(reason)s"),
                            params={"reason": resp.reason},
                            code="error_code:{}".format(resp.status_code)
                        )

                    c_length = resp.headers.get("content-length", None)
                    if not verify_download_size(c_length, current_size):
                        session.close()
                        dvfile.close()
                        os.unlink(dvfile.name)
                        raise exceptions.ValidationError(
                            _("Content too big: %(size)s"),
                            params={"size": c_length},
                            code="invalid_size"
                        )
                    c_length = int(c_length)
                    current_size += c_length
                    # preallocate file
                    dvfile.truncate(c_length)
                    dvfile.seek(0, 0)

                    for chunk in resp.iter_content(BUFFER_SIZE):
                        dvfile.write(chunk)
                    dvfile.seek(0, 0)
            except requests.exceptions.Timeout:
                session.close()
                raise exceptions.ValidationError(
                    _('url timed out: %(url)s'),
                    params={"url": url},
                    code="timeout_url"
                )
            except requests.exceptions.ConnectionError:
                session.close()
                raise exceptions.ValidationError(
                    _('invalid url: %(url)s'),
                    params={"url": url},
                    code="invalid_url"
                )
    g = Graph()
    g.namespace_manager.bind("spkc", spkcgraph, replace=True)
    try:
        g.parse(
            dvfile.name,
            format="turtle"
        )
    except Exception:
        if settings.DEBUG:
            dvfile.seek(0, 0)
            logging.exception(dvfile.read())
        logging.error("Parsing file failed")
        session.close()
        dvfile.close()
        os.unlink(dvfile.name)
        raise exceptions.ValidationError(
            _('Invalid graph fromat'),
            code="invalid_format"
        )

    tmp = list(g.triples((None, spkcgraph["scope"], None)))
    if len(tmp) != 1:
        dvfile.close()
        os.unlink(dvfile.name)
        raise exceptions.ValidationError(
            _('Invalid graph'),
            code="invalid_graph"
        )
    start = tmp[0][0]
    scope = tmp[0][2].toPython()
    tmp = list(g.triples((start, spkcgraph["pages.num_pages"], None)))
    if len(tmp) != 1:
        session.close()
        dvfile.close()
        os.unlink(dvfile.name)
        raise exceptions.ValidationError(
            _('Invalid graph'),
            code="invalid_graph"
        )
    pages = tmp[0][2].toPython()
    tmp = list(g.triples((
        start,
        spkcgraph["pages.current_page"],
        Literal(1, datatype=XSD.positiveInteger)
    )))
    if len(tmp) != 1:
        session.close()
        dvfile.close()
        os.unlink(dvfile.name)
        raise exceptions.ValidationError(
            _('Must be page 1'),
            code="invalid_page"
        )
    if task:
        task.update_state(
            state='RETRIEVING',
            meta={
                'page': 1,
                'num_pages': pages
            }
        )
    tmp = list(g.objects(start, spkcgraph["action:view"]))
    if len(tmp) != 1:
        session.close()
        dvfile.close()
        os.unlink(dvfile.name)
        raise exceptions.ValidationError(
            _('Invalid graph'),
            code="invalid_graph"
        )
    view_url = tmp[0].toPython()
    if isinstance(ob, tuple):
        split = view_url.split("?", 1)
        source = VerifySourceObject.objects.update_or_create(
            url=split[0], defaults={"get_params": split[1]}
        )
    mtype = set()
    if scope == "list":
        mtype.add("UserComponent")
    else:
        mtype.update(map(
            lambda x: x.toPython(), g.objects(start, spkcgraph["type"])
        ))

    data_type = get_settings_func(
        "VERIFIER_CLEAN_GRAPH",
        "spkcspider.apps.verifier.functions.clean_graph"
    )(mtype, g, start, source, hostpart)
    if not data_type:
        session.close()
        dvfile.close()
        os.unlink(dvfile.name)
        raise exceptions.ValidationError(
            _('Invalid graph type: %(type)s'),
            params={"type": data_type},
            code="invalid_type"
        )

    # retrieve further pages
    for page in range(2, pages+1):
        url = merge_get_url(
            source.get_url(), raw="embed", page=str(page)
        )
        # validation not neccessary here (base url is verified)
        params, can_inline = get_requests_params(url)
        if can_inline:
            resp = Client().get(url)
            if resp.status_code != 200:
                session.close()
                dvfile.close()
                os.unlink(dvfile.name)
                raise exceptions.ValidationError(
                    _("Retrieval failed: %(reason)s"),
                    params={"reason": resp.reason},
                    code="error_code:{}".format(resp.status_code)
                )

            c_length = resp.get("content-length", None)
            if not verify_download_size(c_length, current_size):
                resp.close()
                session.close()
                dvfile.close()
                os.unlink(dvfile.name)
                raise exceptions.ValidationError(
                    _("Content too big: %(size)s"),
                    params={"size": c_length},
                    code="invalid_size"
                )
            c_length = int(c_length)
            current_size += c_length
            # clear file
            dvfile.truncate(c_length)
            dvfile.seek(0, 0)

            for chunk in resp:
                dvfile.write(chunk)
            resp.close()
            dvfile.seek(0, 0)
        else:
            try:
                with session.get(
                    url, stream=True, **params
                ) as resp:
                    if resp.status_code != 200:
                        session.close()
                        dvfile.close()
                        os.unlink(dvfile.name)
                        raise exceptions.ValidationError(
                            _("Retrieval failed: %(reason)s"),
                            params={"reason": resp.reason},
                            code="error_code:{}".format(resp.status_code)
                        )

                    c_length = resp.headers.get("content-length", None)
                    if not verify_download_size(c_length, current_size):
                        session.close()
                        dvfile.close()
                        os.unlink(dvfile.name)
                        raise exceptions.ValidationError(
                            _("Content too big: %(size)s"),
                            params={"size": c_length},
                            code="invalid_size"
                        )
                    c_length = int(c_length)
                    current_size += c_length
                    # clear file
                    dvfile.truncate(c_length)
                    dvfile.seek(0, 0)

                    for chunk in resp.iter_content(BUFFER_SIZE):
                        dvfile.write(chunk)
                    dvfile.seek(0, 0)
            except requests.exceptions.Timeout:
                session.close()
                dvfile.close()
                os.unlink(dvfile.name)
                raise exceptions.ValidationError(
                    _('url timed out: %(url)s'),
                    params={"url": url},
                    code="timeout_url"
                )
            except requests.exceptions.ConnectionError:
                session.close()
                dvfile.close()
                os.unlink(dvfile.name)
                raise exceptions.ValidationError(
                    _('Invalid url: %(url)s'),
                    params={"url": url},
                    code="innvalid_url"
                )

        try:
            g.parse(
                dvfile.name,
                format="turtle"
            )
        except Exception as exc:
            if settings.DEBUG:
                dvfile.seek(0, 0)
                logging.error(dvfile.read())
            logging.exception(exc)
            session.close()
            dvfile.close()
            os.unlink(dvfile.name)
            # pages could have changed, but still incorrect
            raise exceptions.ValidationError(
                _("%(page)s is not a \"%(format)s\" file"),
                params={"format": "turtle", "page": page},
                code="invalid_file"
            )

        if task:
            task.update_state(
                state='RETRIEVING',
                meta={
                    'page': page,
                    'num_pages': pages
                }
            )
    g.remove((None, spkcgraph["csrftoken"], None))

    hashable_nodes = set(map(
        lambda x: Resource(g, x),
        g.subjects(
            predicate=spkcgraph["hashable"], object=Literal(True)
        )
    ))

    hashes = [
        *yield_hashes(g, hashable_nodes)
    ]
    if task:
        task.update_state(
            state='RETRIEVING',
            meta={
                'hashable_urls_checked': 0
            }
        )
    for count, lit in enumerate(yield_hashable_urls(
        g, hashable_nodes
    ), start=1):
        if (URIRef(lit.value), None, None) in g:
            continue
        url = merge_get_url(lit.value, raw="embed")
        if not get_settings_func(
            "SPIDER_URL_VALIDATOR",
            "spkcspider.apps.spider.functions.validate_url_default"
        )(url):
            session.close()
            dvfile.close()
            os.unlink(dvfile.name)
            raise exceptions.ValidationError(
                _('Insecure url: %(url)s'),
                params={"url": url},
                code="insecure_url"
            )

        params, can_inline = get_requests_params(url)
        if can_inline:
            resp = Client().get(url)
            if resp.status_code != 200:
                raise exceptions.ValidationError(
                    _("Retrieval failed: %(reason)s"),
                    params={"reason": resp.reason},
                    code="code_{}".format(resp.status_code)
                )
            h = get_hashob()
            h.update(XSD.base64Binary.encode("utf8"))
            for chunk in resp.iter_content(BUFFER_SIZE):
                h.update(chunk)
            resp.close()
            # do not use add as it could be corrupted by user
            # (user can provide arbitary data)
            g.set((
                URIRef(lit.value),
                spkcgraph["hash"],
                Literal(h.finalize().hex())
            ))
            if task:
                task.update_state(
                    state='RETRIEVING',
                    meta={
                        'hashable_urls_checked': count
                    }
                )
        else:
            try:
                with session.get(
                    url, stream=True, **params
                ) as resp:
                    if resp.status_code != 200:
                        raise exceptions.ValidationError(
                            _("Retrieval failed: %(reason)s"),
                            params={"reason": resp.reason},
                            code="code_{}".format(resp.status_code)
                        )
                    h = get_hashob()
                    h.update(XSD.base64Binary.encode("utf8"))
                    for chunk in resp.iter_content(BUFFER_SIZE):
                        h.update(chunk)
                    # do not use add as it could be corrupted by user
                    # (user can provide arbitary data)
                    g.set((
                        URIRef(lit.value),
                        spkcgraph["hash"],
                        Literal(h.finalize().hex())
                    ))
                    if task:
                        task.update_state(
                            state='RETRIEVING',
                            meta={
                                'hashable_urls_checked': count
                            }
                        )
            except requests.exceptions.Timeout:
                session.close()
                dvfile.close()
                os.unlink(dvfile.name)
                raise exceptions.ValidationError(
                    _('url timed out: %(url)s'),
                    params={"url": url},
                    code="timeout_url"
                )
            except requests.exceptions.ConnectionError:
                session.close()
                dvfile.close()
                os.unlink(dvfile.name)
                raise exceptions.ValidationError(
                    _('Invalid url: %(url)s'),
                    params={"url": url},
                    code="innvalid_url"
                )
    # not required anymore
    session.close()
    if task:
        task.update_state(
            state='HASHING',
        )

    # make sure triples are linked to start
    # (user can provide arbitary data)
    g.remove((start, spkcgraph["hashed"], None))
    for t in g.triples((None, spkcgraph["hash"], None)):
        g.add((
            start,
            spkcgraph["hashed"],
            t[0]
        ))
        hashes.append(binascii.unhexlify(t[2].value))

    for i in g.subjects(spkcgraph["type"], Literal("Content")):
        h = get_hashob()
        h.update(i.encode("utf8"))
        hashes.append(h.finalize())
    hashes.sort()

    h = get_hashob()
    for i in hashes:
        h.update(i)
    # do not use add as it could be corrupted by user
    # (user can provide arbitary data)
    digest = h.finalize().hex()
    g.set((
        start,
        spkcgraph["hash"],
        Literal(digest)
    ))

    dvfile.truncate(0)
    dvfile.seek(0, 0)
    # save in temporary file
    g.serialize(
        dvfile, format="turtle"
    )

    result, created = DataVerificationTag.objects.get_or_create(
        defaults={
            "dvfile": File(dvfile),
            "source": source,
            "data_type": data_type
        },
        hash=digest
    )
    dvfile.close()
    os.unlink(dvfile.name)
    update_fields = set()
    # and source, cannot remove source without replacement
    if not created and source and source != result.source:
        result.source = source
        update_fields.add("source")
    if data_type != result.data_type:
        result.data_type = data_type
        update_fields.add("data_type")
    result.save(update_fields=update_fields)
    verify_tag(result, task=task, ffrom="validate")
    if task:
        task.update_state(
            state='SUCCESS'
        )
    return result


@celery_app.task(bind=True, name='async validation')
def async_validate(self, ob, hostpart):
    ret = validate(ob, hostpart, self)
    return ret.get_absolute_url()


def verify_tag(tag, hostpart=None, ffrom="sync_call", task=None):
    """ for auto validation or hooks"""
    if not hostpart:
        hostpart = get_anchor_domain()
    if task:
        task.update_state(
            state='VERIFY'
        )

    if get_settings_func(
        "VERIFIER_TAG_VERIFIER",
        "spkcspider.apps.verifier.functions.verify_tag_default"
    )(tag, hostpart, ffrom):
        try:
            tag.callback(hostpart)
        except exceptions.ValidationError:
            logging.exception("Error while calling back")
    if task:
        task.update_state(
            state='SUCCESS'
        )


@celery_app.task(bind=True, name='async verification', ignore_results=True)
def async_verify_tag(self, tagid, hostpart=None, ffrom="async_call"):
    verify_tag(
        tag=DataVerificationTag.objects.get(id=tagid),
        hostpart=hostpart, task=self, ffrom=ffrom
    )
