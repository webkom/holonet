# -*- coding: utf8 -*-

from rest_framework.authentication import BaseAuthentication

from .models import Token


class TokenAuthenticationBackend(BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get('HTTP_X_TOKEN')

        if token is None:
            token = request.META.get('HTTP_TOKEN')

        try:
            token_object = Token.get_token(token)
            return token_object.application, request
        except Token.DoesNotExist:
            pass

        return None
