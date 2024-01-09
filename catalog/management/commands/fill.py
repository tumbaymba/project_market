from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()

        category_list = [
            {"pk": 1, "title": "Чай, кофе, какао",
             "description": "Чай, кофе, какао"},
            {"pk": 2, "title": "Кондитерские изделия",
             "description": "Конфеты, шоколад, торты, пирожные, десерты"}
        ]

        categories = []
        for category in category_list:
            categories.append(Category(**category))

        Category.objects.bulk_create(categories)

        product_list = [{
            "pk": 1,
            "title": "Бисквитные изделия",
            "description": "Пирожное бисквитное МЕДВЕЖОНОК БАРНИ с шоколадной начинкой, 5х30г, Россия, 150 г",
            "image": "images_product/барни.jpeg",
            "category": categories[1],
            "price": 85,
            "date_of_creation": "2024-01-09",
            "last_modified_date": "2024-01-09"
        },
            {"pk": 3, "title": "Зефир",
             "description": "Зефир BONVIDA бело-розовый, 540г, Россия, 540 г",
             "image": "images_product/зефир.jpeg",
             "category": categories[1],
             "price": 175,
             "date_of_creation": "2024-01-09",
             "last_modified_date": "2024-01-09"},
            {"pk": 6, "title": "Цикорий",
             "description": "Цикорий ELZA Натуральный, ст/б, 100г, Германия, 100 г",
             "image": "images_product/цикорий.jpeg",
             "category": categories[0],
             "price": 365,
             "date_of_creation": "2024-01-09",
             "last_modified_date": "2024-01-09"}
        ]

        products = []
        for product in product_list:
            products.append(Product(**product))

        Product.objects.bulk_create(products)
