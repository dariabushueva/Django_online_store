import json
from django.core.management import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options):

        Product.objects.all().delete()
        Category.objects.all().delete()

        with open('catalog_data.json', 'r', encoding='utf-8') as json_file:
            catalog_data = json.load(json_file)

        for item in catalog_data:
            if item["model"] == "catalog.category":
                Category.objects.create(pk=item["pk"],
                                        name=item["fields"]["name"],
                                        description=item["fields"]["description"]
                                        )
            elif item["model"] == "catalog.product":
                category = Category.objects.get(pk=item["fields"]["category"])
                Product.objects.create(pk=item["pk"],
                                       name=item["fields"]["name"],
                                       description=item["fields"]["description"],
                                       image_preview=item["fields"]["image_preview"],
                                       category=category,
                                       price=item["fields"]["price"],
                                       creation_date=item["fields"]["creation_date"],
                                       modification_date=item["fields"]["modification_date"]
                                       )





