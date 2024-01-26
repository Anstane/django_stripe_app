from django.core.management.base import BaseCommand
from api.models import Item

class Command(BaseCommand):
    help = 'Create some items'

    def handle(self, *args, **options):
        items_data = [
            {'name': 'Чехол для телефона', 'description': 'Чехол для iPhone', 'price': 25000},
            {'name': 'Постельное белье', 'description': 'Бежевое постельное белье', 'price': 300000},
            {'name': 'Чайник', 'description': 'Электрический чайник', 'price': 100000},
            {'name': 'Кувшин', 'description': 'Стеклянный кувшин', 'price': 70000},
            {'name': 'Стул', 'description': 'Деревянный стул', 'price': 200000},
        ]

        for data in items_data:
            Item.objects.create(**data)

        self.stdout.write(self.style.SUCCESS('Successfully created items'))
