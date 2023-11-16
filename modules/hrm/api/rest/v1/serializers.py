from django.contrib.auth.models import update_last_login

from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.serializers import TokenObtainSerializer


class SupervisorLoginSerializer(serializers.Serializer):
    username = serializers.CharField(
        required=True,
        allow_null=False,
        allow_blank=False,
        max_length=15,
        help_text="phone number",
    )

    class Meta:
        fields = ["username"]


class SupervisorLoginResponseSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=15, min_length=15)
    message = serializers.CharField()
    code = serializers.IntegerField()

    class Meta:
        fields = ["username", "message", "code"]


class CustomTokenObtainPairSerializer(TokenObtainSerializer):
    token_class = RefreshToken

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        data["id"] = self.user.pk
        data["username"] = self.user.username
        data["first_name"] = self.user.first_name
        data["last_name"] = self.user.last_name
        data["is_active"] = self.user.is_verified
        data["is_supervisor"] = self.user.is_supervisor
        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data
