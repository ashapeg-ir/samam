from rest_framework import exceptions, serializers

from modules.domain.models import Palace, PalaceKind, PalaceLevel, PalaceStatus, PalaceAccountType, PalaceOwnershipType


class PalaceOwnershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = PalaceOwnershipType
        fields = [
            "name",
            "organization",
        ]
        read_oly = ["id", "created", "updated"]


class PalaceLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PalaceLevel
        fields = [
            "name",
            "organization",
            "is_provincial_unit",
            "is_executive_unit",
            "is_provider",
            "is_top_notch_organization",
        ]
        read_oly = ["id", "created", "updated"]

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
    class Meta:
        model = PalaceStatus
        fields = [
            "name",
            "organization",
            "is_active",
        ]
        read_oly = ["id", "created", "updated"]


class PalaceKindSerializer(serializers.ModelSerializer):
    class Meta:
        model = PalaceKind
        fields = [
            "name",
            "organization",
        ]
        read_only = ["id", "created", "updated"]


class PalaceAccountTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PalaceAccountType
        fields = [
            "name",
            "organization",
        ]
        read_only = ["id", "created", "updated"]


class PalaceSerializer(serializers.ModelSerializer):
    banner = serializers.FileField()
    logo = serializers.FileField()

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
