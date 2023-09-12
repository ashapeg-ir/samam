from rest_framework.routers import SimpleRouter

from modules.hrm.api.rest.v1.views import CustomerLoginViewSet, UserLoginViewSet

router = SimpleRouter()
router.register('customer/login', CustomerLoginViewSet, basename='auth-customer')
router.register('user', UserLoginViewSet, basename='auth-user')
urlpatterns = router.urls
