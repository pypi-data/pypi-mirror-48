__all__ = (
    "AdminTokenManagement", "TokenDeletionRequest", "TokenRenewal"
)

import logging

from django.conf import settings
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.views.generic.edit import DeleteView
from django.http import (
    Http404, HttpResponseServerError, JsonResponse, HttpResponseRedirect,
    HttpResponse
)

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from django.test import Client


import requests

from ._core import UCTestMixin
from ..models import AuthToken
from ..helpers import get_settings_func, get_requests_params
from ..constants import TokenCreationError


logger = logging.getLogger(__name__)


class AdminTokenManagement(UCTestMixin, View):
    scope = None
    created_token = None

    def dispatch_extra(self, request, *args, **kwargs):
        self.remove_old_tokens()

    def test_func(self):
        if self.scope == "delete":
            return self.has_special_access(
                user_by_login=True
            )
        else:
            return self.has_special_access(
                user_by_login=True, user_by_token=True
            )

    def post(self, request, *args, **kwargs):
        if self.request.POST.get("add_token"):
            self.created_token = self.create_token(
                extra={
                    "strength": self.usercomponent.strength
                }
            )
        delids = self.request.POST.getlist("delete_tokens")
        if delids:
            delquery = AuthToken.objects.filter(
                usercomponent=self.usercomponent,
                id__in=delids
            )
            if self.scope == "share":
                delquery = delquery.filter(
                    Q(session_key=request.session.session_key) |
                    Q(token=request.auth_token)
                )
            shall_redirect = delquery.filter(token=request.auth_token).exists()
            delquery.delete()
            del delquery
            if shall_redirect:
                return HttpResponseRedirect(
                    redirect_to=request.get_full_path()
                )

        return self.get(request, *args, **kwargs)

    def _token_dict(self, token):
        if token.session_key == self.request.session.session_key:
            assert(not token.referrer)
            return {
                "expires": None if token.persist >= 0 else (
                    token.created +
                    self.usercomponent.token_duration
                ).strftime("%a, %d %b %Y %H:%M:%S %z"),
                "referrer": token.referrer if token.referrer else "",
                "name": token.token,
                "id": token.id,
                "same_session": True,
                "created": self.created_token == token,
                "admin_key": self.request.auth_token == token
            }
        elif self.request.auth_token == token:
            assert(not token.referrer)
            return {
                "expires": None if token.persist >= 0 else (
                    token.created +
                    self.usercomponent.token_duration
                ).strftime("%a, %d %b %Y %H:%M:%S %z"),
                "referrer": token.referrer if token.referrer else "",
                "name": token.token,
                "id": token.id,
                "same_session": True,
                "created": self.created_token == token,
                "admin_key": True
            }
        else:
            return {
                "expires": None if token.persist >= 0 else (
                    token.created +
                    self.usercomponent.token_duration
                ).strftime("%a, %d %b %Y %H:%M:%S %z"),
                "referrer": token.referrer if token.referrer else "",
                "name": str(token),
                "id": token.id,
                "same_session": False,
                "created": self.created_token == token,
                "admin_key": False
            }

    def get(self, request, *args, **kwargs):
        if self.scope == "delete":
            response = {
                "tokens": list(map(
                    self._token_dict,
                    AuthToken.objects.filter(
                        usercomponent=self.usercomponent
                    )  # TODO: add order function which sorts admin_key higher
                )),
            }
        else:
            response = {
                "tokens": list(map(
                    self._token_dict,
                    AuthToken.objects.filter(
                        Q(session_key=request.session.session_key) |
                        Q(token=request.auth_token),
                        usercomponent=self.usercomponent,
                    )
                )),
            }
        return JsonResponse(response)


