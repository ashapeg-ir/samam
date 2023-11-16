from django.contrib.auth.models import AnonymousUser
from modules.domain.models import PalaceSupervisor
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

        if not PalaceSupervisor.objects.filter(user=request.user, is_active=True).exists():
            return False

        return True

    def has_object_permission(self, request, view, obj):
        if not PalaceSupervisor.objects.filter(user=request.user, palace=obj).exists():
            return False
        return True
