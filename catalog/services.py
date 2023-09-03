from django.core.cache import cache

from catalog.models import Category
from config.settings import CACHE_ENABLED


def get_cached_categories():

    if CACHE_ENABLED:
        key = 'categories_list'
        categories_list = cache.get(key)
        if categories_list is None:
            categories_list = Category.objects.all()
            cache.set(key, categories_list)
    else:
        categories_list = Category.objects.all()
    return categories_list
