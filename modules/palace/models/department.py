from django.db import models
from django.utils.translation import gettext_lazy as _

from mptt.models import MPTTModel, TreeManager, TreeForeignKey
from model_utils.models import SoftDeletableModel

from modules.common.models import CustomerModelMixin, ActivatedModelMixin, TimestampedModelMixin
from modules.palace.models import Palace


class Department(CustomerModelMixin, TimestampedModelMixin,ActivatedModelMixin, SoftDeletableModel, MPTTModel):
    name = models.CharField(max_length=400, verbose_name=_("name"))
    description = models.TextField(blank=True, null=True, verbose_name=_("description"))
    palace = models.ForeignKey(Palace, on_delete=models.CASCADE, verbose_name=_("palace"))
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
        verbose_name=_("parent"),
    )
    objects = models.Manager()
    tree_manager = TreeManager()

    class Meta:
        db_table = "palace_department"
        verbose_name = _("Department")
        verbose_name_plural = _("Departments")

    def __str__(self):
        return self.name
