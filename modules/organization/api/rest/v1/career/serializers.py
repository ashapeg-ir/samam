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
        fields = ["id", "name", "organization", "created", "updated"]
        read_only_fields = ["id"]


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
        fields = ["id", "organization", "name", "created", "updated"]
        read_only_fields = ["id"]


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
        fields = ["id", "organization", "name", "created", "updated"]
        read_only_fields = ["id"]


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
            "id",
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
        read_only_fields = ["id"]


class RelationSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200, allow_blank=False, allow_null=False, required=True)
    organization = serializers.PrimaryKeyRelatedField(
        allow_null=False,
        required=True,
        queryset=Organization.objects.all(),
    )
    created = serializers.DateField(read_only=True)
    updated = serializers.DateField(read_only=True)

    class Meta:
        model = Relation
        fields = [
            "id",
            "name",
            "organization",
            "created",
            "updated",
        ]
        read_only_fields = ["id"]


class MaritalStatusSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200, allow_blank=False, allow_null=False, required=True)
    organization = serializers.PrimaryKeyRelatedField(
        allow_null=False,
        required=True,
        queryset=Organization.objects.all(),
    )
    created = serializers.DateField(read_only=True)
    updated = serializers.DateField(read_only=True)

    class Meta:
        model = MaritalStatus
        fields = [
            "id",
            "name",
            "organization",
            "created",
            "updated",
        ]
        read_only_fields = ["id"]


class FieldOfStudySerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200, allow_blank=False, allow_null=False, required=True)
    organization = serializers.PrimaryKeyRelatedField(
        allow_null=False,
        required=True,
        queryset=Organization.objects.all(),
    )
    created = serializers.DateField(read_only=True)
    updated = serializers.DateField(read_only=True)

    class Meta:
        model = FieldOfStudy
        fields = [
            "id",
            "name",
            "organization",
            "created",
            "updated",
        ]
        read_only_fields = ["id"]


class GradeSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200, allow_blank=False, allow_null=False, required=True)
    organization = serializers.PrimaryKeyRelatedField(
        allow_null=False,
        required=True,
        queryset=Organization.objects.all(),
    )
    created = serializers.DateField(read_only=True)
    updated = serializers.DateField(read_only=True)

    class Meta:
        model = Grade
        fields = [
            "name",
            "organization",
            "created",
            "updated",
        ]
        read_only_fields = ["id"]


class OccupationSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200, allow_blank=False, allow_null=False, required=True)
    organization = serializers.PrimaryKeyRelatedField(
        allow_null=False,
        required=True,
        queryset=Organization.objects.all(),
    )
    created = serializers.DateField(read_only=True)
    updated = serializers.DateField(read_only=True)

    class Meta:
        model = Occupation
        fields = [
            "id",
            "name",
            "organization",
            "created",
            "updated",
        ]
        read_only_fields = ["id"]


class CareerFieldSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200, allow_blank=False, allow_null=False, required=True)
    organization = serializers.PrimaryKeyRelatedField(
        allow_null=False,
        required=True,
        queryset=Organization.objects.all(),
    )
    created = serializers.DateField(read_only=True)
    updated = serializers.DateField(read_only=True)

    class Meta:
        model = CareerField
        fields = [
            "id",
            "name",
            "organization",
            "created",
            "updated",
        ]
        read_only_fields = ["id"]


class EmploymentStateSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200, allow_blank=False, allow_null=False, required=True)
    organization = serializers.PrimaryKeyRelatedField(
        allow_null=False,
        required=True,
        queryset=Organization.objects.all(),
    )
    created = serializers.DateField(read_only=True)
    updated = serializers.DateField(read_only=True)

    class Meta:
        model = EmploymentState
        fields = [
            "id",
            "name",
            "organization",
            "created",
            "updated",
        ]
        read_only_fields = ["id"]


class ElectronicAnnouncementTitleSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200, allow_blank=False, allow_null=False, required=True)
    organization = serializers.PrimaryKeyRelatedField(
        allow_null=False,
        required=True,
        queryset=Organization.objects.all(),
    )
    created = serializers.DateField(read_only=True)
    updated = serializers.DateField(read_only=True)

    class Meta:
        model = ElectronicAnnouncementTitle
        fields = [
            "id",
            "name",
            "organization",
            "created",
            "updated",
        ]
        read_only_fields = ["id"]


class MilitaryStatusSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200, allow_blank=False, allow_null=False, required=True)
    organization = serializers.PrimaryKeyRelatedField(
        allow_null=False,
        required=True,
        queryset=Organization.objects.all(),
    )
    created = serializers.DateField(read_only=True)
    updated = serializers.DateField(read_only=True)

    class Meta:
        model = MilitaryStatus
        fields = [
            "id",
            "name",
            "organization",
            "created",
            "updated",
        ]
        read_only_fields = ["id"]


class CareerGroupSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200, allow_blank=False, allow_null=False, required=True)
    organization = serializers.PrimaryKeyRelatedField(
        allow_null=False,
        required=True,
        queryset=Organization.objects.all(),
    )
    created = serializers.DateField(read_only=True)
    updated = serializers.DateField(read_only=True)

    class Meta:
        model = CareerGroup
        fields = [
            "id",
            "name",
            "organization",
            "created",
            "updated",
        ]
        read_only_fields = ["id"]


class BloodTypeSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200, allow_blank=False, allow_null=False, required=True)
    organization = serializers.PrimaryKeyRelatedField(
        allow_null=False,
        required=True,
        queryset=Organization.objects.all(),
    )
    created = serializers.DateField(read_only=True)
    updated = serializers.DateField(read_only=True)

    class Meta:
        model = BloodType
        fields = [
            "id",
            "name",
            "organization",
            "created",
            "updated",
        ]
        read_only_fields = ["id"]


class DegreeComplianceSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200, allow_blank=False, allow_null=False, required=True)
    organization = serializers.PrimaryKeyRelatedField(
        allow_null=False,
        required=True,
        queryset=Organization.objects.all(),
    )
    created = serializers.DateField(read_only=True)
    updated = serializers.DateField(read_only=True)

    class Meta:
        model = DegreeCompliance
        fields = [
            "id",
            "name",
            "organization",
            "created",
            "updated",
        ]
        read_only_fields = ["id"]


class JobLevelSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200, allow_blank=False, allow_null=False, required=True)
    organization = serializers.PrimaryKeyRelatedField(
        allow_null=False,
        required=True,
        queryset=Organization.objects.all(),
    )
    created = serializers.DateField(read_only=True)
    updated = serializers.DateField(read_only=True)

    class Meta:
        model = JobLevel
        fields = [
            "id",
            "name",
            "organization",
            "created",
            "updated",
        ]
        read_only_fields = ["id"]


class ReligionSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200, allow_blank=False, allow_null=False, required=True)
    organization = serializers.PrimaryKeyRelatedField(
        allow_null=False,
        required=True,
        queryset=Organization.objects.all(),
    )
    created = serializers.DateField(read_only=True)
    updated = serializers.DateField(read_only=True)

    class Meta:
        model = Religion
        fields = [
            "id",
            "name",
            "organization",
            "created",
            "updated",
        ]
        read_only_fields = ["id"]


class EmploymentTypeSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200, allow_blank=False, allow_null=False, required=True)
    organization = serializers.PrimaryKeyRelatedField(
        allow_null=False,
        required=True,
        queryset=Organization.objects.all(),
    )
    created = serializers.DateField(read_only=True)
    updated = serializers.DateField(read_only=True)

    class Meta:
        model = EmploymentType
        fields = [
            "id",
            "name",
            "organization",
            "created",
            "updated",
        ]
        read_only_fields = ["id"]


class EmploymentStatusSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200, allow_blank=False, allow_null=False, required=True)
    organization = serializers.PrimaryKeyRelatedField(
        allow_null=False,
        required=True,
        queryset=Organization.objects.all(),
    )
    created = serializers.DateField(read_only=True)
    updated = serializers.DateField(read_only=True)

    class Meta:
        model = EmploymentStatus
        fields = [
            "id",
            "name",
            "organization",
            "created",
            "updated",
        ]
        read_only_fields = ["id"]
