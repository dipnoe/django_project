# Generated by Django 4.2.3 on 2023-08-06 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_alter_blog_preview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='preview',
            field=models.ImageField(blank=True, null=True, upload_to='media/', verbose_name='Изображение'),
        ),
    ]
