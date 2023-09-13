from rest_framework.permissions import BasePermission


class CustomerPermission(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_customer and request.user.is_active and request.user.is_verified)
