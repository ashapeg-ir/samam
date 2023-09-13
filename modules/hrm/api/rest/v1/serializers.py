from django.contrib.auth.models import update_last_login

from rest_framework import exceptions, serializers
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.serializers import TokenObtainSerializer

from .backends import user_authenticate


class CustomerLoginSerializer(serializers.Serializer):
    phone = serializers.CharField(required=True)

    class Meta:
        fields = ["phone"]


class CustomerLoginResponseSerializer(serializers.Serializer):
    phone = serializers.CharField(required=True)
    message = serializers.CharField()
    code = serializers.IntegerField()

    class Meta:
        fields = ["phone", "message", "code"]


class CustomTokenObtainPairSerializer(TokenObtainSerializer):
    token_class = RefreshToken

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        data["id"] = self.user.pk
        data["phone"] = self.user.phone
        data["first_name"] = self.user.first_name
        data["last_name"] = self.user.last_name
        data["is_active"] = self.user.is_verified
        data["is_customer"] = self.user.is_customer
        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data


class UserLoginSerializer(TokenObtainSerializer):
    token_class = RefreshToken

    def validate(self, attrs):
        authenticate_kwargs = {
            self.username_field: attrs[self.username_field],
            "password": attrs["password"],
        }
        try:
            authenticate_kwargs["request"] = self.context["request"]
        except KeyError:
            pass

        self.user = user_authenticate(**authenticate_kwargs)
        if not api_settings.USER_AUTHENTICATION_RULE(self.user):
            raise exceptions.AuthenticationFailed(
                self.error_messages["no_active_account"],
                "no_active_account",
            )

        refresh = self.get_token(self.user)
        data = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "id": self.user.pk,
            "phone": self.user.phone,
            "first_name": self.user.first_name,
            "last_name": self.user.last_name,
            "is_active": self.user.is_verified,
            "is_customer": self.user.is_customer,
        }
        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data

