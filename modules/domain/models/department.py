from django.db import models
from django.utils.translation import gettext_lazy as _

from mptt.models import MPTTModel, TreeManager, TreeForeignKey
from model_utils.models import SoftDeletableModel

from modules.common.models import PalaceModelMixin, ActivatedModelMixin, TimestampedModelMixin, OrganizationModelMixin


class Place(OrganizationModelMixin, PalaceModelMixin):
    name = models.CharField(max_length=250, verbose_name=_("name"))

    class Meta:
        db_table = "samam_place"
        verbose_name = _("Place")
        verbose_name_plural = _("Place")

    def __str__(self):
        return self.name


class Department(PalaceModelMixin, OrganizationModelMixin, TimestampedModelMixin, ActivatedModelMixin, SoftDeletableModel, MPTTModel):
    place = models.ForeignKey("Place", on_delete=models.CASCADE, verbose_name=_("place"), related_name="%(class)ss")
    description = models.TextField(blank=True, null=True, verbose_name=_("description"))
    is_private = models.BooleanField(default=False, verbose_name=_("is private"))
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
        verbose_name=_("parent"),
    )

    email = models.EmailField(verbose_name=_("email"))
    land_area = models.IntegerField(verbose_name=_("land area"))
    noble_area = models.IntegerField(verbose_name=_("area of noble"))
    operation_date = models.DateField(verbose_name=_("operation date"))
    completion_date = models.DateField(verbose_name=_("completion date"))
    completion_certificate = models.ImageField(upload_to="palace/completion_certificate")

    website = models.URLField(max_length=300, verbose_name=_("website"), blank=True)
    postal_code = models.CharField(max_length=15, verbose_name=_("postal code"))

    objects = models.Manager()
    tree_manager = TreeManager()

    class Meta:
        db_table = "samam_palace_department"
        verbose_name = _("Department")
        verbose_name_plural = _("Departments")

    def __str__(self):
        return self.name


class DepartmentPhone(OrganizationModelMixin, PalaceModelMixin):
    title = models.CharField(max_length=255, verbose_name=_("title"), blank=False)
    phone_number = models.CharField(max_length=15, verbose_name=_("palace phone"), blank=False)
    is_internal = models.BooleanField(default=False, verbose_name=_("is internal phone"))

    class Meta:
        db_table = "samam_palace_phone"
        verbose_name = _("Palace Phone")
        verbose_name_plural = _("Palace Phones")
