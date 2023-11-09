from django.db import models
from django.utils.translation import gettext_lazy as _

from djchoices import ChoiceItem, DjangoChoices

from modules.common.models import UserModelMixin, ActivatedModelMixin, TimestampedModelMixin, OrganizationModelMixin


class Supervisor(OrganizationModelMixin, UserModelMixin, TimestampedModelMixin, ActivatedModelMixin):
    class Level(DjangoChoices):
        org = ChoiceItem("org", "organization")
        palace = ChoiceItem("plc", "palace")
        department = ChoiceItem("dpt", "department")

    level = models.CharField(max_length=3, choices=Level.choices, default="")
    obj_id = models.BigIntegerField(null=False, blank=False)

    class Meta:
        db_table = "samam_supervisor"
        verbose_name = _("Supervisor")
        verbose_name_plural = _("Supervisors")
