# Generated by Django 4.2.4 on 2023-09-01 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_product_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='опубликовано'),
        ),
    ]
