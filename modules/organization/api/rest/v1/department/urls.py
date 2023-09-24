from rest_framework.routers import SimpleRouter

from modules.organization.api.rest.v1.department.views import DepartmentViewSet, TeamDistributionViewSet

router = SimpleRouter()
router.register("team-distribution", TeamDistributionViewSet, basename="team-distribution")
router.register("", DepartmentViewSet, basename="department")

urlpatterns = router.urls
