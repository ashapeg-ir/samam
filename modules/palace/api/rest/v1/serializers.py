from rest_framework import serializers

from modules.domain.models import Palace, PalaceKind, PalaceAccountType


class PalaceKindSerializer(serializers.ModelSerializer):
    class Meta:
        model = PalaceKind
        fields = "__all__"
        read_only = ["id"]


class PalaceAccountTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PalaceAccountType
        fields = "__all__"
        read_only = ["id"]


class PalaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Palace
        fields = "__all__"
        read_only = ["id"]
