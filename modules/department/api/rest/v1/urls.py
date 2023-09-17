from rest_framework.routers import SimpleRouter

from modules.department.api.rest.v1.views import DepartmentViewSet

router = SimpleRouter()
router.register("", DepartmentViewSet, basename="department")

urlpatterns = router.urls
