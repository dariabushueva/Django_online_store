import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

from catalog.models import NULLABLE


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Email')
    phone = models.CharField(max_length=35, verbose_name='Телефон', **NULLABLE)
    country = models.CharField(max_length=50, verbose_name='Страна', **NULLABLE)
    avatar = models.ImageField(upload_to='user/', verbose_name='Ававтар', **NULLABLE)

    is_active = models.BooleanField(default=False, verbose_name='Активный')
    verification_key = models.CharField(max_length=20, verbose_name='Ключ верификации', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
