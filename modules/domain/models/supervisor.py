from django.utils.translation import gettext_lazy as _

from modules.common.models import UserModelMixin, ActivatedModelMixin, TimestampedModelMixin, OrganizationModelMixin ,PalaceModelMixin


class Supervisor(OrganizationModelMixin, UserModelMixin, TimestampedModelMixin, ActivatedModelMixin, PalaceModelMixin):

    class Meta:
        db_table = "samam_supervisor"
        verbose_name = _("Supervisor")
        verbose_name_plural = _("Supervisors")
