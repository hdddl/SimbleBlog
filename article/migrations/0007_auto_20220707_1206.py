# Generated by Django 3.2.5 on 2022-07-07 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_auto_20220707_1122'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='private',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='micro_blog',
            name='private',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
