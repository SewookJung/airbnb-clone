import random
from django.core.management.base import BaseCommand
from django_seed import Seed

from rooms import models as rooms_models
from users import models as users_models


class Command(BaseCommand):
    help = "This command created rooms!"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            type=int,
            default=2,
            help="How many create rooms you want to create?",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = users_models.User.objects.all()
        room_types = rooms_models.RoomType.objects.all()
        seeder.add_entity(
            rooms_models.Room,
            number,
            {
                "name": seeder.faker.address(),
                "host": lambda x: random.choice(all_users),
                "room_type": lambda x: random.choice(room_types),
                "guests": lambda x: random.randint(1, 20),
                "price": lambda x: random.randint(1, 300),
                "beds": lambda x: random.randint(1, 5),
                "baths": lambda x: random.randint(1, 5),
                "bedrooms": lambda x: random.randint(1, 5),
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} rooms created!"))
