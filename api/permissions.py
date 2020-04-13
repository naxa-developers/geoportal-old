from rest_framework import permissions


class SuperAdminPermission(permissions.BasePermission):
    """
        Super user Permission who can access all
    """

    def has_permission(self, request, view):

        if request.user.is_superuser:
            return True
