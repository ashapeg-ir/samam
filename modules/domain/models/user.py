from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

from modules.domain.managers import UserManager


class User(AbstractUser):
    organization = models.ForeignKey(
        "domain.Organization", on_delete=models.CASCADE, related_name="%(class)ss", null=True, blank=True
    )
    first_name = models.CharField(_("first name"), max_length=300, blank=True)
    last_name = models.CharField(_("last name"), max_length=300, blank=True)
    is_verified = models.BooleanField(
        verbose_name=_("user verified"),
        default=False,
        help_text=_("Designates if this user has been verified."),
    )
    is_customer = models.BooleanField(
        _("is customer"),
        default=False,
        help_text=_("Designates whether the user is customer or not"),
    )
    username = models.CharField(max_length=150, unique=True, verbose_name=_("username"))
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects: UserManager = UserManager()  # type: ignore

    class Meta:
        db_table = "samam_user"
        verbose_name = _("user")
        verbose_name_plural = _("users")
        ordering = ["-date_joined"]

    def __str__(self):
        return self.username
