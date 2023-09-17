from rest_framework import serializers

from modules.domain.models import Department


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        exclude = ["is_active", "is_removed"]
        read_only = ["id"]
