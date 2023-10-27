from modules.organization.api.rest.v1.position.serializers import PositionSerializer
from modules.domain.models import Position, Organization
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet


class PositionViewSet(GenericViewSet, ListModelMixin, CreateModelMixin, RetrieveModelMixin):
    queryset = Position.objects.none()
    serializer_class = PositionSerializer

    def get_queryset(self):
        return Position.objects.filter(organization__customer_id=self.request.user.id)
