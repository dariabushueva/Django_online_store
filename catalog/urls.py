from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ContactFormView, ProductDetailView, ProductsListView, ProductCreateView, CategoryListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('<slug:slug>/products/', ProductsListView.as_view(), name='products'),
    path('product/<slug:slug>/', ProductDetailView.as_view(), name='product'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('contacts/', ContactFormView.as_view(), name='contacts'),
    path('product_form/', ProductCreateView.as_view(), name='product_form'),
]