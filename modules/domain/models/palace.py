from django.db import models
from django.utils.translation import gettext_lazy as _

from mptt.models import MPTTModel, TreeManager, TreeForeignKey

from modules.common.models import PalaceModelMixin, ActivatedModelMixin, TimestampedModelMixin, OrganizationModelMixin


class PalaceStatus(OrganizationModelMixin, TimestampedModelMixin, ActivatedModelMixin):
    name = models.CharField(max_length=150, verbose_name=_("name"))

    class Meta:
        db_table = "samam_palace_status"
        verbose_name = _("Palace Status")
        verbose_name_plural = _("Palace Statuses")

    def __str__(self):
        return self.name


class PalaceOwnershipType(OrganizationModelMixin, TimestampedModelMixin):
    name = models.CharField(max_length=150, verbose_name=_("name"))

    class Meta:
        db_table = "samam_palace_ownership_type"
        verbose_name = _("Palace Ownership type")
        verbose_name_plural = _("Palace Ownership Types")

    def __str__(self):
        return self.name


class PalaceLevel(OrganizationModelMixin, TimestampedModelMixin):
    name = models.CharField(max_length=100, verbose_name=_("name"))
    is_headquarters_unit = models.BooleanField(default=False)
    is_provincial_unit = models.BooleanField(default=False)
    is_executive_unit = models.BooleanField(default=False)
    is_provider = models.BooleanField(default=False)  # Supplier of goods and services
    is_top_notch_organization = models.BooleanField(default=False)

    class Meta:
        db_table = "samam_palace_level"
        verbose_name = _("Palace Level")
        verbose_name_plural = _("Palace Levels")

    def __str__(self):
        return self.name


class PalaceKind(OrganizationModelMixin, TimestampedModelMixin):
    name = models.CharField(max_length=250, verbose_name=_("name"))

    class Meta:
        db_table = "samam_palace_kind"
        verbose_name = _("Palace Kind")
        verbose_name_plural = _("Palace Kinds")

    def __str__(self):
        return self.name


class PalaceAccountType(OrganizationModelMixin, TimestampedModelMixin):
    name = models.CharField(max_length=150, verbose_name=_("name"))

    class Meta:
        db_table = "samam_palace_account_type"
        verbose_name = _("Palace Account Type")
        verbose_name_plural = _("Palace Account Types")

    def __str__(self):
        return self.name


class Palace(OrganizationModelMixin, TimestampedModelMixin, ActivatedModelMixin, MPTTModel):
    banner = models.ImageField(upload_to="palace/banner", blank=True)
    logo = models.ImageField(upload_to="palace/logo", blank=True)
    name = models.CharField(max_length=255, verbose_name=_("name"))
    address = models.CharField(max_length=255, verbose_name=_("address"))
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="children",
        verbose_name=_("parent"),
    )
    city = models.ForeignKey("City", on_delete=models.CASCADE, verbose_name=_("city"), related_name="%(class)ss")
    account_type = models.ForeignKey(PalaceAccountType, on_delete=models.CASCADE, related_name="%(class)ss")
    kind = models.ForeignKey(PalaceKind, on_delete=models.CASCADE, verbose_name=_("kind"), related_name="%(class)ss")
    is_private = models.BooleanField(default=True, verbose_name=_("is private"))
    land_area = models.IntegerField(verbose_name=_("land area"), null=True)
    noble_area = models.IntegerField(verbose_name=_("area of noble"), null=True)
    distance_to_province = models.IntegerField(blank=True, null=True)
    distance_to_same_palace = models.IntegerField(blank=True, null=True)
    operation_date = models.DateField(verbose_name=_("operation date"))
    completion_certificate = models.ImageField(upload_to="palace/completion_certificate", blank=True)
    completion_date = models.DateField(verbose_name=_("completion date"), blank=True)
    ownership_type = models.ForeignKey(
        PalaceOwnershipType,
        verbose_name=_("ownership type"),
        on_delete=models.CASCADE,
        related_name="%(class)ss",
    )
    operation_license = models.ImageField(
        upload_to="palace/operation_license",
        verbose_name=_("operation license"),
        blank=True,
    )
    status = models.ForeignKey(PalaceStatus, verbose_name=_("palace status"), on_delete=models.CASCADE, related_name="%(class)ss")
    palace_level = models.ForeignKey(PalaceLevel, on_delete=models.CASCADE, related_name="%(class)ss")
    phone = models.CharField(max_length=15, verbose_name=_("phone"))
    email = models.EmailField(verbose_name=_("palace email"))
    website = models.URLField(max_length=300, verbose_name=_("website"), blank=True)
    postal_code = models.CharField(max_length=15, verbose_name=_("postal code"))
    description = models.TextField(blank=True, null=True)

    objects = models.Manager()
    tree_manager = TreeManager()

    class Meta:
        db_table = "samam_palace"
        verbose_name = _("Palace")
        verbose_name_plural = _("Palaces")

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


class PalaceStatusHistory(OrganizationModelMixin, PalaceModelMixin):
    status = models.ForeignKey(
        PalaceStatus,
        verbose_name=_("palace status history"),
        on_delete=models.CASCADE,
        related_name="%(class)ss",
    )
    start = models.DateTimeField(verbose_name=_("start at"), auto_now_add=True)
    end = models.DateTimeField(verbose_name=_("end at"), auto_now_add=False)

    class Meta:
        db_table = "samam_palace_status_history"
