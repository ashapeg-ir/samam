from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.viewsets import GenericViewSet

from modules.domain.models import Palace, PalaceKind, PalaceLevel, PalaceStatus, PalaceAccountType, PalaceOwnershipType
from modules.common.permissions import CustomerPermission
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
    permission_classes = [CustomerPermission]

    def get_queryset(self):
        return PalaceOwnershipType.objects.filter(organization__customer_id=self.request.user.id)


class PalaceStatusViewSet(GenericViewSet, CreateModelMixin, RetrieveModelMixin, ListModelMixin, UpdateModelMixin):
    queryset = PalaceStatus.objects.none()
    serializer_class = PalaceStatusSerializer
    permission_classes = [CustomerPermission]

    def get_queryset(self):
        return PalaceStatus.objects.filter(organization__customer_id=self.request.user.id)


class PalaceLevelViewSet(GenericViewSet, CreateModelMixin, RetrieveModelMixin, ListModelMixin, UpdateModelMixin):
    queryset = PalaceLevel.objects.none()
    serializer_class = PalaceLevelSerializer
    permission_classes = [CustomerPermission]

    def get_queryset(self):
        return PalaceLevel.objects.filter(organization__customer_id=self.request.user.id)


class PalaceViewSet(GenericViewSet, CreateModelMixin, RetrieveModelMixin, ListModelMixin, UpdateModelMixin):
    queryset = Palace.objects.none()
    serializer_class = PalaceSerializer
    permission_classes = [CustomerPermission]
    parser_classes = [MultiPartParser, FormParser]

    def get_queryset(self):
        return Palace.objects.filter(organization__customer_id=self.request.user.id)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class PalaceKindViewSet(GenericViewSet, CreateModelMixin, RetrieveModelMixin, ListModelMixin, UpdateModelMixin):
    queryset = PalaceKind.objects.none()
    serializer_class = PalaceKindSerializer
    permission_classes = [CustomerPermission]

    def get_queryset(self):
        return PalaceKind.objects.filter(organization__customer_id=self.request.user.id)


class PalaceAccountTypeViewSet(GenericViewSet, CreateModelMixin, RetrieveModelMixin, ListModelMixin, UpdateModelMixin):
    queryset = PalaceAccountType.objects.none()
    serializer_class = PalaceAccountTypeSerializer
    permission_classes = [CustomerPermission]

    def get_queryset(self):
        return PalaceAccountType.objects.filter(organization__customer_id=self.request.user.id)
