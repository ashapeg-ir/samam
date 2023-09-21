from django.contrib import admin

from modules.domain.models import City, Place, Country, Province, Organization, LanguageCaption, PlaceAccountType


@admin.register(PlaceAccountType)
class PlaceAccountTypeAdmin(admin.ModelAdmin):
    list_display = ["name", "organization", "created", "updated"]


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ["name", "customer", "language"]


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "organization", "palace", "is_workplace",
        "is_equipment_location",
        "is_committee",
        "is_team",
        "is_management_leadership",
    ]


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ["name", "organization"]


@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    list_display = ["name", "organization", "country"]


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ["name", "organization", "province"]


@admin.register(LanguageCaption)
class LanguageCaptionAdmin(admin.ModelAdmin):
    list_display = ["title", "is_editable", "language", "code", "organization"]
