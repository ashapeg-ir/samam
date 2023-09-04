from typing import Optional

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(
        self, email: str, password: Optional[str], **extra_fields
    ) -> "User":
        """
        Create and save a user with the given email, and password.
        """
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password) if password else user.set_unusable_password()
        user.save()
        return user

    def create_user(self, email: str, password: str = None, **extra_fields) -> "User":
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email: str, password: str, **extra_fields) -> "User":
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    first_name = models.CharField(_("first name"), max_length=300, blank=True)
    last_name = models.CharField(_("last name"), max_length=300, blank=True)
    phone = models.CharField(max_length=15, verbose_name=_("phone"), unique=True)
    is_verified = models.BooleanField(
        verbose_name=_("email verified"),
        default=False,
        help_text=_("Designates if this user's email has been verified."),
    )
    is_customer = models.BooleanField(
        _("is customer"),
        default=False,
        help_text=_("Designates whether the user is customer or not"),
    )
    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects: UserManager = UserManager()  # type: ignore

    class Meta:
        db_table = "hrm_user"
        verbose_name = _("user")
        verbose_name_plural = _("users")
        ordering = ["-date_joined"]

    def __str__(self):
        return self.phone
