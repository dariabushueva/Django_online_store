from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView

from catalog.forms import ContactForm
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
    paginate_by = 2
    model = Product
    template_name = 'catalog/products_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category__slug=self.kwargs.get('slug'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        category_item = Category.objects.get(slug=self.kwargs.get('slug'))
        context_data['title'] = f'Товары из категории: {category_item.name}'
        return context_data


class ProductDetailView(DetailView):
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(slug=self.kwargs.get('slug'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        category_item = Product.objects.get(slug=self.kwargs.get('slug'))
        context_data['title'] = f'Товар из категории: {category_item.category}'
        return context_data


class CategoryListView(ListView):
    model = Category
    extra_context = {
        'title': 'Категории товаров'
    }


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'slug', 'description', 'image_preview', 'price', 'category',)
    success_url = reverse_lazy('catalog:index')
    extra_context = {
        'title': 'Добавить новый продукт:'
    }


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'catalog/contacts.html'
    success_url = reverse_lazy('catalog:index')
    extra_context = {
        'title': f'Контактная информация:'
    }

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        context_data['all_contacts'] = Contacts.objects.all()
        return context_data

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('catalog:index')
