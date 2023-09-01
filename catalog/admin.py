from django.contrib import admin

from catalog.models import Category, Product, Contacts, Version


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug')
    list_display_links = ('pk', 'name')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'price', 'category', 'slug', 'is_published')
    list_display_links = ('pk', 'name')
    list_filter = ('category',)
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('is_published',)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('product', 'number', 'name', 'is_active')
    list_display_links = ('number', 'name',)
    list_editable = ('is_active',)


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('city', 'address', 'phone', )
    list_filter = ('address',)