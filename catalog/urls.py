from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, contacts, ProductDetailView, ProductsListView, ProductCreateView, CategoryListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('<int:pk>/products/', ProductsListView.as_view(), name='products'),
    path('<int:pk>/product/', ProductDetailView.as_view(), name='product'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('contacts/', contacts, name='contacts'),
    path('product_form/', ProductCreateView.as_view(), name='product_form'),
]