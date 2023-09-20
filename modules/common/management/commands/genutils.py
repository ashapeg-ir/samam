from django.core.management.base import BaseCommand
from faker import Faker
from faker.providers import company
from random import randint
from django.conf import settings
from modules.domain.models import User, Organization, PlaceAccountType, Place, Gender


class Command(BaseCommand):
    """General Utilities command

    This command provides general helper codes and tools
    """

    help = """
    This command provides general helper codes and tools
    """

    def add_arguments(self, parser):
        # Named (optional) arguments
        parser.add_argument(
            "--create-superuser",
            action="store_true",
            dest="create-superuser",
            help="Perform all initialization actions",
        )
        parser.add_argument(
            "--default-data",
            action="store_true",
            dest="default-data",
            help="Perform all initialization actions",
        )

    def create_superuser(
        self,
        email: str = "zarinpy@gmail.com",
        password: str = "test123",
        first_name: str = "omid",
        last_name: str = "zarinmahd",
        phone="09358588181",
    ):
        # import user here for isolation
        from modules.domain.models import User

        # create the initial superuser for test purposes
        User.objects.create_superuser(
            email=email, password=password, first_name=first_name, last_name=last_name, phone=phone
        )

    def insert_messages(self):
        import json

        from modules.domain.models import LanguageCaption
        print("insert system messages...")
        file_address = f"{settings.APPS_DIR}/common/messages/system_messages.json"
        json_messages = open(file_address, "r")
        messages = json.load(json_messages)
        objs = []
        for m in messages:
            objs.append(LanguageCaption(**m))
        LanguageCaption.objects.bulk_create(objs)

    def add_user(self):
        print("adding user...")
        Gender.objects.create(name="مرد")
        Gender.objects.create(name="زن")
        faker = Faker("fa_IR")
        for i in range(5):
            User.objects.create(
                phone=f"09{randint(100000000, 999999999)}",
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                email=faker.email(),
                gender=Gender.objects.get(id=1),
                is_active=True,
                is_verified=True,
                is_customer=True,
            )

    def add_org(self):
        print("add organization...")
        faker = Faker("fa_IR")
        faker.add_provider(company)
        for user in User.objects.all():
            Organization.objects.create(
                customer=user,
                name=faker.company(),
                language="fa",
            )

    def add_place_type(self):
        faker = Faker("fa_IR")
        for org in Organization.objects.all():
            PlaceAccountType.objects.create(
                organization=org,
                name=faker.name(),
            )

    def handle(self, *args, **options):
        """Handle command

        The entry point of the command

        :param args:
        :param options:
        :return:
        """
        # create a sample superuser if the appropriate argument is passed
        if options["create-superuser"]:
            print("creating superuser...")
            self.create_superuser()
        if options["default-data"]:
                print("insert default data...")
                # self.create_superuser()
                self.insert_messages()
                self.add_user()
                self.add_org()
                self.add_place_type()
