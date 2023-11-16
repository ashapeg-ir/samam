from django.contrib import admin

from modules.domain.models import (
    City,
    Grade,
    Place,
    Gender,
    Palace,
    Country,
    JobLevel,
    Province,
    Relation,
    Religion,
    BloodType,
    Department,
    Occupation,
    PalaceKind,
    PalaceSupervisor,
    CareerField,
    CareerGroup,
    PalaceLevel,
    FieldOfStudy,
    Organization,
    PalaceStatus,
    MaritalStatus,
    MilitaryStatus,
    EmploymentState,
    LanguageCaption,
    DegreeCompliance,
    DepartmentStatus,
    PlaceAccountType,
    TeamDistribution,
    OrganizationGraph,
    PalaceAccountType,
    PalaceOwnershipType,
    OrganizationNickname,
    DepartmentOwnershipType,
    ElectronicAnnouncementTitle,
)


@admin.register(TeamDistribution)
class TeamDistributionAdmin(admin.ModelAdmin):
    list_display = ["department", "organization", "created", "updated"]


@admin.register(CareerGroup)
class CareerGroupAdmin(admin.ModelAdmin):
    list_display = ["name", "organization", "created", "updated"]


@admin.register(OrganizationNickname)
class OrganizationNicknameAdmin(admin.ModelAdmin):
    list_display = ["name", "organization", "created", "updated"]


@admin.register(DegreeCompliance)
class DegreeComplianceAdmin(admin.ModelAdmin):
    list_display = ["name", "organization", "created", "updated"]


@admin.register(FieldOfStudy)
class FieldOfStudyAdmin(admin.ModelAdmin):
    list_display = ["name", "organization", "created", "updated"]


@admin.register(JobLevel)
class JobLevelAdmin(admin.ModelAdmin):
    list_display = ["name", "organization", "created", "updated"]


@admin.register(OrganizationGraph)
class OrganizationGraphAdmin(admin.ModelAdmin):
    list_display = ["row_name", "row_full_name", "organization", "created", "updated"]


@admin.register(Religion)
class ReligionAdmin(admin.ModelAdmin):
    list_display = ["name", "organization", "created", "updated"]


@admin.register(Relation)
class RelationAdmin(admin.ModelAdmin):
    list_display = ["name", "organization", "created", "updated"]


@admin.register(MaritalStatus)
class MaritalStatusAdmin(admin.ModelAdmin):
    list_display = ["name", "organization", "created", "updated"]


@admin.register(MilitaryStatus)
class MilitaryStatusAdmin(admin.ModelAdmin):
    list_display = ["name", "organization", "created", "updated"]


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ["name", "organization", "created", "updated"]


@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    list_display = ["name", "organization", "created", "updated"]


@admin.register(BloodType)
class BloodTypeAdmin(admin.ModelAdmin):
    list_display = ["name", "organization", "created", "updated"]


@admin.register(Occupation)
class OccupationAdmin(admin.ModelAdmin):
    list_display = ["name", "organization", "created", "updated"]


@admin.register(CareerField)
class CareerFieldAdmin(admin.ModelAdmin):
    list_display = ["name", "organization", "created", "updated"]


@admin.register(EmploymentState)
class EmploymentStateAdmin(admin.ModelAdmin):
    list_display = ["name", "organization", "created", "updated"]


@admin.register(ElectronicAnnouncementTitle)
class ElectronicAnnouncementTitleAdmin(admin.ModelAdmin):
    list_display = ["name", "organization", "created", "updated"]


@admin.register(DepartmentOwnershipType)
class DepartmentOwnershipTypeAdmin(admin.ModelAdmin):
    list_display = ["name", "organization", "created", "updated"]


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["place", "palace", "created", "updated"]


@admin.register(DepartmentStatus)
class DepartmentStatusAdmin(admin.ModelAdmin):
    list_display = ["name", "organization", "created", "updated"]


@admin.register(PalaceOwnershipType)
class PalaceOwnershipTypeAdmin(admin.ModelAdmin):
    list_display = ["name", "organization", "created", "updated"]


@admin.register(PalaceAccountType)
class PalaceAccountTypeAdmin(admin.ModelAdmin):
    list_display = ["name", "organization", "created", "updated"]


@admin.register(PalaceStatus)
class PalaceStatusAdmin(admin.ModelAdmin):
    list_display = ["name", "organization", "created", "updated"]


@admin.register(PalaceLevel)
class PalaceLevelAdmin(admin.ModelAdmin):
    list_display = ["name", "organization", "created", "updated"]


@admin.register(PalaceKind)
class PalaceKindAdmin(admin.ModelAdmin):
    list_display = ["name", "organization", "created", "updated"]


@admin.register(Palace)
class PalaceAdmin(admin.ModelAdmin):
    list_display = ["name", "organization", "created", "updated"]


@admin.register(PlaceAccountType)
class PlaceAccountTypeAdmin(admin.ModelAdmin):
    list_display = ["name", "organization", "created", "updated"]


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ["name", "customer", "language"]


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "organization", "palace", "is_workplace",
        "is_equipment_location",
        "is_committee",
        "is_team",
        "is_management_leadership",
    ]


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ["name", "organization"]


@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    list_display = ["name", "organization", "country"]


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ["name", "organization", "province"]


@admin.register(LanguageCaption)
class LanguageCaptionAdmin(admin.ModelAdmin):
    list_display = ["title", "is_editable", "language", "code", "organization"]


@admin.register(PalaceSupervisor)
class SupervisorAdmin(admin.ModelAdmin):
    list_display = ["organization", "user", "palace", "is_active", "created", "updated"]
