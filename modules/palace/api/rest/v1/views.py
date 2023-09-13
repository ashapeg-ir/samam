from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from modules.domain.models import Palace
from modules.common.permissions import CustomerPermission
from modules.palace.api.rest.v1.serializers import PalaceSerializer


class PalaceViewSet(GenericViewSet, CreateModelMixin, RetrieveModelMixin, ListModelMixin, UpdateModelMixin):
    serializer_class = PalaceSerializer
    permission_classes = [CustomerPermission]

    def get_queryset(self):
        return Palace.objects.filter(user=self.request.user)
