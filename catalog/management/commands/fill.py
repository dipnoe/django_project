import json

from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):
    help = 'Добавляем категории в БД!'

    def handle(self, *args, **options):
        Category.objects.all().delete()
        category_list = []

        with open('category_data.json') as file:
            data = json.loads(file.read())
            for category in data:
                category_list.append(category.get('fields'))

        category_create = []
        for category_item in category_list:
            category_create.append(Category(**category_item))

        Category.objects.bulk_create(category_create)

        self.stdout.write(self.style.SUCCESS('Все заполнилось'))
