# Generated by Django 4.2.4 on 2023-08-28 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='verification_key',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Ключ верификации'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Активный'),
        ),
    ]
