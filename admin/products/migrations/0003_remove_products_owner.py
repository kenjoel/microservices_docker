# Generated by Django 3.2.8 on 2021-11-10 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_rename_name_products_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='owner',
        ),
    ]
