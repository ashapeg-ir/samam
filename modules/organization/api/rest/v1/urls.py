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

router.register("places", PlaceViewSet, basename="place")
router.register("place-account-types", PlaceAccountTypeViewSet, basename="place-account-type")
router.register("countries", CountryViewSet, basename="country")
router.register("provinces", ProvinceViewSet, basename="province")
router.register("cities", CityViewSet, basename="city")
router.register("", OrganizationViewSet, basename="org")
urlpatterns = [
    path("palaces/", include("modules.organization.api.rest.v1.palace.urls")),
    path("departments/", include("modules.organization.api.rest.v1.department.urls")),
    path("career/", include("modules.organization.api.rest.v1.career.urls")),
    path("users/", include("modules.organization.api.rest.v1.users.urls")),
    path("positions/", include("modules.organization.api.rest.v1.position.urls")),
]
urlpatterns += router.urls
