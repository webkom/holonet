from django.contrib.auth.models import AbstractBaseUser, _user_has_module_perms
from oauth2_provider.ext.rest_framework import OAuth2Authentication


class HolonetAuthentication(OAuth2Authentication):
    """
    OAuth 2 authentication backend using `django-oauth-toolkit`
    Overrides the OAuth2Authentication class and adds a mock user if the token is valid but no
    user is attached. (ClientCredentials)
    """

    def authenticate(self, request):
        """
        Returns two-tuple of (user, token) if authentication succeeds,
        or None otherwise.
        """
        token_validation = super().authenticate(request)

        if token_validation is not None:
            user, token = token_validation
            if user is None:
                user = HolonetAPIUser()
            return user, token

        return None


class HolonetAPIUser(AbstractBaseUser):

    def get_full_name(self):
        return 'HolonetAPI'

    get_short_name = get_full_name
    get_username = get_full_name

    def has_perm(self, perm, obj=None):
        return False

    def has_perms(self, perm_list, obj=None):
        """
        Returns True if the user has each of the specified permissions. If
        object is passed, it checks if the user has all required perms for this
        object.
        """
        for perm in perm_list:
            if not self.has_perm(perm, obj):
                return False
        return True

    def has_module_perms(self, app_label):
        """
        Returns True if the user has any permissions in the given app label.
        Uses pretty much the same logic as has_perm, above.
        """
        return _user_has_module_perms(self, app_label)
