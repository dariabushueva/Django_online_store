from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.http import Http404
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
        if self.request.user.is_staff:
            queryset = Product.objects.order_by('-creation_date')[:6]
        else:
            queryset = Product.objects.filter(Q(is_published=True) | Q(owner=self.request.user))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        for product in context_data['object_list']:
            active_version = Version.objects.filter(product=product, is_active=True).last()
            if active_version:
                product.active_version_number = active_version.number
                product.active_version_name = active_version.name
            else:
                product.active_version_number = None
                product.active_version_name = None
        return context_data


class ProductsListView(ListView):
    paginate_by = 3
    model = Product
    template_name = 'catalog/products_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_staff:
            queryset = queryset.filter(category__slug=self.kwargs.get('slug'))
        else:
            queryset = Product.objects.filter(Q(is_published=True, category__slug=self.kwargs.get('slug')) |
                                              Q(owner=self.request.user, category__slug=self.kwargs.get('slug')))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        category_item = Category.objects.get(slug=self.kwargs.get('slug'))
        context_data['title'] = f'Товары из категории: {category_item.name}'
        for product in context_data['object_list']:
            active_version = Version.objects.filter(product=product, is_active=True).last()
            if active_version:
                product.active_version_number = active_version.number
                product.active_version_name = active_version.name
            else:
                product.active_version_number = None
                product.active_version_name = None
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

        active_version = Version.objects.filter(product=self.object, is_active=True).last()
        if active_version:
            context_data['active_version_number'] = active_version.number
            context_data['active_version_name'] = active_version.name
        else:
            context_data['active_version_number'] = None
            context_data['active_version_name'] = None

        return context_data


class CategoryListView(ListView):
    model = Category
    extra_context = {
        'title': 'Категории товаров'
    }


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')
    extra_context = {
        'title': 'Добавить новый продукт:'
    }

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')
    extra_context = {
        'title': 'Редактировать продукт:'
    }
    permission_required = 'catalog.change_product'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user and not self.request.user.is_staff:
            raise Http404
        return self.object

    def get_success_url(self):
        return reverse('catalog:product_detail', args=[self.kwargs.get('slug')])


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:index')
    extra_context = {
        'title': 'Удаление записи:'
    }
    permission_required = 'catalog.delete_product'


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
