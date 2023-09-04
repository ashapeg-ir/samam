from django.db import models
from django.utils.translation import gettext_lazy as _

from django_extensions.db.models import ActivatorModel, TimeStampedModel


class Country(TimeStampedModel, ActivatorModel, models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        # db_table = "country"
        verbose_name = _("Country")
        verbose_name_plural = _("Countries")

    def __str__(self) -> str:
        return self.name.name


class Province(TimeStampedModel, models.Model):
    name = models.CharField(max_length=255, verbose_name=_("name"))
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name=_("country"))
    is_active = models.BooleanField(default=True, verbose_name=_("is active"))

    class Meta:
        db_table = "province"
        verbose_name = _("Province")
        verbose_name_plural = _("Provinces")

    def __str__(self):
        return self.name


class City(TimeStampedModel, models.Model):
    name = models.CharField(max_length=255, verbose_name=_("name"))
    province = models.ForeignKey(Province, on_delete=models.CASCADE, verbose_name=_("province"))
    is_active = models.BooleanField(default=True, verbose_name=_("is active"))

    class Meta:
        db_table = "city"
        verbose_name = _("City")
        verbose_name_plural = _("Cities")

    def __str__(self):
        return self.name
