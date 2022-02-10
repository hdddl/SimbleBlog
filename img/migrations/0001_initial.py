# Generated by Django 3.2.5 on 2022-02-07 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='未分类', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('add_date', models.DateTimeField()),
                ('content', models.ImageField(upload_to='image/')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='img.album')),
            ],
        ),
    ]