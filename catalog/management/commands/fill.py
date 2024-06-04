from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()
        category_list = [
            {"pk": 1, "title": "Огурцы, помидоры, лук",
             "description": "Огурцы, помидоры, лук и пр."},
            {"pk": 2, "title": "Овощи",
             "description": "Огурцы, помидоры, лук и пр."}
        ]
        categories = []
        for category in category_list:
            categories.append(Category(**category))

        Category.objects.bulk_create(categories)

        product_list = [{
            "pk": 1,
            "title": "Огурцы",
            "description": "Огурцы, короткоплодные, в развес, пр-во Россия",
            "image": "images_product/cucumber_1.jpg",
            "category": categories[1],
            "price": 247,
            "date_of_creation": "2024-05-31",
            "last_modified_date": "2024-05-31"
        },
            {"pk": 3, "title": "Помидоры",
             "description": "Помидор красный, в развес, пр-во Россия",
             "image": "images_product/pomidor.jpg",
             "category": categories[1],
             "price": 152,
             "date_of_creation": "2024-05-31",
             "last_modified_date": "2024-05-31"},
            {"pk": 6, "title": "Лук",
             "description": "Лук репчатый, в развес, пр-во Россия",
             "image": "images_product/luk.jpg",
             "category": categories[1],
             "price": 96,
             "date_of_creation": "2024-05-31",
             "last_modified_date": "2024-05-31"}
        ]

        products = []
        for product in product_list:
            products.append(Product(**product))

        Product.objects.bulk_create(products)
