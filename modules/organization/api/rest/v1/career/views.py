from rest_framework import exceptions
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from modules.domain.models import (
    Grade,
    Gender,
    JobLevel,
    Relation,
    Religion,
    BloodType,
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
from modules.common.permissions import CustomerPermission

from .serializer import (
    GradeSerializer,
    GenderSerializer,
    JobLevelSerializer,
    RelationSerializer,
    ReligionSerializer,
    BloodTypeSerializer,
    OccupationSerializer,
    CareerFieldSerializer,
    CareerGroupSerializer,
    FieldOfStudySerializer,
    MaritalStatusSerializer,
    EmploymentTypeSerializer,
    MilitaryStatusSerializer,
    EmploymentStateSerializer,
    DegreeComplianceSerializer,
    EmploymentStatusSerializer,
    OrganizationGraphSerializer,
    OrganizationLevelSerializer,
    OrganizationNicknameSerializer,
    ElectronicAnnouncementTitleSerializer,
)


class GenderViewSet(GenericViewSet, CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin):
    queryset = Gender.objects.none()
    serializer_class = GenderSerializer
    permission_classes = [CustomerPermission]

    def get_queryset(self):
        return Gender.objects.filter(organization__customer_id=self.request.user)

    def perform_create(self, serializer):
        if Organization.objects.get(customer_id=self.request.user) != serializer.validated_data["organization"]:
            raise exceptions.PermissionDenied
        super().perform_create(serializer)


class OrganizationLevelViewSet(GenericViewSet, CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin):
    queryset = OrganizationLevel.objects.none()
    serializer_class = OrganizationLevelSerializer
    permission_classes = [CustomerPermission]

    def get_queryset(self):
        return OrganizationLevel.objects.filter(organization__customer_id=self.request.user)

    def perform_create(self, serializer):
        if Organization.objects.get(customer_id=self.request.user) != serializer.validated_data["organization"]:
            raise exceptions.PermissionDenied
        super().perform_create(serializer)


class OrganizationNicknameViewSet(GenericViewSet, CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin):
    queryset = OrganizationNickname.objects.none()
    serializer_class = OrganizationNicknameSerializer
    permission_classes = [CustomerPermission]

    def get_queryset(self):
        return OrganizationNickname.objects.filter(organization__customer_id=self.request.user)

    def perform_create(self, serializer):
        if Organization.objects.get(customer_id=self.request.user) != serializer.validated_data["organization"]:
            raise exceptions.PermissionDenied
        super().perform_create(serializer)


class OrganizationGraphViewSet(GenericViewSet, CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin):
    queryset = OrganizationGraph.objects.none()
    serializer_class = OrganizationGraphSerializer
    permission_classes = [CustomerPermission]

    def get_queryset(self):
        return OrganizationGraph.objects.filter(organization__customer_id=self.request.user)

    def perform_create(self, serializer):
        if Organization.objects.get(customer_id=self.request.user) != serializer.validated_data["organization"]:
            raise exceptions.PermissionDenied
        super().perform_create(serializer)


class JobLevelViewSet(GenericViewSet, CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin):
    queryset = JobLevel.objects.none()
    serializer_class = JobLevelSerializer
    permission_classes = [CustomerPermission]

    def get_queryset(self):
        return JobLevel.objects.filter(organization__customer_id=self.request.user)

    def perform_create(self, serializer):
        if Organization.objects.get(customer_id=self.request.user) != serializer.validated_data["organization"]:
            raise exceptions.PermissionDenied
        super().perform_create(serializer)


class GradeSerializerViewSet(GenericViewSet, CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin):
    queryset = Grade.objects.none()
    serializer_class = GradeSerializer
    permission_classes = [CustomerPermission]

    def get_queryset(self):
        return Grade.objects.filter(organization__customer_id=self.request.user)

    def perform_create(self, serializer):
        if Organization.objects.get(customer_id=self.request.user) != serializer.validated_data["organization"]:
            raise exceptions.PermissionDenied
        super().perform_create(serializer)


class RelationViewSet(GenericViewSet, CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin):
    queryset = Relation.objects.none()
    serializer_class = RelationSerializer
    permission_classes = [CustomerPermission]

    def get_queryset(self):
        return Relation.objects.filter(organization__customer_id=self.request.user)

    def perform_create(self, serializer):
        if Organization.objects.get(customer_id=self.request.user) != serializer.validated_data["organization"]:
            raise exceptions.PermissionDenied
        super().perform_create(serializer)


class ReligionViewSet(GenericViewSet, CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin):
    queryset = Religion.objects.none()
    serializer_class = ReligionSerializer
    permission_classes = [CustomerPermission]

    def get_queryset(self):
        return Religion.objects.filter(organization__customer_id=self.request.user)

    def perform_create(self, serializer):
        if Organization.objects.get(customer_id=self.request.user) != serializer.validated_data["organization"]:
            raise exceptions.PermissionDenied
        super().perform_create(serializer)


class BloodTypeViewSet(GenericViewSet, CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin):
    queryset = BloodType.objects.none()
    serializer_class = BloodTypeSerializer
    permission_classes = [CustomerPermission]

    def get_queryset(self):
        return BloodType.objects.filter(organization__customer_id=self.request.user)

    def perform_create(self, serializer):
        if Organization.objects.get(customer_id=self.request.user) != serializer.validated_data["organization"]:
            raise exceptions.PermissionDenied
        super().perform_create(serializer)


class OccupationViewSet(GenericViewSet, CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin):
    queryset = Occupation.objects.none()
    serializer_class = OccupationSerializer
    permission_classes = [CustomerPermission]

    def get_queryset(self):
        return Occupation.objects.filter(organization__customer_id=self.request.user)

    def perform_create(self, serializer):
        if Organization.objects.get(customer_id=self.request.user) != serializer.validated_data["organization"]:
            raise exceptions.PermissionDenied
        super().perform_create(serializer)


class CareerFieldViewSet(GenericViewSet, CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin):
    queryset = CareerField.objects.none()
    serializer_class = CareerFieldSerializer
    permission_classes = [CustomerPermission]

    def get_queryset(self):
        return CareerField.objects.filter(organization__customer_id=self.request.user)

    def perform_create(self, serializer):
        if Organization.objects.get(customer_id=self.request.user) != serializer.validated_data["organization"]:
            raise exceptions.PermissionDenied
        super().perform_create(serializer)


class CareerGroupViewSet(GenericViewSet, CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin):
    queryset = CareerGroup.objects.none()
    serializer_class = CareerGroupSerializer
    permission_classes = [CustomerPermission]

    def get_queryset(self):
        return CareerGroup.objects.filter(organization__customer_id=self.request.user)

    def perform_create(self, serializer):
        if Organization.objects.get(customer_id=self.request.user) != serializer.validated_data["organization"]:
            raise exceptions.PermissionDenied
        super().perform_create(serializer)


class ElectronicAnnouncementTitleViewSet(GenericViewSet, CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin):
    queryset = ElectronicAnnouncementTitle.objects.none()
    serializer_class = ElectronicAnnouncementTitleSerializer
    permission_classes = [CustomerPermission]

    def get_queryset(self):
        return ElectronicAnnouncementTitle.objects.filter(organization__customer_id=self.request.user)

    def perform_create(self, serializer):
        if Organization.objects.get(customer_id=self.request.user) != serializer.validated_data["organization"]:
            raise exceptions.PermissionDenied
        super().perform_create(serializer)


class FieldOfStudyViewSet(GenericViewSet, CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin):
    queryset = FieldOfStudy.objects.none()
    serializer_class = FieldOfStudySerializer
    permission_classes = [CustomerPermission]

    def get_queryset(self):
        return FieldOfStudy.objects.filter(organization__customer_id=self.request.user)

    def perform_create(self, serializer):
        if Organization.objects.get(customer_id=self.request.user) != serializer.validated_data["organization"]:
            raise exceptions.PermissionDenied
        super().perform_create(serializer)


class MilitaryStatusViewSet(GenericViewSet, CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin):
    queryset = MilitaryStatus.objects.none()
    serializer_class = MilitaryStatusSerializer
    permission_classes = [CustomerPermission]

    def get_queryset(self):
        return MilitaryStatus.objects.filter(organization__customer_id=self.request.user)

    def perform_create(self, serializer):
        if Organization.objects.get(customer_id=self.request.user) != serializer.validated_data["organization"]:
            raise exceptions.PermissionDenied
        super().perform_create(serializer)


class MaritalStatusViewSet(GenericViewSet, CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin):
    queryset = MaritalStatus.objects.none()
    serializer_class = MaritalStatusSerializer
    permission_classes = [CustomerPermission]

    def get_queryset(self):
        return MaritalStatus.objects.filter(organization__customer_id=self.request.user)

    def perform_create(self, serializer):
        if Organization.objects.get(customer_id=self.request.user) != serializer.validated_data["organization"]:
            raise exceptions.PermissionDenied
        super().perform_create(serializer)


class EmploymentTypeViewSet(GenericViewSet, CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin):
    queryset = EmploymentType.objects.none()
    serializer_class = EmploymentTypeSerializer
    permission_classes = [CustomerPermission]

    def get_queryset(self):
        return EmploymentType.objects.filter(organization__customer_id=self.request.user)

    def perform_create(self, serializer):
        if Organization.objects.get(customer_id=self.request.user) != serializer.validated_data["organization"]:
            raise exceptions.PermissionDenied
        super().perform_create(serializer)


class EmploymentStateViewSet(GenericViewSet, CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin):
    queryset = EmploymentState.objects.none()
    serializer_class = EmploymentStateSerializer
    permission_classes = [CustomerPermission]

    def get_queryset(self):
        return EmploymentState.objects.filter(organization__customer_id=self.request.user)

    def perform_create(self, serializer):
        if Organization.objects.get(customer_id=self.request.user) != serializer.validated_data["organization"]:
            raise exceptions.PermissionDenied
        super().perform_create(serializer)


class DegreeComplianceViewSet(GenericViewSet, CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin):
    queryset = DegreeCompliance.objects.none()
    serializer_class = DegreeComplianceSerializer
    permission_classes = [CustomerPermission]

    def get_queryset(self):
        return DegreeCompliance.objects.filter(organization__customer_id=self.request.user)

    def perform_create(self, serializer):
        if Organization.objects.get(customer_id=self.request.user) != serializer.validated_data["organization"]:
            raise exceptions.PermissionDenied
        super().perform_create(serializer)


class EmploymentStatusViewSet(GenericViewSet, CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin):
    queryset = EmploymentStatus.objects.none()
    serializer_class = EmploymentStatusSerializer
    permission_classes = [CustomerPermission]

    def get_queryset(self):
        return EmploymentStatus.objects.filter(organization__customer_id=self.request.user)

    def perform_create(self, serializer):
        if Organization.objects.get(customer_id=self.request.user) != serializer.validated_data["organization"]:
            raise exceptions.PermissionDenied
        super().perform_create(serializer)
