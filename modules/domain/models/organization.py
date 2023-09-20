from django.db import models
from django.utils.translation import gettext_lazy as _

from modules.common.models import CustomerModelMixin, OrganizationModelMixin, TimestampedModelMixin, PalaceModelMixin


class PlaceAccountType(OrganizationModelMixin, TimestampedModelMixin):
    name = models.CharField(max_length=150, verbose_name=_("name"))

    class Meta:
        db_table = "samam_place_account_type"
        verbose_name = _("Place Account Type")
        verbose_name_plural = _("Place Account Types")

    def __str__(self):
        return self.name


class Place(OrganizationModelMixin, TimestampedModelMixin, PalaceModelMixin):
    name = models.CharField(max_length=250, verbose_name=_("name"))
    account_type = models.ForeignKey(PlaceAccountType, verbose_name=_("place account type"), on_delete=models.CASCADE, related_name="%(class)ss")
    is_workplace = models.BooleanField(default=False)
    is_equipment_location = models.BooleanField(default=False)
    is_committee = models.BooleanField(default=False)
    is_team = models.BooleanField(default=False)
    is_management_leadership = models.BooleanField(default=False)

    class Meta:
        db_table = "samam_place"
        verbose_name = _("Place")
        verbose_name_plural = _("Place")

    def __str__(self):
        return self.name


class Organization(CustomerModelMixin):
    name = models.CharField(max_length=300, verbose_name=_("name"))
    language = models.CharField(max_length=5, verbose_name=_("language"))

    class Meta:
        db_table = "samam_organization"
        verbose_name = _("Organization")
        verbose_name_plural = _("Organizations")

    def __str__(self):
        return self.name
