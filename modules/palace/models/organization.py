from django.db import models
from modules.common.models import UserModelMixin


class Organization(UserModelMixin):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name
