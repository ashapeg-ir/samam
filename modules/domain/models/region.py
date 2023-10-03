from django.db import models
from django.utils.translation import gettext_lazy as _

from modules.common.models import TimestampedModelMixin, OrganizationModelMixin


class Country(TimestampedModelMixin, OrganizationModelMixin):
    name = models.CharField(max_length=200)

    class Meta:
        db_table = "samam_country"
        verbose_name = _("Country")
        verbose_name_plural = _("Countries")

    def __str__(self) -> str:
        return self.name


class Province(TimestampedModelMixin, OrganizationModelMixin):
    name = models.CharField(max_length=255, verbose_name=_("name"))
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name=_("country"))

    class Meta:
        db_table = "samam_province"
        verbose_name = _("Province")
        verbose_name_plural = _("Provinces")

    def __str__(self):
        return self.name


class City(TimestampedModelMixin, OrganizationModelMixin):
    name = models.CharField(max_length=255, verbose_name=_("name"))
    province = models.ForeignKey(Province, on_delete=models.CASCADE, verbose_name=_("province"))

    class Meta:
        db_table = "samam_city"
        verbose_name = _("City")
        verbose_name_plural = _("Cities")

    def __str__(self):
        return self.name


class ResidentialArea(TimestampedModelMixin, OrganizationModelMixin):
    name = models.CharField(max_length=255, verbose_name=_("name"))
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name=_("city"))

    class Meta:
        db_table = "samam_residential_area"
        verbose_name = _("Residential Area")
        verbose_name_plural = _("Residential Areas")

    def __str__(self):
        return self.name
