# Generated by Django 5.0.6 on 2024-10-23 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productItems', '0007_product_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='boyutlar',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
