# Generated by Django 3.2.5 on 2022-07-07 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_micro_blog_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='micro_blog',
            name='description',
            field=models.CharField(default='blank', max_length=50),
        ),
    ]
