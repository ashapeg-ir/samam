from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin
from rest_framework.parsers import MultiPartParser
from rest_framework.viewsets import GenericViewSet

from modules.domain.models import Department, TeamDistribution
from modules.common.permissions import CustomerPermission
from modules.organization.api.rest.v1.department.serializers import DepartmentSerializer, TeamDistributionSerializer


class DepartmentViewSet(GenericViewSet, CreateModelMixin, RetrieveModelMixin, ListModelMixin, UpdateModelMixin):
    queryset = Department.objects.none()
    serializer_class = DepartmentSerializer
    permission_classes = [CustomerPermission]
    parser_classes = [MultiPartParser]

    def get_queryset(self):
        return Department.objects.filter(organization__customer_id=self.request.user.id)


class TeamDistributionViewSet(GenericViewSet, CreateModelMixin, RetrieveModelMixin, ListModelMixin, UpdateModelMixin):
    queryset = TeamDistribution.objects.none()
    serializer_class = TeamDistributionSerializer
    permission_classes = [CustomerPermission]

    def get_queryset(self):
        return TeamDistribution.objects.filter(organization__customer_id=self.request.user.id)