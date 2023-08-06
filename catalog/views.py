from django.shortcuts import render
from catalog.models import Product, Contacts, Category


def index(request):

    content = {
        'object_list': Product.objects.order_by('-creation_date')[:3],
        'title': 'Последние поступления'
    }
    return render(request, 'catalog/index.html', content)


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


def products(request, pk):

    category_item = Category.objects.get(pk=pk)

    content = {
        'object_list': Product.objects.filter(category_id=pk),
        'title': f'Товары из категории: {category_item.name}'
    }
    return render(request, 'catalog/products.html', content)


def product(request, pk):

    category_item = Product.objects.get(pk=pk)

    content = {
        'object': Product.objects.get(pk=pk),
        'title': f'Товар из категории: {category_item.category}'
    }
    return render(request, 'catalog/product.html', content)


def categories(request):
    content = {
        'object_list': Category.objects.all(),
        'title': 'Категории товаров'
    }
    return render(request, 'catalog/categories.html', content)

