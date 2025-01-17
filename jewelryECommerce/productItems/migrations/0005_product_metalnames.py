# Generated by Django 5.0.6 on 2024-10-22 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categoriesItems', '0006_metalname'),
        ('productItems', '0004_alter_images_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='metalNames',
            field=models.ManyToManyField(blank=True, related_name='products', to='categoriesItems.metalname'),
        ),
    ]
