from django.conf import settings

from rest_framework import status, exceptions
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from modules.domain.models import City, Place, Country, Province, Organization, PlaceAccountType, get_message
from modules.common.messages import samam
from modules.common.permissions import SupervisorPermission
from modules.organization.api.rest.v1.serializers import (
    CitySerializer,
    PlaceSerializer,
    CountrySerializer,
    ProvinceSerializer,
    OrganizationSerializer,
    PlaceAccountTypeSerializer,
)


class OrganizationViewSet(GenericViewSet, CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [SupervisorPermission]

    def get_queryset(self):
        return Organization.objects.filter(customer_id=self.request.user.id)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if Organization.objects.filter(customer_id=self.request.user.id).count() >= settings.SAMAM_ORG_LIMIT:
            message = get_message(code=samam.ORGANIZATION_CREATION_LIMIT, language=serializer.validated_data["language"])
            raise exceptions.ValidationError(detail=message)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        language = serializer.validated_data["language"]
        data = {
            "message": get_message(code=samam.ORGANIZATION_CREATED, language=language),
            **serializer.validated_data,
        }
        return Response(data=data, headers=headers, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)


class PlaceViewSet(GenericViewSet, CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin):
    queryset = Place.objects.none()
    serializer_class = PlaceSerializer
    permission_classes = [SupervisorPermission]

    def get_queryset(self):
        return Place.objects.filter(organization__customer_id=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        language = Organization.objects.get(customer_id=self.request.user.id).language
        data = {
            "message": get_message(code=samam.ORGANIZATION_CREATED, language=language),
        }
        return Response(data=data, headers=headers, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        if Organization.objects.get(customer_id=self.request.user) != serializer.validated_data["organization"]:
            raise exceptions.PermissionDenied
        super().perform_create(serializer)


class CountryViewSet(GenericViewSet, CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin):
    queryset = Country.objects.none()
    serializer_class = CountrySerializer
    permission_classes = [SupervisorPermission]

    def get_queryset(self):
        return Country.objects.filter(organization__customer_id=self.request.user)


class ProvinceViewSet(GenericViewSet, CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin):
    queryset = Province.objects.none()
    serializer_class = ProvinceSerializer
    permission_classes = [SupervisorPermission]

    def get_queryset(self):
        return Province.objects.filter(organization__customer_id=self.request.user)


class CityViewSet(GenericViewSet, CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin):
    queryset = City.objects.none()
    serializer_class = CitySerializer
    permission_classes = [SupervisorPermission]

    def get_queryset(self):
        return City.objects.filter(organization__customer_id=self.request.user)


class PlaceAccountTypeViewSet(GenericViewSet, CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin):
    queryset = PlaceAccountType.objects.none()
    serializer_class = PlaceAccountTypeSerializer
    permission_classes = [SupervisorPermission]

    def get_queryset(self):
        return PlaceAccountType.objects.filter(organization__customer_id=self.request.user.id)
