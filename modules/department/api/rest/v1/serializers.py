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

    def validate(self, attrs):
        place = attrs.get("place")
        is_private = attrs.get("is_private")
        if not place.is_team and is_private:
            raise serializers.ValidationError("This place is not a team you cant set the department private.")
        return attrs
