from rest_framework import serializers

from modules.domain.models import Department


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
