from django.db import models
from django.utils.translation import gettext_lazy as _

from modules.common.models import TimestampedModelMixin


class LanguageCaption(TimestampedModelMixin, models.Model):
    organization = models.ForeignKey(
        "domain.Organization", on_delete=models.CASCADE, related_name="%(class)ss", blank=True, null=True
    )
    title = models.CharField(max_length=200, verbose_name=_("title"))
    language = models.CharField(verbose_name=_("language"), max_length=5)
    code = models.IntegerField(verbose_name=_("code"))
    is_editable = models.BooleanField(default=False, verbose_name=_("is editable"))

    class Meta:
        db_table = "samam_language_caption"
        verbose_name = _("Language Caption")
        verbose_name_plural = _("Language Captions")

    def __str__(self):
        return self.title


def get_message(code, language):
    value = LanguageCaption.objects.filter(language=language, code=code).values("title").first()["title"]
    if not value:
        value = ""
    return value
