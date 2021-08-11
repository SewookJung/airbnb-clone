import random

from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed

from lists import models as list_models
from users import models as user_models
from rooms import models as room_models


NAME = "Lists"


class Command(BaseCommand):
    help = f"This command created {NAME}!"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            type=int,
            default=2,
            help=f"How many create {NAME} you want to create?",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        users = user_models.User.objects.all()
        rooms = room_models.Room.objects.all()
        seeder.add_entity(
            list_models.List,
            number,
            {
                "user": lambda x: random.choice(users),
            },
        )
        created_lists = flatten(list(seeder.execute().values()))

        for pk in created_lists:
            list_obj = list_models.List.objects.get(pk=pk)
            random_rooms = rooms[random.randint(0, 5) : random.randint(6, 30)]
            list_obj.rooms.add(*random_rooms)

        self.stdout.write(self.style.SUCCESS(f"{number} {NAME} created!"))
