from rest_framework import serializers
from modules.domain.models import User, Department, Organization, TeamDistribution


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = [
            "place",
            "phone",
            "description",
            "is_private",
            "parent",
            "email",
            "land_area",
            "noble_area",
            "operation_date",
            "completion_date",
            "completion_certificate",
            "status",
            "ownership",
            "palace",
            "organization",
        ]
        read_only_fields = ["id"]

    def validate(self, attrs):
        place = attrs.get("place")
        is_private = attrs.get("is_private")
        if not place.is_team and is_private:
            raise serializers.ValidationError("This place is not a team you cant set the department private.")
        return attrs


class TeamDistributionSerializer(serializers.ModelSerializer):
    organization = serializers.PrimaryKeyRelatedField(
        allow_null=False,
        required=True,
        queryset=Organization.objects.all(),
    )
    department = serializers.PrimaryKeyRelatedField(
        allow_null=False,
        required=True,
        queryset=Department.objects.filter(place__is_team=True),
    )
    user = serializers.PrimaryKeyRelatedField(
        allow_null=False,
        required=True,
        queryset=User.objects.filter(is_supervisor=False, is_active=True, is_verified=True),
    )
    name = serializers.CharField(max_length=150, allow_null=False, allow_blank=False, required=True)
    created = serializers.DateField(read_only=True)
    updated = serializers.DateField(read_only=True)

    class Meta:
        model = TeamDistribution
        fields = [
            "department",
            "organization",
            "is_active",
            "created",
            "updated",
        ]
        read_only_fields = ["id"]
