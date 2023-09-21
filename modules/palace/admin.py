from django.contrib import admin

from mptt.admin import MPTTModelAdmin

from modules.domain.models import (
    Palace,
    Department,
    PalaceKind,
    PalaceAccountType,
    PalaceStatus,
    PalaceLevel,
    PalaceOwnershipType,
)


@admin.register(PalaceOwnershipType)
class PalaceOwnershipTypeAdmin(admin.ModelAdmin):
    list_display = ["name", "organization"]


@admin.register(PalaceLevel)
class PalaceLevelAdmin(admin.ModelAdmin):
    list_display = ["name", "organization"]


@admin.register(PalaceStatus)
class PalaceStatusAdmin(admin.ModelAdmin):
    list_display = ["name", "organization"]


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
