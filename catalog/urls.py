from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts, home, product

app_name = CatalogConfig.name

urlpatterns = [
    path('', home),
    path('contacts/', contacts),
    path('home/', home),
    path('<int:pk>/product', product, name='product'),
]
