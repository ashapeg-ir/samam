from rest_framework.routers import SimpleRouter

from modules.palace.api.rest.v1.views import PalaceViewSet

router = SimpleRouter()
router.register("", PalaceViewSet, basename="palace")
urlpatterns = router.urls
