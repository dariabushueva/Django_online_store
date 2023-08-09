from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='заголовок')
    body = models.TextField(verbose_name='содержимое')
    image_preview = models.ImageField(upload_to='media/', verbose_name='изображение', **NULLABLE)
    creation_date = models.DateField(auto_now_add=True, verbose_name='дата создания')
    is_published = models.BooleanField(default=True, verbose_name='опубликовано')
    count_views = models.PositiveIntegerField(default=0, verbose_name='просмотры')
    slug = models.CharField(max_length=150, verbose_name='slug')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
