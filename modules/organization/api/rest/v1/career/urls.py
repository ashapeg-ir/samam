from rest_framework.routers import SimpleRouter

from .views import (
    GenderViewSet,
    OrganizationGraphViewSet,
    OrganizationLevelViewSet,
    OrganizationNicknameViewSet,
    JobLevelViewSet,
    GradeSerializerViewSet,
    RelationViewSet,
    ReligionViewSet,
    BloodTypeViewSet,
    OccupationViewSet,
    CareerFieldViewSet,
    CareerGroupViewSet,
    ElectronicAnnouncementTitleViewSet,
    FieldOfStudyViewSet,
    MilitaryStatusViewSet,
    MaritalStatusViewSet,
    EmploymentTypeViewSet,
    EmploymentStateViewSet,
    DegreeComplianceViewSet,
    EmploymentStatusViewSet,
)

router = SimpleRouter()
router.register("gender", GenderViewSet, basename="gender")
router.register("org-nickname", OrganizationNicknameViewSet, basename="org-nickname")
router.register("org-level", OrganizationLevelViewSet, basename="org-level")
router.register("org-graph", OrganizationGraphViewSet, basename="org-graph")
router.register("grade", GradeSerializerViewSet, basename="job-level")
router.register("job-level", JobLevelViewSet, basename="job-level")
router.register("relation", RelationViewSet, basename="job-level")
router.register("blood-type", BloodTypeViewSet, basename="job-level")
router.register("religion", ReligionViewSet, basename="job-level")
router.register("occupation", OccupationViewSet, basename="job-level")
router.register("career-field", CareerFieldViewSet, basename="job-level")
router.register("career-group", CareerGroupViewSet, basename="job-level")
router.register("electric-announcement", ElectronicAnnouncementTitleViewSet, basename="job-level")
router.register("field-of-study", FieldOfStudyViewSet, basename="job-level")
router.register("military-status", MilitaryStatusViewSet, basename="job-level")
router.register("marital-status", MaritalStatusViewSet, basename="job-level")
router.register("employment-type", EmploymentTypeViewSet, basename="job-level")
router.register("employment-state", EmploymentStateViewSet, basename="job-level")
router.register("degree-compliance", DegreeComplianceViewSet, basename="job-level")
router.register("employment-status", EmploymentStatusViewSet, basename="job-level")

urlpatterns = router.urls
