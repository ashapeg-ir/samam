from django.urls import path, include

from rest_framework.routers import SimpleRouter

from modules.organization.api.rest.v1.views import (
    CityViewSet,
    PlaceViewSet,
    CountryViewSet,
    ProvinceViewSet,
    OrganizationViewSet,
    PlaceAccountTypeViewSet,
)

router = SimpleRouter()

router.register("place", PlaceViewSet, basename="place")
router.register("place-account-type", PlaceAccountTypeViewSet, basename="place-account-type")
router.register("country", CountryViewSet, basename="country")
router.register("province", ProvinceViewSet, basename="province")
router.register("city", CityViewSet, basename="city")
router.register("", OrganizationViewSet, basename="org")
urlpatterns = [
    path("palace/", include("modules.organization.api.rest.v1.palace.urls")),
    path("department/", include("modules.organization.api.rest.v1.department.urls")),
]
urlpatterns += router.urls
