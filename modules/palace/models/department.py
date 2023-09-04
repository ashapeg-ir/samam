from django.db import models
from django.utils.translation import gettext_lazy as _

from model_utils.models import SoftDeletableModel
from django_extensions.db.models import ActivatorModel, TimeStampedModel
from modules.palace.models import Palace


class Department(TimeStampedModel, ActivatorModel, SoftDeletableModel, models.Model):
    name = models.CharField(max_length=400, verbose_name=_("name"))
    description = models.TextField(blank=True, null=True, verbose_name=_("description"))
    palace = models.ForeignKey(Palace, on_delete=models.CASCADE, verbose_name=_("palace"))

    class Meta:
        db_table = "palace_department"
        verbose_name = _("Department")
        verbose_name_plural = _("Departments")

    def __str__(self):
        return self.name.title
