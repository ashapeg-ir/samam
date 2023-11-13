from django.contrib.auth.models import AnonymousUser
from modules.domain.models import Supervisor
from rest_framework.permissions import BasePermission


class SupervisorPermission(BasePermission):
    def has_permission(self, request, view):

        if type(request.user) == AnonymousUser:
            return False

        return bool(
            request.user.is_supervisor and
            request.user.is_active and
            request.user.is_verified and
            request.user.is_authenticated
        )


class SuperVisorPermission(BasePermission):

    def has_permission(self, request, view):

        if type(request.user) == AnonymousUser:
            return False

        if not Supervisor.objects.filter(user=request.user, is_active=True).exists():
            return False

        return True
