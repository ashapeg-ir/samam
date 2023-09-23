from django.db import models
from django.utils.translation import gettext_lazy as _

from modules.common.models import TimestampedModelMixin


class Gender(TimestampedModelMixin):
    name = models.CharField(max_length=50, verbose_name=_("gender"))

    class Meta:
        db_table = "samam_gender"
        verbose_name = _("gender")
        verbose_name_plural = _("genders")
