# Generated by Django 4.2.4 on 2023-08-23 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_version'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='number',
            field=models.CharField(max_length=10, unique=True, verbose_name='номер версии'),
        ),
    ]
