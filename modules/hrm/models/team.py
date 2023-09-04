from django.db import models
from django.utils.translation import gettext_lazy as _

from modules.common.models import UserModelMixin


class Team(models.Model):
    name = models.CharField(max_length=300)

    class Meta:
        verbose_name = _("team")
        verbose_name_plural = _("teams")


class TeamMembers(UserModelMixin):
    team = models.ForeignKey("hrm.Team", on_delete=models.CASCADE, related_name="%(class)ss")

    class Meta:
        verbose_name = _("team member")
        verbose_name_plural = _("team members")

