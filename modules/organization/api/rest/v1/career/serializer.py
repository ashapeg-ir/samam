from rest_framework import serializers

from modules.domain.models import (
    User,
    Grade,
    Gender,
    JobLevel,
    Relation,
    Religion,
    BloodType,
    Department,
    Occupation,
    CareerField,
    CareerGroup,
    FieldOfStudy,
    Organization,
    MaritalStatus,
    EmploymentType,
    MilitaryStatus,
    EmploymentState,
    DegreeCompliance,
    EmploymentStatus,
    OrganizationGraph,
    OrganizationLevel,
    OrganizationNickname,
    ElectronicAnnouncementTitle,
)


class GenderSerializer(serializers.ModelSerializer):
    organization = serializers.PrimaryKeyRelatedField(
        allow_null=False,
        required=True,
        queryset=Organization.objects.all(),
    )
    name = serializers.CharField(max_length=200, allow_blank=False, allow_null=False, required=True)
    created = serializers.DateField(read_only=True)
    updated = serializers.DateField(read_only=True)

    class Meta:
        model = Gender
        fields = ["name", "organization", "created", "updated"]


class OrganizationLevelSerializer(serializers.ModelSerializer):
    organization = serializers.PrimaryKeyRelatedField(
        allow_null=False,
        required=True,
        queryset=Organization.objects.all(),
    )
    name = serializers.CharField(max_length=200, allow_blank=False, allow_null=False, required=True)
    created = serializers.DateField(read_only=True)
    updated = serializers.DateField(read_only=True)

    class Meta:
        model = OrganizationLevel
        fields = ["organization", "name", "created", "updated"]


class OrganizationNicknameSerializer(serializers.ModelSerializer):
    organization = serializers.PrimaryKeyRelatedField(
        allow_null=False,
        required=True,
        queryset=Organization.objects.all(),
    )
    name = serializers.CharField(max_length=200, allow_blank=False, allow_null=False, required=True)
    created = serializers.DateField(read_only=True)
    updated = serializers.DateField(read_only=True)

    class Meta:
        model = OrganizationNickname
        fields = ["organization", "name", "created", "updated"]


class OrganizationGraphSerializer(serializers.ModelSerializer):
    organization = serializers.PrimaryKeyRelatedField(
        allow_null=False,
        allow_empty=False,
        required=True,
        queryset=Organization.objects.all(),
    )
    department = serializers.PrimaryKeyRelatedField(
        allow_null=False,
        allow_empty=False,
        required=True,
        queryset=Department.objects.all(),
    )
    occupation = serializers.PrimaryKeyRelatedField(
        allow_null=False,
        allow_empty=False,
        required=True,
        queryset=Occupation.objects.all(),
    )
    career_field = serializers.PrimaryKeyRelatedField(
        allow_null=False,
        allow_empty=False,
        required=True,
        queryset=CareerField.objects.all(),
    )
    electronic_announcement_title = serializers.PrimaryKeyRelatedField(
        allow_null=False,
        allow_empty=False,
        required=True,
        queryset=ElectronicAnnouncementTitle.objects.all(),
    )
    career_group = serializers.PrimaryKeyRelatedField(
        allow_null=False,
        allow_empty=False,
        required=True,
        queryset=CareerGroup.objects.all(),
    )
    organization_level = serializers.PrimaryKeyRelatedField(
        allow_null=False,
        allow_empty=False,
        required=True,
        queryset=OrganizationLevel.objects.all(),
    )
    communicator = serializers.PrimaryKeyRelatedField(
        allow_null=False,
        allow_empty=False,
        required=False,
        queryset=User.objects.filter(is_active=True, is_verified=True),
    )
    obligate_to_job_description = serializers.IntegerField(
        required=True,
        allow_null=False,
        min_value=0,
        max_value=2,
        help_text="none=0, electronic=1, paper=2"
    )
    obligate_to_announcement = serializers.IntegerField(
        required=True,
        allow_null=False,
        min_value=0,
        max_value=2,
        help_text="none=0, electronic=1, paper=2"
    )
    row_name = serializers.CharField(
        required=True,
        allow_null=False,
        allow_blank=True,
        max_length=200,
    )
    row_full_name = serializers.CharField(
        required=True,
        allow_null=False,
        allow_blank=True,
        max_length=250,
    )
    number = serializers.IntegerField(
        required=True,
        allow_null=False,
    )
    name = serializers.CharField(max_length=200, allow_blank=False, allow_null=False, required=True)
    created = serializers.DateField(read_only=True)
    updated = serializers.DateField(read_only=True)

    class Meta:
        model = OrganizationGraph
        fields = [
            "department",
            "organization",
            "occupation",
            "career_field",
            "electronic_announcement_title",
            "career_group",
            "organization_level",
            "obligate_to_job_description",
            "obligate_to_announcement",
            "row_name",
            "row_full_name",
            "number",
            "communicator",
            "name",
            "created",
            "updated",
        ]
        read_only_fields = ["id", "created", "updated"]


class RelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relation
        fields = "__all__"
        read_only_fields = ["id", "created", "updated"]


class MaritalStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaritalStatus
        fields = "__all__"
        read_only_fields = ["id", "created", "updated"]


class FieldOfStudySerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldOfStudy
        fields = "__all__"
        read_only_fields = ["id", "created", "updated"]


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = "__all__"
        read_only_fields = ["id", "created", "updated"]


class OccupationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Occupation
        fields = "__all__"
        read_only_fields = ["id", "created", "updated"]


class CareerFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerField
        fields = "__all__"
        read_only_fields = ["id", "created", "updated"]


class EmploymentStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmploymentState
        fields = "__all__"
        read_only_fields = ["id", "created", "updated"]


class ElectronicAnnouncementTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectronicAnnouncementTitle
        fields = "__all__"
        read_only_fields = ["id", "created", "updated"]


class MilitaryStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = MilitaryStatus
        fields = "__all__"
        read_only_fields = ["id", "created", "updated"]


class CareerGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerGroup
        fields = "__all__"
        read_only_fields = ["id", "created", "updated"]


class BloodTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodType
        fields = "__all__"
        read_only_fields = ["id", "created", "updated"]


class DegreeComplianceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DegreeCompliance
        fields = "__all__"
        read_only_fields = ["id", "created", "updated"]


class JobLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobLevel
        fields = "__all__"
        read_only_fields = ["id", "created", "updated"]


class ReligionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Religion
        fields = "__all__"
        read_only_fields = ["id", "created", "updated"]


class EmploymentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmploymentType
        fields = "__all__"
        read_only_fields = ["id", "created", "updated"]


class EmploymentStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmploymentStatus
        fields = "__all__"
        read_only_fields = ["id", "created", "updated"]
