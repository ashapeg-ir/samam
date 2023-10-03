import random
import datetime
from random import randint

from django.conf import settings
from django.core.management.base import BaseCommand

from faker import Faker
from faker.providers import company

from modules.domain.models import (
    City,
    User,
    Place,
    Gender,
    Palace,
    Country,
    Province,
    PalaceKind,
    PalaceLevel,
    Organization,
    PalaceStatus,
    PlaceAccountType,
    PalaceAccountType,
    PalaceOwnershipType,
)


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
        username="09358588181",
    ):
        # import user here for isolation
        from modules.domain.models import User

        # create the initial superuser for test purposes
        User.objects.create_superuser(
            email=email, password=password, first_name=first_name, last_name=last_name, username=username
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
        faker = Faker("fa_IR")
        faker.add_provider(company)
        kind1 = {
            "is_workplace": True,
            "is_equipment_location": False,
            "is_committee": False,
            "is_team": False,
            "is_management_leadership": False,
        }
        kind2 = {
            "is_workplace": False,
            "is_equipment_location": True,
            "is_committee": False,
            "is_team": False,
            "is_management_leadership": False,
        }
        kind3 = {
            "is_workplace": False,
            "is_equipment_location": False,
            "is_committee": True,
            "is_team": False,
            "is_management_leadership": False,
        }
        choices = [kind1, kind2, kind3]
        for i in range(20):
            user = User.objects.create(
                username=f"09{randint(100000000, 999999999)}",
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                email=faker.email(),
                # gender=Gender.objects.get(id=1),
                is_active=True,
                is_verified=True,
                is_customer=True,
            )
            org = Organization.objects.create(
                customer=user,
                name=faker.company(),
                language="fa",
            )
            Gender.objects.create(name="مرد", organization=org)
            Gender.objects.create(name="زن", organization=org)
            PalaceAccountType.objects.create(
                organization=org,
                name=faker.company(),
            )
            Country.objects.create(
                organization=org,
                name="ایران"
            )
            Province.objects.create(
                organization=org,
                country_id=1,
                name=faker.administrative_unit()
            )
            City.objects.create(
                organization=org,
                name=faker.city(),
                province_id=1,
            )
            PalaceLevel.objects.create(
                organization=org,
                name=faker.company(),
            )
            PalaceStatus.objects.create(
                organization=org,
                name=faker.company(),
            )
            PalaceKind.objects.create(
                organization=org,
                name=faker.company(),
            )
            PalaceOwnershipType.objects.create(
                organization=org,
                name=faker.company(),
            )
            palace = Palace.objects.create(
                organization=org,
                name=faker.company(),
                status_id=1,
                kind_id=1,
                ownership_type_id=1,
                address=faker.address()[:7],
                city_id=1,
                account_type_id=1,
                land_area=random.randint(0, 1000),
                noble_area=random.randint(0, 1000),
                distance_to_province=random.randint(0, 1000),
                distance_to_same_palace=random.randint(0, 1000),
                operation_date=datetime.date(2000, 1, 1),
                completion_date=datetime.date(2000, 1, 1),
                palace_level_id=1,
                phone=f"09{randint(100000000, 999999999)}",
                email=faker.email(),
                # operation_license=faker.image_url(),
                postal_code=random.randint(0, 1000),
                description=faker.address()[:6],
            )
            PlaceAccountType.objects.create(
                organization=org,
                name=faker.company()[:5],
            )
            Place.objects.create(
                palace=palace,
                organization=org,
                name=faker.company()[:5],
                account_type_id=1,
                **random.choices(choices)[0],
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
                self.create_superuser()
                self.insert_messages()
                self.add_user()
