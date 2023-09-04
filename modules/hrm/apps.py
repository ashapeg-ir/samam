from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class HrmAppConfig(AppConfig):
    name = "modules.hrm"
    verbose_name = _("Human Resource Management")
    default_auto_field = "django.db.models.BigAutoField"

    def ready(self):
        """
        Hrm system checks
        Hrm signal registration
        """
        try:
            import modules.hrm.receivers  # noqa F401
        except ImportError:
            pass
