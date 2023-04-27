from django.core.management.base import BaseCommand
from faker import Faker
from teachers.models import Teacher

faker = Faker()


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("quantity", type=int, nargs="?", default=100)

    def handle(self, quantity, **options):
        for _ in range(quantity):
            t = Teacher.objects.create(
                first_name=faker.first_name(), last_name=faker.last_name()
            )
            self.stdout.write(
                self.style.SUCCESS('Successfully created teacher with ID "%s"' % t.id)
            )
