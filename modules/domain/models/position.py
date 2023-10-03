from django.db import models
from django.utils.translation import gettext_lazy as _

from modules.common.models import TimestampedModelMixin, OrganizationModelMixin
from modules.domain.models import User

__all__ = ["EmploymentType", "EmploymentStatus", "Position"]


class EmploymentType(OrganizationModelMixin, TimestampedModelMixin):  # نوع استخدام
    name = models.CharField(max_length=150, verbose_name=_("name"))

    class Meta:
        db_table = "samam_employment_type"
        verbose_name = _("Employment Type")
        verbose_name_plural = _("Employment Types")


class EmploymentStatus(OrganizationModelMixin, TimestampedModelMixin):  # وضعیت اشتغال
    name = models.CharField(max_length=150, verbose_name=_("name"))
    state = models.ForeignKey("EmploymentState", on_delete=models.CASCADE, related_name="%(class)ss")

    class Meta:
        db_table = "samam_employment_status"
        verbose_name = _("Employment Status")
        verbose_name_plural = _("Employment Statuses")


class Position(OrganizationModelMixin, TimestampedModelMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="%(class)ss")
    organization_graph = models.ForeignKey("OrganizationGraph", on_delete=models.CASCADE, related_name="%(class)ss")
    employment_type = models.ForeignKey("EmploymentType", on_delete=models.CASCADE, related_name="%(class)ss")
    city = models.ForeignKey("City", on_delete=models.CASCADE, related_name="%(class)ss")
    region = models.ForeignKey("ResidentialArea", on_delete=models.CASCADE, related_name="%(class)ss")
    phone = models.CharField(max_length=20, verbose_name=_("phone"), null=True, blank=True)
    postal_code = models.CharField(max_length=20, verbose_name=_("postal code"), null=True, blank=True)
    start_date = models.DateField(verbose_name=_("start date"), null=True, blank=True)
    end_date = models.DateField(verbose_name=_("end date"), null=True, blank=True)
    email = models.EmailField(verbose_name=_("email"), null=True, blank=True)
    employment_status = models.ForeignKey("EmploymentStatus", on_delete=models.CASCADE, related_name="%(class)ss")
    job_level = models.ForeignKey("JobLevel", on_delete=models.CASCADE, related_name="%(class)ss")
