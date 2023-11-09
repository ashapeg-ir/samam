from rest_framework.routers import SimpleRouter

from modules.organization.api.rest.v1.position.views import PositionViewSet

router = SimpleRouter()
router.register("", PositionViewSet, basename="position")
urlpatterns = router.urls
