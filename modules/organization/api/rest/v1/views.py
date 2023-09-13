from rest_framework import status, exceptions
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from modules.domain.models import Place, Organization, get_message
from modules.common.permissions import CustomerPermission
from modules.organization.api.rest.v1.serializers import PlaceSerializer, OrganizationSerializer
from modules.common.messages import samam


class OrganizationViewSet(GenericViewSet, CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [CustomerPermission]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        language = serializer.validated_data["language"]
        data = {
            "message": get_message(code=samam.ORGANIZATION_CREATED, language=language),
            "data": serializer.validated_data,
        }
        return Response(data=data, headers=headers, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)


class PlaceViewSet(ModelViewSet):
    serializer_class = PlaceSerializer
    permission_classes = [CustomerPermission]

    def get_queryset(self):
        return Place.objects.filter(user=self.request.user)
