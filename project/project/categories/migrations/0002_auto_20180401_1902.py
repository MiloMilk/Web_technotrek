# Generated by Django 2.0.3 on 2018-04-01 19:02

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categories',
            new_name='Category',
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
    ]
