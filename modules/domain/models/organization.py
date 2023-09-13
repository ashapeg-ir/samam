from django.db import models
from django.utils.translation import gettext_lazy as _

from modules.common.models import CustomerModelMixin


class Organization(CustomerModelMixin):
    name = models.CharField(max_length=300, verbose_name=_("name"))
    language = models.CharField(max_length=5, verbose_name=_("language"))

    class Meta:
        db_table = "samam_organization"
        verbose_name = _("Organization")
        verbose_name_plural = _("Organizations")

    def __str__(self):
        return self.name
