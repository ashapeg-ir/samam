from django.db import models
from django.utils.translation import gettext_lazy as _

from modules.common.models import UserModelMixin, OrganizationModelMixin, TimestampedModelMixin, ActivatedModelMixin


class Team(OrganizationModelMixin, TimestampedModelMixin, ActivatedModelMixin):
    name = models.CharField(max_length=300)
    palace = models.ForeignKey("Palace", on_delete=models.CASCADE, related_name="%(class)ss")

    class Meta:
        db_table = "team"
        verbose_name = _("team")
        verbose_name_plural = _("teams")


class TeamMembers(UserModelMixin):
    team = models.ForeignKey("hrm.Team", on_delete=models.CASCADE, related_name="%(class)ss")

    class Meta:
        db_table = "team_member"
        verbose_name = _("team member")
        verbose_name_plural = _("team members")

