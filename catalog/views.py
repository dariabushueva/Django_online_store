from django.shortcuts import render
from catalog.models import Product, Contacts


def index(request):
    latest_products = Product.objects.order_by('-creation_date')[:5]
    for product in latest_products:
        print(f"Product: {product.name} - {product.price}")

    return render(request, 'catalog/index.html')


def contacts(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name} ({email}): {message}')

    all_contacts = Contacts.objects.all()
    return render(request, 'catalog/contacts.html', {'all_contacts': all_contacts})

