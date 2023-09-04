from django.contrib import admin

from mptt.admin import DraggableMPTTAdmin

# Register your models here.
from modules.palace.models import City, Country, Language, Province, Department, Palace, LanguageCaption


@admin.register(Palace)
class PalaceAdmin(DraggableMPTTAdmin):
    list_display = ("tree_actions", "indented_title", "status", "city")
    list_filter = ["status", "city__province"]

    expand_tree_by_default = True


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'Palace']
    list_display_links = ['name']
    search_fields = ['name']


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ["name", "province", "is_active"]
    list_filter = ["province", "is_active"]


@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    list_display = ["name", "country", "is_active"]
    list_filter = ["country", "is_active"]


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ["title", "code"]
    list_filter = ["code"]


@admin.register(LanguageCaption)
class LanguageCaptionAdmin(admin.ModelAdmin):
    list_display = ["title", "language", "Palace"]
    list_filter = ["language", "code", "Palace"]
