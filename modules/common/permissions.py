from django.contrib.auth.models import AnonymousUser

from rest_framework.permissions import BasePermission


class CustomerPermission(BasePermission):
    def has_permission(self, request, view):

        if isinstance(request.user, AnonymousUser):
            return False

        return bool(
            request.user.is_customer and
            request.user.is_active and
            request.user.is_verified and
            request.user.is_authenticated
        )
