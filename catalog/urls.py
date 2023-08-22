from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import *

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('<slug:slug>/products/', ProductsListView.as_view(), name='products'),
    path('product_detail/<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('contacts/', ContactFormView.as_view(), name='contacts'),
    path('product_create/', ProductCreateView.as_view(), name='product_create'),
    path('product_edit/<slug:slug>', ProductUpdateView.as_view(), name='product_edit'),
    path('product_delete/<slug:slug>', ProductDeleteView.as_view(), name='product_delete')
]
