from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from modules.domain.models import Palace, PalaceKind, PalaceAccountType
from modules.common.permissions import CustomerPermission
from modules.palace.api.rest.v1.serializers import PalaceSerializer, PalaceKindSerializer, PalaceAccountTypeSerializer


class PalaceViewSet(GenericViewSet, CreateModelMixin, RetrieveModelMixin, ListModelMixin, UpdateModelMixin):
    serializer_class = PalaceSerializer
    permission_classes = [CustomerPermission]

    def get_queryset(self):
        return Palace.objects.filter(organization__customer_id=self.request.user.id)


class PalaceKindViewSet(ModelViewSet):
    serializer_class = PalaceKindSerializer
    permission_classes = [CustomerPermission]

    def get_queryset(self):
        return PalaceKind.objects.filter(organization__customer_id=self.request.user.id)


class PalaceAccountTypeViewSet(ModelViewSet):
    serializer_class = PalaceAccountTypeSerializer
    permission_classes = [CustomerPermission]

    def get_queryset(self):
        return PalaceAccountType.objects.filter(organization__customer_id=self.request.user.id)
