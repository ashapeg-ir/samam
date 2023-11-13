from rest_framework import exceptions
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.viewsets import GenericViewSet

from modules.domain.models import (
    Palace,
    PalaceKind,
    PalaceLevel,
    Organization,
    PalaceStatus,
    PalaceAccountType,
    PalaceOwnershipType,
)
from modules.common.permissions import SupervisorPermission
from modules.organization.api.rest.v1.palace.serializers import (
    PalaceSerializer,
    PalaceKindSerializer,
    PalaceLevelSerializer,
    PalaceStatusSerializer,
    PalaceOwnershipSerializer,
    PalaceAccountTypeSerializer,
)


class PalaceOwnershipTypeViewSet(GenericViewSet, CreateModelMixin, RetrieveModelMixin, ListModelMixin, UpdateModelMixin):
    queryset = PalaceOwnershipType.objects.none()
    serializer_class = PalaceOwnershipSerializer
    permission_classes = [SupervisorPermission]

    def get_queryset(self):
        return PalaceOwnershipType.objects.filter(organization__customer_id=self.request.user.id)

    def perform_create(self, serializer):
        if Organization.objects.get(customer_id=self.request.user) != serializer.validated_data["organization"]:
            raise exceptions.PermissionDenied
        super().perform_create(serializer)


class PalaceStatusViewSet(GenericViewSet, CreateModelMixin, RetrieveModelMixin, ListModelMixin, UpdateModelMixin):
    queryset = PalaceStatus.objects.none()
    serializer_class = PalaceStatusSerializer
    permission_classes = [SupervisorPermission]

    def get_queryset(self):
        return PalaceStatus.objects.filter(organization__customer_id=self.request.user.id)

    def perform_create(self, serializer):
        if Organization.objects.get(customer_id=self.request.user) != serializer.validated_data["organization"]:
            raise exceptions.PermissionDenied
        super().perform_create(serializer)


class PalaceLevelViewSet(GenericViewSet, CreateModelMixin, RetrieveModelMixin, ListModelMixin, UpdateModelMixin):
    queryset = PalaceLevel.objects.none()
    serializer_class = PalaceLevelSerializer
    permission_classes = [SupervisorPermission]

    def get_queryset(self):
        return PalaceLevel.objects.filter(organization__customer_id=self.request.user.id)

    def perform_create(self, serializer):
        if Organization.objects.get(customer_id=self.request.user) != serializer.validated_data["organization"]:
            raise exceptions.PermissionDenied
        super().perform_create(serializer)


class PalaceViewSet(GenericViewSet, CreateModelMixin, RetrieveModelMixin, ListModelMixin, UpdateModelMixin):
    queryset = Palace.objects.none()
    serializer_class = PalaceSerializer
    permission_classes = [SupervisorPermission]
    parser_classes = [MultiPartParser, FormParser]

    def get_queryset(self):
        return Palace.objects.filter(organization__customer_id=self.request.user.id)

    def perform_create(self, serializer):
        if Organization.objects.get(customer_id=self.request.user) != serializer.validated_data["organization"]:
            raise exceptions.PermissionDenied
        super().perform_create(serializer)


class PalaceKindViewSet(GenericViewSet, CreateModelMixin, RetrieveModelMixin, ListModelMixin, UpdateModelMixin):
    queryset = PalaceKind.objects.none()
    serializer_class = PalaceKindSerializer
    permission_classes = [SupervisorPermission]

    def get_queryset(self):
        return PalaceKind.objects.filter(organization__customer_id=self.request.user.id)

    def perform_create(self, serializer):
        if Organization.objects.get(customer_id=self.request.user) != serializer.validated_data["organization"]:
            raise exceptions.PermissionDenied
        super().perform_create(serializer)


class PalaceAccountTypeViewSet(GenericViewSet, CreateModelMixin, RetrieveModelMixin, ListModelMixin, UpdateModelMixin):
    queryset = PalaceAccountType.objects.none()
    serializer_class = PalaceAccountTypeSerializer
    permission_classes = [SupervisorPermission]

    def get_queryset(self):
        return PalaceAccountType.objects.filter(organization__customer_id=self.request.user.id)

    def perform_create(self, serializer):
        if Organization.objects.get(customer_id=self.request.user) != serializer.validated_data["organization"]:
            raise exceptions.PermissionDenied
        super().perform_create(serializer)
