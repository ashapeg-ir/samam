from rest_framework.parsers import MultiPartParser
from rest_framework.viewsets import ModelViewSet

from modules.domain.models import Department
from modules.common.permissions import CustomerPermission
from modules.department.api.rest.v1.serializers import DepartmentSerializer


class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.none()
    serializer_class = DepartmentSerializer
    permission_classes = [CustomerPermission]
    parser_classes = [MultiPartParser]

    def get_queryset(self):
        return Department.objects.filter(organization__customer_id=self.request.user.id)
