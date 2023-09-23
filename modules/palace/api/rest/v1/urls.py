from rest_framework.routers import SimpleRouter

from modules.palace.api.rest.v1.views import (
    PalaceViewSet,
    PalaceKindViewSet,
    PalaceLevelViewSet,
    PalaceStatusViewSet,
    PalaceAccountTypeViewSet,
    PalaceOwnershipTypeViewSet,
)

router = SimpleRouter()
router.register("palace-kind", PalaceKindViewSet, basename="palace-kind")
router.register("palace-account-type", PalaceAccountTypeViewSet, basename="palace-account-type")
router.register("palace-level", PalaceLevelViewSet, basename="palace-level")
router.register("palace-ownership-type", PalaceOwnershipTypeViewSet, basename="palace-ownership-type")
router.register("palace-status", PalaceStatusViewSet, basename="palace-status")
router.register("", PalaceViewSet, basename="palace")

urlpatterns = router.urls
