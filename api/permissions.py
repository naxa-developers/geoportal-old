from rest_framework import permissions


class OwnerProfilePermission(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to View and Update it.
    """

    def has_object_permission(self, request, view, obj):

        if obj.user == request.user:
            return True
