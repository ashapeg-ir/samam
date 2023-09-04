from django.db import models
from django.db.models.manager import BaseManager
from django.utils.translation import gettext_lazy as _

from django_extensions.db.models import TimeStampedModel
from modules.palace.models import Palace


class LanguageCaptionManager(BaseManager):

    def _(self, code, language):
        value = self.get_queryset().filter(language__code=language, code=code).first()
        if not value:
            value = ""
        return value


class Language(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name=_("title"))
    code = models.CharField(max_length=5)

    class Meta:
        db_table = "language"
        verbose_name = _("Language")
        verbose_name_plural = _("Languages")

    def __str__(self):
        return f"{self.title}-{self.code}"


class LanguageCaption(TimeStampedModel, models.Model):
    title = models.TextField(verbose_name=_("title"))
    language = models.ForeignKey(Language, on_delete=models.CASCADE, verbose_name=_("language"))
    palace = models.ForeignKey(Palace, on_delete=models.CASCADE, verbose_name=_("palace"))
    code = models.IntegerField(verbose_name=_("code"))
    is_editable = models.BooleanField(default=False, verbose_name=_("is editable"))

    class Meta:
        db_table = "language_caption"
        verbose_name = _("Language Caption")
        verbose_name_plural = _("Language Captions")

    def __str__(self):
        return self.title
