from django.db import models
from django.utils.translation import gettext_lazy as _

from mptt.models import MPTTModel, TreeManager, TreeForeignKey

from modules.common.models import CustomerModelMixin, ActivatedModelMixin, TimestampedModelMixin, OrganizationModelMixin


class Palace(CustomerModelMixin, OrganizationModelMixin, TimestampedModelMixin, ActivatedModelMixin, MPTTModel):
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
    city = models.ForeignKey("City", on_delete=models.CASCADE, verbose_name=_("city"))  # TODO:
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
