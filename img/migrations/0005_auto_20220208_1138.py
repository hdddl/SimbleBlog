# Generated by Django 3.2.5 on 2022-02-08 03:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('img', '0004_remove_image_add_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'verbose_name_plural': '相册'},
        ),
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['name'], 'verbose_name_plural': '图片'},
        )
    ]
