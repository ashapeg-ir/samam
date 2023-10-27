from rest_framework import serializers
from modules.domain.models import Position, Organization, EmploymentType, EmploymentStatus


class PositionSerializer(serializers.ModelSerializer):
    organization = serializers.PrimaryKeyRelatedField(
        allow_null=False,
        required=True,
        queryset=Organization.objects.all(),
    )
    created = serializers.DateField(read_only=True)
    updated = serializers.DateField(read_only=True)

    class Meta:
        model = Position
        fields = [
            "phone",
            "organization",
            "organization_graph",
            "employment_type",
            "city",
            "region",
            "postal_code",
            "email",
            "employment_status",
            "job_level",
            "is_main",
            "created",
            "updated",
        ]
        read_only = ["id"]
