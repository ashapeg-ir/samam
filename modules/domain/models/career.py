
from django.db import models
from django.utils.translation import gettext_lazy as _

from modules.common.models import TimestampedModelMixin, OrganizationModelMixin

__all__ = [
    "OrganizationLevel",
    "OrganizationNickname",
    "Relation",
    "MaritalStatus",
    "FieldOfStudy",
    "Grade",
    "Gender",
    "Occupation",
    "CareerField",
    "EmploymentState",
    "ElectronicAnnouncementTitle",
    "MilitaryStatus",
    "CareerGroup",
    "BloodType",
    "DegreeCompliance",
    "JobLevel",
    "OrganizationGraph",
    "Religion",
]


class Gender(TimestampedModelMixin):
    organization = models.ForeignKey(
        "domain.Organization", on_delete=models.CASCADE, related_name="%(class)ss", null=True, blank=True,
    )
    name = models.CharField(max_length=50, verbose_name=_("gender"))

    class Meta:
        db_table = "samam_gender"
        verbose_name = _("gender")
        verbose_name_plural = _("genders")


class OrganizationLevel(OrganizationModelMixin, TimestampedModelMixin):  # سطح سازمانی
    name = models.CharField(max_length=150, verbose_name=_("name"))
    is_manager = models.BooleanField(default=False, verbose_name=_("is manager"))  # رطبه مدیریتی

    class Meta:
        db_table = "samam_organization_level"
        verbose_name = _("organization level")
        verbose_name_plural = _("organization levels")


class OrganizationNickname(OrganizationModelMixin, TimestampedModelMixin):  # لقب سازمانی
    name = models.CharField(max_length=150, verbose_name=_("name"))
    gender = models.ForeignKey("Gender", on_delete=models.CASCADE, related_name="%(class)ss")

    class Meta:
        db_table = "samam_organization_nickname"
        verbose_name = _("organization nickname")
        verbose_name_plural = _("organization nicknames")


class Relation(OrganizationModelMixin, TimestampedModelMixin):  # نسبت ها
    name = models.CharField(max_length=150, verbose_name=_("name"))

    class Meta:
        db_table = "samam_relation"
        verbose_name = _("Relations")
        verbose_name_plural = _("Relations")


class MaritalStatus(OrganizationModelMixin, TimestampedModelMixin):
    name = models.CharField(max_length=150, verbose_name=_("name"))

    class Meta:
        db_table = "samam_marital_status"
        verbose_name = _("Marital Status")
        verbose_name_plural = _("Marital Status")


class FieldOfStudy(OrganizationModelMixin, TimestampedModelMixin):  # رشته تحصیلی
    name = models.CharField(max_length=150, verbose_name=_("name"))

    class Meta:
        db_table = "samam_field_of_study"
        verbose_name = _("Field of Study")
        verbose_name_plural = _("Field of Studies")


class Grade(OrganizationModelMixin, TimestampedModelMixin):  #‌مقطع تحصیلی
    name = models.CharField(max_length=150, verbose_name=_("name"))

    class Meta:
        db_table = "samam_grade"
        verbose_name = _("Grade")
        verbose_name_plural = _("Grades")


class Occupation(OrganizationModelMixin, TimestampedModelMixin):  # رسته شغلی
    name = models.CharField(max_length=150, verbose_name=_("name"))

    class Meta:
        db_table = "samam_occupation"
        verbose_name = _("Occupation")
        verbose_name_plural = _("Occupations")


class CareerField(OrganizationModelMixin, TimestampedModelMixin):  # رشته شغلی
    name = models.CharField(max_length=150, verbose_name=_("name"))

    class Meta:
        db_table = "samam_career_field"
        verbose_name = _("Career Field")
        verbose_name_plural = _("Career Fields")


class EmploymentState(OrganizationModelMixin, TimestampedModelMixin):  # حالت اشتغال
    name = models.CharField(max_length=150, verbose_name=_("name"))

    class Meta:
        db_table = "samam_employment_state"
        verbose_name = _("Employment State")
        verbose_name_plural = _("Employment States")


class CareerGroup(OrganizationModelMixin, TimestampedModelMixin):  # گروه شغلی
    name = models.CharField(max_length=150, verbose_name=_("name"))

    class Meta:
        db_table = "samam_career_group"
        verbose_name = _("Career Group")
        verbose_name_plural = _("Career Groups")


