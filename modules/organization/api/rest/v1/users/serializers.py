from rest_framework import serializers
from modules.domain.models import (
    User,
    Profile,
    Organization,
    Gender,
    Grade,
    ResidentialArea,
    BloodType,
    MaritalStatus,
    MilitaryStatus,
    Religion,
    Occupation,
    DegreeCompliance,
    FieldOfStudy,
    OrganizationNickname,
)


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "username"]


class UserCreateSerializer(serializers.Serializer):
    organization = serializers.PrimaryKeyRelatedField(
        allow_null=False,
        required=True,
        queryset=Organization.objects.all(),
    )
    gender = serializers.PrimaryKeyRelatedField(
        allow_null=False,
        required=True,
        queryset=Gender.objects.all(),
    )
    city = serializers.PrimaryKeyRelatedField(
        allow_null=False,
        required=True,
        queryset=Organization.objects.all(),
    )
    grade = serializers.PrimaryKeyRelatedField(
        allow_null=False,
        required=True,
        queryset=Grade.objects.all(),
    )
    region = serializers.PrimaryKeyRelatedField(
        allow_null=False,
        required=True,
        queryset=ResidentialArea.objects.all(),
    )
    blood_type = serializers.PrimaryKeyRelatedField(
        allow_null=False,
        required=True,
        queryset=BloodType.objects.all(),
    )
    marital_status = serializers.PrimaryKeyRelatedField(
        allow_null=False,
        required=True,
        queryset=MaritalStatus.objects.all(),
    )
    military_status = serializers.PrimaryKeyRelatedField(
        allow_null=False,
        required=True,
        queryset=MilitaryStatus.objects.all(),
    )
    Organization_nickname = serializers.PrimaryKeyRelatedField(
        allow_null=False,
        required=True,
        queryset=OrganizationNickname.objects.all(),
    )
    field_of_study = serializers.PrimaryKeyRelatedField(
        allow_null=False,
        required=True,
        queryset=FieldOfStudy.objects.all(),
    )
    degree_compliance = serializers.PrimaryKeyRelatedField(
        allow_null=False,
        required=True,
        queryset=DegreeCompliance.objects.all(),
    )
    religion = serializers.PrimaryKeyRelatedField(
        allow_null=False,
        required=True,
        queryset=Religion.objects.all(),
    )
    picture = serializers.FileField()
    phone = serializers.CharField(max_length=150, allow_null=False, allow_blank=False, required=True)
    birthdate = serializers.DateField(required=True)
    identification_id = serializers.CharField(max_length=10, allow_null=False, allow_blank=False, required=True)
    essential_phone = serializers.CharField(max_length=15, allow_null=False, allow_blank=False, required=True)
    national_id = serializers.CharField(max_length=10, allow_null=False, allow_blank=False, required=True)
    personnel_code = serializers.CharField(max_length=150, allow_null=False, allow_blank=False, required=True)
    username = serializers.CharField(max_length=150, allow_null=False, allow_blank=False, required=True)
    password = serializers.CharField(max_length=150, allow_null=False, allow_blank=False, required=True)
    first_name = serializers.CharField(max_length=150, allow_null=False, allow_blank=False, required=True)
    last_name = serializers.CharField(max_length=150, allow_null=False, allow_blank=False, required=True)
    email = serializers.EmailField(max_length=150, allow_null=False, allow_blank=False, required=True)
    is_active = serializers.BooleanField(default=True)

    def validate(self, attrs):
        # detect unknown fields and raise exception
        unknown_fields = set(attrs) - set(self.fields)
        if unknown_fields:
            raise serializers.ValidationError(f"Unknown fields: {', '.join(unknown_fields)}")

        # validate username uniqueness
        if User.objects.filter(username=attrs["username"]).exists():
            raise serializers.ValidationError("Username already exists")

        # validate email uniqueness
        if User.objects.filter(email=attrs["email"]).exists():
            raise serializers.ValidationError("Email already exists")

        # validate phone uniqueness
        if User.objects.filter(phone=attrs["phone"]).exists():
            raise serializers.ValidationError("Phone already exists")

        # validate personnel_code uniqueness
        if User.objects.filter(personnel_code=attrs["personnel_code"]).exists():
            raise serializers.ValidationError("Personnel code already exists")

        # validate national_id uniqueness
        if User.objects.filter(national_id=attrs["national_id"]).exists():
            raise serializers.ValidationError("National id already exists")

        return attrs

    def create(self, validated_data):
        user = User(
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            email=validated_data["email"],
            is_active=validated_data["is_active"],
        )
        user.set_password(validated_data["password"])
        user.save()
        profile = Profile.objects.create(
            user=user,
            gender_id=validated_data["gender"],
            organization_id=validated_data["organization"],
            city_id=validated_data["city"],
            grade_id=validated_data["grade"],
            region_id=validated_data["region"],
            blood_type_id=validated_data["blood_type"],
            marital_status_id=validated_data["marital_status"],
            military_status_id=validated_data["military_status"],
            organization_nickname_id=validated_data["Organization_nickname"],
            field_of_study_id=validated_data["field_of_study"],
            degree_compliance_id=validated_data["degree_compliance"],
            religion_id=validated_data["cyber"],
            picture=validated_data["picture"],
            phone_number=validated_data["phone_number"],
            birthdate=validated_data["birthdate"],
            identification_id=validated_data["identification_id"],
            essential_phone=validated_data["essential_phone"],
            national_id=validated_data["national_id"],
            personnel_code=validated_data["personnel_code"],
        )

        return profile


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "is_active"]
