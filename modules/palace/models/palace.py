from django.db import models
from django.utils.translation import gettext_lazy as _

from mptt.models import MPTTModel, TreeManager, TreeForeignKey

from modules.common.models import ActivatedModelMixin, TimestampedModelMixin, OrganizationModelMixin


class PalaceKind(OrganizationModelMixin):
    name = models.CharField(max_length=250, verbose_name=_("name"))

    class Meta:
        db_table = "palace_kind"
        verbose_name = _("Palace Kind")
        verbose_name_plural = _("Palace Kinds")

    def __str__(self):
        return self.name


class PalaceAccountType(OrganizationModelMixin):
    name = models.CharField(max_length=250, verbose_name=_("name"))

    class Meta:
        db_table = "palace_account_type"
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
    account_type = models.ForeignKey("PalaceAccountType", on_delete=models.CASCADE, related_name="%(class)ss")
    kind = models.ForeignKey(PalaceKind, on_delete=models.CASCADE, verbose_name=_("kind"), related_name="%(class)ss")
    is_private = models.BooleanField(default=True, verbose_name=_("is private"))
    upstream_organization_code = models.IntegerField(blank=True, null=True)
    land_area = models.IntegerField(verbose_name=_("land area"), null=True)
    noble_area = models.IntegerField(verbose_name=_("area of noble"), null=True)
    distance_to_province = models.IntegerField(blank=True, null=True)
    distance_to_same_palace = models.IntegerField(blank=True, null=True)
    operation_date = models.DateField(verbose_name=_("operation date"))
    completion_certificate = models.ImageField(upload_to="palace/completion_certificate")
    completion_date = models.DateField(verbose_name=_("completion date"))
    ownership_code = models.IntegerField(blank=True, null=True)
    operation_license = models.ImageField(
        upload_to="palace/operation_license",
        verbose_name=_("operation license"),
    )
    phone = models.CharField(max_length=15, verbose_name=_("phone"))
    email = models.EmailField(verbose_name=_("palace email"))
    website = models.URLField(max_length=300, verbose_name=_("website"), blank=True)
    postal_code = models.CharField(max_length=15, verbose_name=_("postal code"))
    description = models.TextField(blank=True, null=True)

    objects = models.Manager()
    tree_manager = TreeManager()

    class Meta:
        db_table = "palace"
        verbose_name = _("Palace")
        verbose_name_plural = _("Palaces")

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name
