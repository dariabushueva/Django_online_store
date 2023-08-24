from pprint import pprint

from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, FormView, UpdateView, DeleteView

from catalog.forms import ContactForm, ProductForm
from catalog.models import Product, Contacts, Category, Version


class ProductListView(ListView):
    model = Product
    extra_context = {
        'title': 'Последние поступления:'
    }

    def get_queryset(self):
        queryset = Product.objects.order_by('-creation_date')[:6]
        return queryset

  #  def get_context_data(self, *args, **kwargs):
  #      context_data = super().get_context_data(*args, **kwargs)
#
  #      try:
  #          version = Version.objects.get(is_active=True)
  #          context_data['version'] = version.name
  #      except Version.DoesNotExist:
  #          context_data['version'] = None
#
  #      return context_data

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
    #    pprint(context_data)
        for product in context_data['object_list']:
            active_version = product.version_set.filter(is_active=False)
            print(active_version)
            if active_version:
         #       context_data['active_version'] = active_version
                product.active_version_number = active_version   # как здесь получить номер из ?
         #       product.active_version_name = active_version   # как здесь получить имя?
            else:
                product.active_version_number = None
                product.active_version_name = None
#
        return context_data   # надо ли предварительно расширять context_data на номер и имя версии?


class ProductsListView(ListView):
    paginate_by = 3
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
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')
    extra_context = {
        'title': 'Добавить новый продукт:'
    }


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')
    extra_context = {
        'title': 'Редактировать продукт:'
    }

    def get_success_url(self):
        return reverse('catalog:product_detail', args=[self.kwargs.get('slug')])


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:index')
    extra_context = {
        'title': 'Удаление записи:'
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
