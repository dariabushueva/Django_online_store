from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import index, contacts, product, products, categories

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('<int:pk>/products/', products, name='products'),
    path('<int:pk>/product/', product, name='product'),
    path('categories/', categories, name='categories'),
    path('contacts/', contacts, name='contacts')
]