class ElectronicAnnouncementTitle(OrganizationModelMixin, TimestampedModelMixin):
    name = models.CharField(max_length=150, verbose_name=_("name"))

    class Meta:
        db_table = "samam_electronic_announcement"
        verbose_name = _("Electronic Announcement")
        verbose_name_plural = _("Electronic Announcements")


class MilitaryStatus(OrganizationModelMixin, TimestampedModelMixin):
    name = models.CharField(max_length=150, verbose_name=_("name"))

    class Meta:
        db_table = "samam_military_status"
        verbose_name = _("Military Status")
        verbose_name_plural = _("Military Statuses")


class Religion(OrganizationModelMixin, TimestampedModelMixin):
    name = models.CharField(max_length=150, verbose_name=_("name"))

    class Meta:
        db_table = "samam_religion"
        verbose_name = _("Religion")
        verbose_name_plural = _("Religions")


class BloodType(OrganizationModelMixin, TimestampedModelMixin):
    name = models.CharField(max_length=150, verbose_name=_("name"))

    class Meta:
        db_table = "samam_blood_type"
        verbose_name = _("Blood Type")
        verbose_name_plural = _("Blood Types")


class DegreeCompliance(OrganizationModelMixin, TimestampedModelMixin):  # انطباق مدرک تحصیلی
    name = models.CharField(max_length=150, verbose_name=_("name"))

    class Meta:
        db_table = "samam_degree_compliance"
        verbose_name = _("Degree Compliance")
        verbose_name_plural = _("Degree Compliances")


class JobLevel(OrganizationModelMixin, TimestampedModelMixin):  # سطح شغل
    name = models.CharField(max_length=150, verbose_name=_("name"))

    class Meta:
        db_table = "samam_job_level"
        verbose_name = _("Job Level")
        verbose_name_plural = _("Job Levels")


class OrganizationGraph(OrganizationModelMixin, TimestampedModelMixin):  # ساختار سازمانی

    class ObligationType:
        NONE = 0
        ELECTRONIC = 1
        PAPER = 2

    department = models.ForeignKey("Department", on_delete=models.CASCADE, related_name="%(class)ss")  # دپارتمان
    occupation = models.ForeignKey("Occupation", on_delete=models.CASCADE, related_name="%(class)ss")  # رسته شغلی
    career_field = models.ForeignKey("CareerField", on_delete=models.CASCADE, related_name="%(class)ss")  # رشته شغلی
    electronic_announcement_title = models.ForeignKey(
        "ElectronicAnnouncementTitle",
        on_delete=models.CASCADE,
        related_name="%(class)ss",
        verbose_name=_("electronic announcement title"),
    )  # عنوان ابلاغ
    career_group = models.ForeignKey(
        "CareerGroup",
        on_delete=models.CASCADE,
        related_name="%(class)ss",
        verbose_name=_("career group"),
    )
    organization_level = models.ForeignKey(
        "OrganizationLevel",
        on_delete=models.CASCADE,
        related_name="%(class)ss",
        verbose_name=_("organization level"),
    )
    obligate_to_job_description = models.IntegerField(
        verbose_name=_("obligate to job description"),
        default=ObligationType.NONE,
    )  # الزام به شرح وظیفه
    obligate_to_announcement = models.IntegerField(
        verbose_name=_("obligate to announcement"),
        default=ObligationType.NONE,
    )  # الزام به صدور ابلاغ
    row_name = models.CharField(max_length=150, verbose_name=_("row name"))  # عنوان ردیف سازمانی
    row_full_name = models.CharField(max_length=150, verbose_name=_("row full name"))  # عنوان ردیف سازمانی در سیستم مکاتبات
    number = models.IntegerField(verbose_name=_("number"))

    communicator = models.ForeignKey("User", on_delete=models.CASCADE, related_name="%(class)ss") # کد ردیف سازمانی صادره کننده ابلاغ
    # TODO: کد سند شرح وظیفه پیاده سازی شود

    class Meta:
        db_table = "samam_organization_graph"
        verbose_name = _("Organization Graph")
        verbose_name_plural = _("Organization Graphs")
