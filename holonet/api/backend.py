# -*- coding: utf8 -*-

from rest_framework.authentication import BaseAuthentication, get_authorization_header

from .models import Token


class TokenAuthenticationBackend(BaseAuthentication):
    def authenticate(self, request):
        token = get_authorization_header(request)

        try:
            token_object = Token.get_token(token)
            return token_object.application, request
        except Token.DoesNotExist:
            pass

        return None
