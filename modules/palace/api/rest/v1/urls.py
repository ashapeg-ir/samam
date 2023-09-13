from rest_framework.routers import SimpleRouter

from modules.palace.api.rest.v1.views import PalaceViewSet, PalaceKindViewSet, PalaceAccountTypeViewSet

router = SimpleRouter()
router.register("palace-kind", PalaceKindViewSet, basename="palace-kind")
router.register("palace-account-type", PalaceAccountTypeViewSet, basename="palace-account-type")
router.register("", PalaceViewSet, basename="palace")

urlpatterns = router.urls
