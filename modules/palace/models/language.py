from django.db import models
from django.db.models.manager import BaseManager
from django.utils.translation import gettext_lazy as _

from modules.common.models import CustomerModelMixin, TimestampedModelMixin, OrganizationModelMixin


class LanguageCaptionManager(BaseManager):

    def _(self, code, language):
        value = self.get_queryset().filter(language__code=language, code=code).first()
        if not value:
            value = ""
        return value


class LanguageCaption(CustomerModelMixin, OrganizationModelMixin, TimestampedModelMixin, models.Model):
    title = models.TextField(verbose_name=_("title"))
    language = models.ForeignKey(
        "Organization",
        on_delete=models.CASCADE,
        verbose_name=_("language"),
        to_field="language",
    )
    code = models.IntegerField(verbose_name=_("code"))
    is_editable = models.BooleanField(default=False, verbose_name=_("is editable"))

    class Meta:
        db_table = "samam_language_caption"
        verbose_name = _("Language Caption")
        verbose_name_plural = _("Language Captions")

    def __str__(self):
        return self.title
