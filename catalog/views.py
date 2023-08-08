from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from catalog.models import Product, Contacts, Category


class ProductListView(ListView):
    model = Product
    extra_context = {
        'title': 'Последние поступления:'
    }

    def get_queryset(self):
        queryset = Product.objects.order_by('-creation_date')[:6]
        return queryset


class ProductsListView(ListView):
    model = Product
    template_name = 'catalog/products_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category_id=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        category_item = Category.objects.get(pk=self.kwargs.get('pk'))
        context_data['title'] = f'Товары из категории: {category_item.name}'
        return context_data


class ProductDetailView(DetailView):
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(pk=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = f'Товар из категории: {Product.objects.get(pk=self.kwargs.get("pk"))}'
        return context_data


class CategoryListView(ListView):
    model = Category
    extra_context = {
        'title': 'Категории товаров'
    }


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'description', 'image_preview', 'price', 'category')
    success_url = reverse_lazy('catalog:index')
    extra_context = {
        'title': 'Добавить новый продукт:'
    }


def contacts(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name} ({email}): {message}')

    content = {
        'all_contacts': Contacts.objects.all(),
        'title': f'Контактная информация:'
    }
    return render(request, 'catalog/contacts.html', content)

