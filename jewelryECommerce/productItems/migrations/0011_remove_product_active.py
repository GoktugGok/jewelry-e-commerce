# Generated by Django 5.0.6 on 2024-10-28 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productItems', '0010_product_stock'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='active',
        ),
    ]
