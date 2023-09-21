from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import MultiPartParser

from modules.domain.models import Department
from modules.common.permissions import CustomerPermission
from modules.department.api.rest.v1.serializers import DepartmentSerializer


class DepartmentViewSet(ModelViewSet):
    serializer_class = DepartmentSerializer
    permission_classes = [CustomerPermission]
    parser_classes = [MultiPartParser]

    def get_queryset(self):
        return Department.objects.filter(organization__customer_id=self.request.user.id)