class TokenDeletionRequest(UCTestMixin, DeleteView):
    model = AuthToken
    template_name = "spider_base/protections/authtoken_confirm_delete.html"

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        try:
            return super().dispatch(request, *args, **kwargs)
        except Http404:
            return get_settings_func(
                "SPIDER_RATELIMIT_FUNC",
                "spkcspider.apps.spider.functions.rate_limit_default"
            )(self, request)

    def test_func(self):
        # tokens which are not persistent can be easily deleted
        if self.object.persist < 0:
            return True
        if self.has_special_access(
            user_by_token=True, user_by_login=True,
            superuser=True, staff="spider_base.delete_authtoken"
        ):
            return True
        return False

    def get_usercomponent(self):
        return self.object.usercomponent

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()

        return get_object_or_404(
            queryset,
            token=self.request.GET.get("delete", ""),
        )

    def get(self, request, *args, **kwargs):
        # tokens which are not persistent can be easily deleted
        if self.object.persist < 0:
            return self.delete(request, *args, **kwargs)
        return super().get(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        url = None
        if self.object.referrer:
            url = self.object.referrer.url
        self.object.delete()
        if not url:
            return HttpResponse(status=200)
        return HttpResponseRedirect(
            redirect_to=url
        )

    def post(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def options(self, request, *args, **kwargs):
        ret = super().options()
        ret["Access-Control-Allow-Origin"] = "*"
        ret["Access-Control-Allow-Methods"] = "GET, POST, DELETE, OPTIONS"
        return ret


class TokenRenewal(UCTestMixin, View):
    model = AuthToken
    oldtoken = None

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        try:
            return super().dispatch(request, *args, **kwargs)
        except Http404:
            return get_settings_func(
                "SPIDER_RATELIMIT_FUNC",
                "spkcspider.apps.spider.functions.rate_limit_default"
            )(self, request)

    def get_usercomponent(self):
        token = self.request.POST.get("token", None)
        if not token:
            raise Http404()
        self.request.auth_token = get_object_or_404(
            AuthToken,
            token=token,
            persist__gte=0,
            referrer__isnull=False
        )
        assert (
            "persist" in self.request.auth_token.extra.get(
                "intentions", []
            )
        )
        return self.request.auth_token.usercomponent

    def test_func(self):
        return True

    def options(self, request, *args, **kwargs):
        ret = super().options()
        ret["Access-Control-Allow-Origin"] = \
            self.request.auth_token.referrer.host
        ret["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        return ret

    def update_with_post(self):
        # application/x-www-form-urlencoded is best here,
        # for beeing compatible to most webservers
        # client side rdf is no problem
        # NOTE: csrf must be disabled or use csrf token from GET,
        #       here is no way to know the token value
        d = {
            "oldtoken": self.oldtoken,
            "token": self.request.auth_token.token,
            "hash_algorithm": settings.SPIDER_HASH_ALGORITHM.name,
            "renew": "true"
        }
        if "payload" in self.request.POST:
            d["payload"] = self.request.POST["payload"]

        params, can_inline = get_requests_params(
            self.request.auth_token.referrer.url
        )
        if can_inline:
            response = Client().post(
                self.request.auth_token.referrer.url,
                data=d,
                Connection="close",
                Referer="%s://%s" % (
                    self.request.scheme,
                    self.request.path
                )
            )
            if response.status_code >= 400:
                return False
        else:
            try:
                with requests.post(
                    self.request.auth_token.referrer.url,
                    data=d,
                    headers={
                        "Referer": "%s://%s" % (
                            self.request.scheme,
                            self.request.path
                        ),
                        "Connection": "close"
                    },
                    **params
                ) as resp:
                    resp.raise_for_status()
            except requests.exceptions.SSLError as exc:
                logger.info(
                    "referrer: \"%s\" has a broken ssl configuration",
                    self.request.auth_token.referrer, exc_info=exc
                )
                return False
            except Exception as exc:
                logger.info(
                    "post failed: \"%s\" failed",
                    self.request.auth_token.referrer, exc_info=exc
                )
                return False
        return True

    def post(self, request, *args, **kwargs):
        self.oldtoken = self.request.auth_token.token
        self.request.auth_token.initialize_token()
        success = True
        if "sl" in self.request.auth_token.extra.get("intentions", []):
            # only the original referer can access this
            success = (
                self.request.headers.get("Referer", "").startswith(
                    self.request.auth_token.referrer.url
                )
            )
        else:
            # if not serverless:
            # you cannot steal a token because it is bound to a domain
            # damage can be only done in persisted data
            success = self.update_with_post()
        if success:
            try:
                self.request.auth_token.save()
            except TokenCreationError:
                success = False
        if not success:
            logger.exception("Token creation failed")
            return HttpResponseServerError(
                "Token update failed, try again"
            )
        if "sl" in self.request.auth_token.extra.get("intentions", []):
            ret = HttpResponse(
                self.request.auth_token.token.encode(
                    "ascii"
                ),
                content_type="text/plain",
                status=200
            )
        else:
            ret = HttpResponse(status=200)
        # no sl: simplifies update logic for thirdparty web servers
        # sl: safety (but anyway checked by referer check)
        ret["Access-Control-Allow-Origin"] = \
            self.request.auth_token.referrer.host
        return ret
