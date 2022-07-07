# Generated by Django 3.2.5 on 2022-07-07 03:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_auto_20220310_1657'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='markdown', max_length=20)),
            ],
            options={
                'verbose_name_plural': '页面类型',
            },
        ),
        migrations.RenameField(
            model_name='pages',
            old_name='name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='pages',
            name='text_type',
        ),
        migrations.AddField(
            model_name='pages',
            name='page_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.pagecategories'),
            preserve_default=False,
        ),
    ]
