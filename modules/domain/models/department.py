from django.db import models
from django.utils.translation import gettext_lazy as _

from mptt.models import MPTTModel, TreeManager, TreeForeignKey
from model_utils.models import SoftDeletableModel

from modules.common.models import PalaceModelMixin, ActivatedModelMixin, TimestampedModelMixin, OrganizationModelMixin


class DepartmentOwnershipType(OrganizationModelMixin, TimestampedModelMixin, PalaceModelMixin):
    name = models.CharField(max_length=150, verbose_name=_("name"))

    class Meta:
        db_table = "samam_department_ownership_type"
        verbose_name = _("Department Ownership type")
        verbose_name_plural = _("Department Ownership Types")

    def __str__(self):
        return self.name


class DepartmentStatus(OrganizationModelMixin, TimestampedModelMixin, ActivatedModelMixin):
    name = models.CharField(max_length=150, verbose_name=_("name"))

    class Meta:
        db_table = "samam_department_status"
        verbose_name = _("Department Status")
        verbose_name_plural = _("Department Statuses")

    def __str__(self):
        return self.name


class Department(PalaceModelMixin, OrganizationModelMixin, TimestampedModelMixin, ActivatedModelMixin, MPTTModel):
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
    land_area = models.IntegerField(verbose_name=_("land area"), blank=True, null=True)
    noble_area = models.IntegerField(verbose_name=_("area of noble"), blank=True, null=True)
    operation_date = models.DateField(verbose_name=_("operation date"), blank=True, null=True)
    completion_date = models.DateField(verbose_name=_("completion date"), blank=True, null=True)
    completion_certificate = models.ImageField(upload_to="palace/completion_certificate", blank=True, null=True)
    status = models.ForeignKey(DepartmentStatus, verbose_name=_("department status"), on_delete=models.CASCADE, related_name="%(class)ss", blank=True, null=True)
    phone = models.CharField(max_length=15, verbose_name=_("department phone"))
    ownership = models.ForeignKey(DepartmentOwnershipType, verbose_name=_("department ownership type"), on_delete=models.CASCADE, related_name="%(class)ss", blank=True, null=True)
    objects = models.Manager()
    tree_manager = TreeManager()

    class Meta:
        db_table = "samam_palace_department"
        verbose_name = _("Department")
        verbose_name_plural = _("Departments")

    def __str__(self):
        return self.place.name


class TeamDistribution(OrganizationModelMixin, PalaceModelMixin, TimestampedModelMixin, ActivatedModelMixin):
    department = models.ForeignKey(
        Department,
        verbose_name=_("department"),
        on_delete=models.CASCADE,
        related_name="%(class)ss",
    )

    class Meta:
        db_table = "samam_palace_team_distribution"
        verbose_name = _("Team Distribution")
        verbose_name_plural = _("Team Distributions")
