from rest_framework import serializers, exceptions

from modules.domain.models import City, Place, Country, Province, Organization, PlaceAccountType


class PlaceAccountTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceAccountType
        fields = [
            "name",
            "organization",
        ]
        read_only = ["id"]


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = [
            "name",
            "organization",
        ]
        read_only = ["id", "created", "updated"]


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = [
            "name",
            "province",
            "organization",
        ]
        read_only = ["id", "created", "updated"]


class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = [
            "name",
            "country",
            "organization",
        ]
        read_only = ["id", "created", "updated"]


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
        fields = [
            "organization",
            "palace",
            "name",
            "account_type",
            "is_workplace",
            "is_equipment_location",
            "is_committee",
            "is_team",
            "is_management_leadership",
        ]
        read_only = ["id", "created", "updated"]

    def validate(self, attrs):
        # Count the number of True values in the boolean fields
        true_fields_count = sum([attrs.get(field, False) for field in [
            "is_workplace",
            "is_equipment_location",
            "is_committee",
            "is_team",
            "is_management_leadership",
        ]])

        # Check if more than one boolean field is set to True
        if true_fields_count > 1:
            raise exceptions.ValidationError("Only one boolean field can be True")

        return attrs
