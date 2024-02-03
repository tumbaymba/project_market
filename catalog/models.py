from django.conf import settings
from django.db import models

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')

    # created_at = models.BooleanField(default=True, verbose_name='created_at')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    title = models.CharField(max_length=250, verbose_name='наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    image = models.ImageField(upload_to='images_product/', **NULLABLE, verbose_name='изображение (превью)')
    # category = models.CharField(max_length=100, verbose_name='категория')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    price = models.PositiveIntegerField(**NULLABLE, verbose_name='цена за штуку')
    date_of_creation = models.DateField(**NULLABLE, verbose_name='дата создания')
    last_modified_date = models.DateField(**NULLABLE, verbose_name='дата последнего изменения')

    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='продавец')

    def __str__(self):
        return f'{self.title} {self.category}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        permissions = [
                (
                    'set_published',
                    'Может публиковать продукты'
                )
            ]


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    version_number = models.CharField(max_length=50, verbose_name="номер версии")
    version_title = models.CharField(max_length=150, verbose_name='название версии')
    is_active = models.BooleanField(default=False, verbose_name='признак текущей версии')

    def __str__(self):
        return f'{self.product}: {self.version_title} {self.version_number}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
