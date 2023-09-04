from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PalaceAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'modules.palace'
    verbose_name = _("Palace")
