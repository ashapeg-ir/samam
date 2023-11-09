from rest_framework import exceptions, serializers

from modules.domain.models import (
    City,
    Palace,
    PalaceKind,
    PalaceLevel,
    Organization,
    PalaceStatus,
    PalaceAccountType,
    PalaceOwnershipType,
)


class PalaceOwnershipSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=150, allow_null=False, allow_blank=False, required=True)
    organization = serializers.PrimaryKeyRelatedField(
        allow_null=False,
        required=True,
        queryset=Organization.objects.all(),
    )
    created = serializers.DateField(read_only=True)
    updated = serializers.DateField(read_only=True)

    class Meta:
        model = PalaceOwnershipType
        fields = [
            "id",
            "name",
            "organization",
            "created",
            "updated",
        ]
        read_oly = ["id"]


class PalaceLevelSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=150, allow_null=False, allow_blank=False, required=True)
    organization = serializers.PrimaryKeyRelatedField(
        allow_null=False,
        required=True,
        queryset=Organization.objects.all(),
    )
    is_provincial_unit = serializers.BooleanField(default=False)
    is_executive_unit = serializers.BooleanField(default=False)
    is_provider = serializers.BooleanField(default=False)
    is_top_notch_organization = serializers.BooleanField(default=False)
    created = serializers.DateField(read_only=True)
    updated = serializers.DateField(read_only=True)

    class Meta:
        model = PalaceLevel
        fields = [
            "name",
            "organization",
            "is_provincial_unit",
            "is_executive_unit",
            "is_provider",
            "is_top_notch_organization",
            "created",
            "updated",
        ]
        read_oly = ["id"]

    def validate(self, attrs):
        # Count the number of True values in the boolean fields
        true_fields_count = sum([attrs.get(field, False) for field in [
            "is_provincial_unit",
            "is_executive_unit",
            "is_provider",
            "is_top_notch_organization",
        ]])

        # Check if more than one boolean field is set to True
        if true_fields_count > 1:
            raise exceptions.ValidationError("Only one boolean field can be True")

        return attrs


class PalaceStatusSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=150, allow_null=False, allow_blank=False, required=True)
    organization = serializers.PrimaryKeyRelatedField(
        allow_null=False,
        required=True,
        queryset=Organization.objects.all(),
    )
    is_active = serializers.BooleanField(default=False)
    created = serializers.DateField(read_only=True)
    updated = serializers.DateField(read_only=True)

    class Meta:
        model = PalaceStatus
        fields = [
            "id",
            "name",
            "organization",
            "is_active",
            "created",
            "updated",
        ]
        read_oly = ["id"]


class PalaceKindSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=150, allow_null=False, allow_blank=False, required=True)
    organization = serializers.PrimaryKeyRelatedField(
        allow_null=False,
        required=True,
        queryset=Organization.objects.all(),
    )
    created = serializers.DateField(read_only=True)
    updated = serializers.DateField(read_only=True)

    class Meta:
        model = PalaceKind
        fields = [
            "id",
            "name",
            "organization",
            "created",
            "updated"
        ]
        read_only = ["id"]


class PalaceAccountTypeSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=150, allow_null=False, allow_blank=False, required=True)
    organization = serializers.PrimaryKeyRelatedField(
        allow_null=False,
        required=True,
        queryset=Organization.objects.all(),
    )
    created = serializers.DateField(read_only=True)
    updated = serializers.DateField(read_only=True)

    class Meta:
        model = PalaceAccountType
        fields = [
            "id",
            "name",
            "organization",
            "created",
            "updated",
        ]
        read_only = ["id"]


class PalaceSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=150, allow_null=False, allow_blank=False, required=True)
    banner = serializers.FileField()
    logo = serializers.FileField()
    organization = serializers.PrimaryKeyRelatedField(
        allow_null=False,
        required=True,
        queryset=Organization.objects.all(),
    )
    status = serializers.PrimaryKeyRelatedField(
        allow_null=False,
        required=True,
        queryset=PalaceStatus.objects.all(),
    )
    parent = serializers.PrimaryKeyRelatedField(
        allow_null=False,
        required=True,
        queryset=Organization.objects.all(),
    )
    city = serializers.PrimaryKeyRelatedField(
        allow_null=False,
        required=True,
        queryset=City.objects.all(),
    )
    account_type = serializers.PrimaryKeyRelatedField(
        allow_null=False,
        required=True,
        queryset=PalaceAccountType.objects.all(),
    )
    kind = serializers.PrimaryKeyRelatedField(
        allow_null=False,
        required=True,
        queryset=PalaceKind.objects.all(),
    )
    is_private = serializers.BooleanField(default=False)
    land_area = serializers.IntegerField(required=False)
    noble_area = serializers.IntegerField(required=False)
    distance_to_province = serializers.IntegerField(required=False)
    distance_to_same_palace = serializers.IntegerField(required=False)
    ownership_type = serializers.PrimaryKeyRelatedField(
        allow_null=False,
        required=True,
        queryset=PalaceOwnershipType.objects.all(),
    )
    palace_level = serializers.PrimaryKeyRelatedField(
        allow_null=False,
        required=True,
        queryset=PalaceLevel.objects.all(),
    )
    phone = serializers.CharField(max_length=15, required=True)
    email = serializers.EmailField(required=False)
    website = serializers.URLField(required=False)
    postal_code = serializers.CharField(max_length=10, required=False)
    description = serializers.CharField(required=False)

    class Meta:
        model = Palace
        fields = [
            "name",
            "organization",
            "status",
            "banner",
            "logo",
            "address",
            "parent",
            "city",
            "account_type",
            "kind",
            "is_private",
            "land_area",
            "noble_area",
            "distance_to_province",
            "distance_to_same_palace",
            "operation_date",
            "completion_certificate",
            "completion_date",
            "ownership_type",
            "operation_license",
            "palace_level",
            "phone",
            "email",
            "website",
            "postal_code",
            "description",
        ]
        read_only = ["id", "created", "updated"]
