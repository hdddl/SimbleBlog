# Generated by Django 3.2.5 on 2022-02-08 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('img', '0005_auto_20220208_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, upload_to='image/'),
        ),
    ]
