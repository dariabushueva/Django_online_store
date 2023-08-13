from django.contrib import admin

from catalog.models import Category, Product, Contacts


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug')
    list_display_links = ('pk', 'name')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'price', 'category', 'slug')
    list_display_links = ('pk', 'name')
    list_filter = ('category',)
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('city', 'address', 'phone', )
    list_filter = ('address',)