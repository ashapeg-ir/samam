from rest_framework.routers import SimpleRouter

from modules.hrm.api.rest.v1.views import SupervisorLoginViewSet

router = SimpleRouter()
router.register('supervisor', SupervisorLoginViewSet, basename='auth-supervisor')

urlpatterns = router.urls
