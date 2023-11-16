from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action

from modules.domain.models import User
from modules.hrm.api.rest.v1.business_logic import AuthBusinessV1

from .serializers import (
    SupervisorLoginSerializer,
    SupervisorLoginResponseSerializer,
    CustomTokenObtainPairSerializer,
)


class SupervisorLoginViewSet(GenericViewSet):
    queryset = User.objects.all()
    business = AuthBusinessV1
    permission_classes = [permissions.AllowAny]

    def get_serializer_class(self):
        if self.action == 'login':
            return SupervisorLoginSerializer
        if self.action == 'get_token':
            return CustomTokenObtainPairSerializer

    @action(detail=False, methods=['post'], url_path=r'login')
    def login(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        code = self.business.send_sms(serializer.validated_data["username"])
        response = SupervisorLoginResponseSerializer({
            'username': serializer.validated_data['username'],
            'message': "message send successfully",
            "code": code,
        })
        return Response(data=response.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'], url_path=r'get_token')
    def get_token(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(data=serializer.validated_data, status=status.HTTP_200_OK)
