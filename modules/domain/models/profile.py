from django.db import models
from django.utils.translation import gettext_lazy as _

from modules.common.models import TimestampedModelMixin, OrganizationModelMixin
from modules.domain.models import User


class Profile(OrganizationModelMixin, TimestampedModelMixin):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.ForeignKey("Gender", on_delete=models.CASCADE, related_name="%(class)ss", null=True, blank=True)
    city = models.ForeignKey("City", on_delete=models.CASCADE, related_name="%(class)ss", null=True, blank=True)
    grade = models.ForeignKey("Grade", on_delete=models.CASCADE, related_name="%(class)ss", null=True, blank=True)
    region = models.ForeignKey(
        "ResidentialArea",
        on_delete=models.CASCADE,
        related_name="%(class)ss",
        null=True,
        blank=True,
    )
    blood_type = models.ForeignKey(
        "BloodType",
        on_delete=models.CASCADE,
        related_name="%(class)ss",
        null=True,
        blank=True,
    )
    marital_status = models.ForeignKey(
        "MaritalStatus",
        on_delete=models.CASCADE,
        related_name="%(class)ss",
        null=True,
        blank=True,
    )
    military_status = models.ForeignKey(
        "MilitaryStatus",
        on_delete=models.CASCADE,
        related_name="%(class)ss",
        null=True,
        blank=True,
    )
    Organization_nickname = models.ForeignKey(
        "OrganizationNickname",
        on_delete=models.CASCADE,
        related_name="%(class)ss",
        null=True,
        blank=True,
    )
    field_of_study = models.ForeignKey(
        "FieldOfStudy",
        on_delete=models.CASCADE,
        related_name="%(class)ss",
        null=True,
        blank=True,
    )
    degree_compliance = models.ForeignKey(
        "DegreeCompliance",
        on_delete=models.CASCADE,
        related_name="%(class)ss",
        null=True,
        blank=True,
    )
    religion = models.ForeignKey(
        "Religion",
        on_delete=models.CASCADE,
        related_name="%(class)ss",
        null=True,
        blank=True,
    )
    personnel_code = models.CharField(max_length=10, verbose_name=_("personnel code"), null=True, blank=True)
    picture = models.ImageField(null=True, blank=True, upload_to="profile", verbose_name=_("picture"))
    phone = models.CharField(max_length=15, verbose_name=_("phone"))
    birthdate = models.DateField(null=True, blank=True, verbose_name=_("birthdate"))
    national_id = models.CharField(max_length=10, verbose_name=_("national id"), null=True, blank=True)
    identification_id = models.CharField(max_length=10, verbose_name=_("identification id"), null=True, blank=True)
    essential_phone = models.CharField(
        max_length=15,
        verbose_name=_("essential phone"),
        null=True,
        blank=True,
    )
