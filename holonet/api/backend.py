from rest_framework.authentication import BaseAuthentication, get_authorization_header
from rest_framework.permissions import BasePermission

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


class StaffRequired(BasePermission):

    def has_permission(self, request, view):
        valid_auth = request.user and request.user.is_authenticated and request.user.is_active

        return valid_auth and (request.user.is_staff or request.user.is_superuser)
