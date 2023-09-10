import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class SoftDeletableModel(models.Model):
    """
    An abstract base class model with a ``is_removed`` field that
    marks entries that are not going to be used anymore, but are
    kept in db for any reason.
    Default manager returns only not-removed entries.
    """
    is_removed = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def delete(self, using=None, soft=True, *args, **kwargs):
        """
        Soft delete object (set its ``is_removed`` field to True).
        Actually delete object if setting ``soft`` to False.
        """
        if soft:
            self.is_removed = True
            self.save(using=using)
        else:
            return super().delete(using=using, *args, **kwargs)


class TimestampedModelMixin(models.Model):
    """Timestamp mixin

    This mixin adds a timestamp to model for create and update events
    """

    created = models.DateTimeField(
        _("created at"),
        auto_now_add=True,
        help_text=_("This is the timestamp of the object creation."),
    )
    updated = models.DateTimeField(
        _("updated at"),
        auto_now=True,
        help_text=_("This is the timestamp of the object update"),
    )

    class Meta:
        ordering = ["-created"]
        abstract = True


class UniversalModelMixin(models.Model):
    """Universal primary key mixin

    This mixin changes the primary key of a model to UUID field.
    Using UUID as primary key could help application scalability
    and could make migrating to microservice, or exporting or
    importing data easier,
    by using a universally unique identifier
    for object that without fear of collision.
    """

    id = models.UUIDField(
        verbose_name=_("universal unique id"),
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        help_text=_("Universally unique object identifier"),
    )

    class Meta:
        abstract = True

    @property
    def serial(self) -> str:
        return str(self.id).upper().split("-")[0]

    def __str__(self):
        return self.serial


class UserModelMixin(models.Model):
    """
    Abstract base class for models that have a user as a foreign key.
    """

    user = models.ForeignKey(
        "hrm.User", on_delete=models.CASCADE, related_name="%(class)ss"
    )

    class Meta:
        abstract = True


class CustomerModelMixin(models.Model):
    """
    Abstract base class for models that have a user as a foreign key.
    """

    customer = models.ForeignKey(
        "hrm.User", on_delete=models.CASCADE, related_name="%(class)ss", limit_choices_to={"is_customer": True}
    )

    class Meta:
        abstract = True


class OrganizationModelMixin(models.Model):
    organization = models.ForeignKey(
        "palace.Organization", on_delete=models.CASCADE, related_name="%(class)ss"
    )

    class Meta:
        abstract = True


class PalaceModelMixin(models.Model):
    palace = models.ForeignKey(
        "palace.Palace", on_delete=models.CASCADE, related_name="%(class)ss"
    )

    class Meta:
        abstract = True


class ActivatedModelMixin(models.Model):
    """Active objects mixin

    This mixin add is_active field to the model
    which indicated the model active status.
    It also adds a queryset to support
    getting only active objects.
    """

    is_active = models.BooleanField(
        verbose_name=_("active"),
        default=True,
        db_index=True,
        help_text=_(
            "Designates if this object should be considered active or not "
            "or to simulate soft delete behaviour."
        ),
    )

    class Meta:
        abstract = True
