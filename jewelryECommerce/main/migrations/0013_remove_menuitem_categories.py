# Generated by Django 5.0.6 on 2024-10-14 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_rename_stock_product_reviewscount_product_active_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='categories',
        ),
    ]