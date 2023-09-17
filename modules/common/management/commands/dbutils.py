from django.db import connection
from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Database Utilities command

    This command provides helper codes and tools for database operations
    """

    help = """
    This command provides helper codes and tools for database operations
    """

    def add_arguments(self, parser):
        # Named (optional) arguments
        parser.add_argument(
            "--reset-db",
            action="store_true",
            dest="reset-db",
            help="Perform all initialization actions",
        )
        parser.add_argument(
            "--insert-messages",
            action="store_true",
            dest="insert-messages"
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

    def reset_database_tables(self):
        """Reset database tables

        This command drops all database tables and recreates them
        by running django migrations.

        Notes:
            - It does not remove postgis related table(s).

        :return:
        """
        # drop the tables
        with connection.cursor() as cursor:
            cursor.execute(
                # language=sql
                """
                DO $$ DECLARE
                    r RECORD;
                BEGIN
                    FOR r IN (SELECT tablename FROM pg_tables WHERE schemaname = current_schema() AND tablename != 'spatial_ref_sys') LOOP  -- # noqa
                        EXECUTE 'DROP TABLE IF EXISTS ' || quote_ident(r.tablename) || ' CASCADE';
                    END LOOP;
                END $$;
                """
            )

    def handle(self, *args, **options):
        """Handle command

        The entry point of the command

        :param args:
        :param options:
        :return:
        """
        # reset the database if the appropriate argument is passed
        if options["reset-db"]:
            self.reset_database_tables()
        if options["insert-messages"]:
            self.insert_messages()