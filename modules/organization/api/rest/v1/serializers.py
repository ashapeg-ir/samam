from rest_framework import exceptions, serializers

from modules.domain.models import City, Place, Country, Province, Organization, PlaceAccountType


class PlaceAccountTypeSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=150, allow_null=False, allow_blank=False, required=True)
    organization = serializers.PrimaryKeyRelatedField(
        allow_null=False,
        required=True,
        queryset=Organization.objects.all(),
    )
    created = serializers.DateField(read_only=True)
    updated = serializers.DateField(read_only=True)

    class Meta:
        model = PlaceAccountType
        fields = [
            "name",
            "organization",
            "created",
            "updated",
        ]


class CountrySerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=150, allow_null=False, allow_blank=False, required=True)
    organization = serializers.PrimaryKeyRelatedField(
        allow_null=False,
        required=True,
        queryset=Organization.objects.all(),
    )
    created = serializers.DateField(read_only=True)
    updated = serializers.DateField(read_only=True)

    class Meta:
        model = Country
        fields = [
            "name",
            "organization",
            "created",
            "updated",
        ]


class CitySerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=150, allow_null=False, allow_blank=False, required=True)
    province = serializers.PrimaryKeyRelatedField(
        allow_null=False,
        required=True,
        queryset=Province.objects.all(),
    )
    organization = serializers.PrimaryKeyRelatedField(
        allow_null=False,
        required=True,
        queryset=Organization.objects.all(),
    )
    created = serializers.DateField(read_only=True)
    updated = serializers.DateField(read_only=True)

    class Meta:
        model = City
        fields = [
            "name",
            "province",
            "organization",
            "created",
            "updated",
        ]


class ProvinceSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=150, allow_null=False, allow_blank=False, required=True)
    country = serializers.PrimaryKeyRelatedField(
        allow_null=False,
        required=True,
        queryset=Country.objects.all(),
    )
    organization = serializers.PrimaryKeyRelatedField(
        allow_null=False,
        required=True,
        queryset=Organization.objects.all(),
    )
    created = serializers.DateField(read_only=True)
    updated = serializers.DateField(read_only=True)

    class Meta:
        model = Province
        fields = [
            "name",
            "country",
            "organization",
            "created",
            "updated",
        ]


class OrganizationSerializer(serializers.ModelSerializer):
    language = serializers.CharField(max_length=2, allow_null=False, allow_blank=False, help_text="fa")
    name = serializers.CharField(max_length=50, allow_null=False, allow_blank=False, required=True)

    class Meta:
        model = Organization
        fields = ["name", "language", "id"]
        read_only = ["id"]


class PlaceSerializer(serializers.ModelSerializer):
    organization = serializers.PrimaryKeyRelatedField(
        allow_null=False,
        required=True,
        queryset=Organization.objects.all(),
    )
    palace = serializers.PrimaryKeyRelatedField(
        allow_null=False,
        required=True,
        queryset=Place.objects.all(),
    )
    name = serializers.CharField(max_length=250, allow_null=False, allow_blank=False, required=True)
    account_type = serializers.PrimaryKeyRelatedField(
        allow_null=False,
        required=True,
        queryset=PlaceAccountType.objects.all(),
    )
    is_workplace = serializers.BooleanField(default=False)
    is_equipment_location = serializers.BooleanField(default=False)
    is_committee = serializers.BooleanField(default=False)
    is_team = serializers.BooleanField(default=False)
    is_management_leadership = serializers.BooleanField(default=False)

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
