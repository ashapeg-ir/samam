from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from modules.domain.models import Profile
from modules.common.permissions import CustomerPermission

from .serializers import UserListSerializer, UserCreateSerializer, UserUpdateSerializer


class UserViewSet(GenericViewSet, ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin):
    queryset = Profile.objects.none()
    permission_classes = [CustomerPermission]
    serializers = {
        "list": UserListSerializer,
        "create": UserCreateSerializer,
        "update": UserUpdateSerializer,
    }

    def get_serializer_class(self):
        return self.serializers[self.action]

    def get_queryset(self):
        return Profile.objects.filter(organization__customer_id=self.request.user.id)
