from rest_framework import serializers

from modules.domain.models import Department


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"
        read_only = ["id"]
