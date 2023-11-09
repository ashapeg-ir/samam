import factory

from modules.domain.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
