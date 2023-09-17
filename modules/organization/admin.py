from django.contrib import admin

from modules.domain.models import City, Place, Country, Province, Organization, LanguageCaption


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ["name", "customer"]


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ["name", "organization", "palace"]


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ["name", "organization"]


@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    list_display = ["name", "organization"]


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ["name", "organization"]


@admin.register(LanguageCaption)
class LanguageCaptionAdmin(admin.ModelAdmin):
    list_display = ["title", "language", "code", "organization", "is_editable"]
