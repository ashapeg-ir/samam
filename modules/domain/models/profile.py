from django.db import models
from django.utils.translation import gettext_lazy as _

from modules.common.models import TimestampedModelMixin, OrganizationModelMixin
from modules.domain.models import User
from djchoices.choices import ChoiceItem, DjangoChoices


class Profile(OrganizationModelMixin, TimestampedModelMixin):

    class Status(DjangoChoices):
        occupied = ChoiceItem(1, "occupied")  # مشغول به کار
        earned_leave = ChoiceItem(2, "earned leave")  # مرخصی
        medical_leave = ChoiceItem(3, "medical leave")  # مرخصی استعلاجی
        academic_leave = ChoiceItem(4, "academic leave")  # مرخصی تحصیلی
        disability_leave = ChoiceItem(5, "disability leave")  # مرخصی صعب الاج
        unpaid_leave = ChoiceItem(6, "unpaid leave")  # مرخصی بدون حقوق
        excused_absence = ChoiceItem(7, "excused absence")  # غیبت موجه
        unexcused_absence = ChoiceItem(8, "unexcused absence")  # غیبت غیر موجه
        retirement = ChoiceItem(9, "retirement")   # بازنشستگی
        resignation = ChoiceItem(10, "resignation")  # انصراف
        death = ChoiceItem(11, "death")  # مرگ
        partial_disability = ChoiceItem(12, "partial disability")  # ازکارافتادگی جزعی
        general_lethargy = ChoiceItem(13, "general lethargy")  # ازکارافتادگی کلی
        on_mission = ChoiceItem(14, "on mission")  # ماموریت
        academic_mission = ChoiceItem(15, "academic mission")  # ماموریت تحصیلی
        women_part_time = ChoiceItem(16, "women part time")  # طرح نیمه وقت بانوان
        pcwp = ChoiceItem(17, "Participants in the coefficient workforce plan")  # مشمولین طرح نیروی ضریب
        pddw = ChoiceItem(18, "Partially disabled due to work")  # از کارافتاده جزئی ناشی از کار
        pfcw = ChoiceItem(19, "Partial failure not caused by work")  # از کار افتاده جزیی غیر ناشی از کار
        wrtd = ChoiceItem(20, "Work-related total disability")  # از کار افتاده کلی ناشی از کار
        nrtd = ChoiceItem(21, "Non-work related total disability")  # از کار افتاده کلی غیر ناشی از کار

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
    status = models.PositiveSmallIntegerField(choices=Status.choices, db_index=True, null=False, blank=False)
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

    class Meta:
        db_table = "samam_profile"
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")
