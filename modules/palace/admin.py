from django.contrib import admin

from mptt.admin import MPTTModelAdmin

from modules.palace.models import (
    City,
    Place,
    Palace,
    Country,
    Province,
    Department,
    PalaceKind,
    Organization,
    LanguageCaption,
    PalaceAccountType,
)


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    pass


@admin.register(PalaceKind)
class PalaceTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(PalaceAccountType)
class PalaceAccountTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Palace)
class PalacesAdmin(MPTTModelAdmin):
    pass


@admin.register(Department)
class DepartmentAdmin(MPTTModelAdmin):
    pass


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    pass


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass


@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    pass


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass


@admin.register(LanguageCaption)
class LanguageCaptionAdmin(admin.ModelAdmin):
    pass
