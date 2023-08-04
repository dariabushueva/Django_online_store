from django.contrib import admin

from catalog.models import Category, Product, Contacts


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'price', 'category',)
    list_filter = ('category',)
    search_fields = ('name', 'description')


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('city', 'address', 'phone',)
    list_filter = ('address',)