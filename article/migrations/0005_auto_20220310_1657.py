# Generated by Django 3.2.5 on 2022-03-10 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_auto_20220208_1039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='updated',
        ),
        migrations.RemoveField(
            model_name='micro_blog',
            name='updated',
        ),
        migrations.RemoveField(
            model_name='pages',
            name='updated',
        ),
    ]
