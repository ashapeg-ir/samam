from django.contrib import admin

from mptt.admin import MPTTModelAdmin

from modules.domain.models import (
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
