from rest_framework.routers import SimpleRouter

from modules.organization.api.rest.v1.views import PlaceViewSet, OrganizationViewSet

router = SimpleRouter()
router.register("", OrganizationViewSet, basename="org")
router.register("place", PlaceViewSet, basename="place")
urlpatterns = router.urls
