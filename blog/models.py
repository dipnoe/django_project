from django.db import models

NULLABLE = {'blank': True, 'null': True}


# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.CharField(max_length=250, verbose_name='slug', **NULLABLE)
    body = models.TextField(verbose_name='Содержимое')
    preview = models.ImageField(upload_to='blog/', verbose_name='Превью', **NULLABLE)
    create_date = models.DateTimeField(verbose_name='Дата создания', auto_now=True)
    is_published = models.BooleanField(default=False, verbose_name='опубликовано')
    views_count = models.PositiveSmallIntegerField(default=0, verbose_name='Количество просмотров', editable=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
        ordering = ['-create_date']
