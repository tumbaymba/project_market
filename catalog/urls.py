from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts, ProductListView, HomeView

app_name = CatalogConfig.name

urlpatterns = [
    # path('', home),
    path('', HomeView.as_view()),
    path('contacts/', contacts),
    # path('home/', home),
    path('home/', HomeView.as_view()),
    # path('<int:pk>/product', product, name='product'),
    path('<int:pk>/product/', ProductListView.as_view(), name='product'),

]
