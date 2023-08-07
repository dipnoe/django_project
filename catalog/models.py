from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    preview = models.ImageField(upload_to='previews/', verbose_name='Изображение', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')
    price = models.PositiveSmallIntegerField(verbose_name='Цена')
    create_date = models.DateField(verbose_name='Дата создания', auto_now_add=True)
    last_modified_date = models.DateField(verbose_name='Дата последнего изменения', auto_now=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование', **NULLABLE)
    description = models.TextField(verbose_name='Описание', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


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
