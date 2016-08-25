from rest_framework import permissions


class HolonetPermissions(permissions.BasePermission):
    """
    Allow admin and staff users, token authentication is granted.
    """

    def has_permission(self, request, view):
        user_authenticated = bool(request.user and request.user.is_authenticated())
        return (
            user_authenticated and (request.user.is_staff or request.user.is_superuser)
        ) or request.auth
