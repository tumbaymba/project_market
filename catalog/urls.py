from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import contacts, ProductListView, HomeView, ProductCreateView, ProductDetailView, ProductUpdateView, \
    ProductDeleteView, version_active, CategoryListView

app_name = CatalogConfig.name

urlpatterns = [
    # path('', home),
    path('', HomeView.as_view(), name='home'),
    path('contacts/', contacts),
    # path('<int:pk>/product', product, name='product'),
    path('<int:pk>/product/', ProductListView.as_view(), name='product'),
    path('<int:pk>/view/', cache_page(60)(ProductDetailView.as_view()), name='view_product'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
    path('version/<int:pk>/', version_active, name='version_active'),
    path('category/', CategoryListView.as_view(), name='category_list'),

]
