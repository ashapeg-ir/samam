from rest_framework import serializers

from modules.domain.models import City, Place, Country, Province, Organization


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"
        read_only = ["id"]


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"
        read_only = ["id"]


class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = "__all__"
        read_only = ["id"]


class OrganizationSerializer(serializers.ModelSerializer):
    language = serializers.CharField(max_length=2, allow_null=False, allow_blank=False)
    name = serializers.CharField(max_length=50, allow_null=False, allow_blank=False)

    class Meta:
        model = Organization
        fields = ["name", "language", "id"]
        read_only = ["id"]


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = "__all__"
        read_only = ["id"]
