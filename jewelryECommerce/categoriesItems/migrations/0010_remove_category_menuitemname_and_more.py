# Generated by Django 5.0.6 on 2024-10-30 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categoriesItems', '0009_category_menuitemname_collection_menuitemname_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='menuItemName',
        ),
        migrations.RemoveField(
            model_name='collection',
            name='menuItemName',
        ),
        migrations.RemoveField(
            model_name='color',
            name='menuItemName',
        ),
        migrations.RemoveField(
            model_name='compatible',
            name='menuItemName',
        ),
        migrations.RemoveField(
            model_name='family',
            name='menuItemName',
        ),
        migrations.RemoveField(
            model_name='metal',
            name='menuItemName',
        ),
        migrations.RemoveField(
            model_name='metalname',
            name='menuItemName',
        ),
        migrations.RemoveField(
            model_name='pricerange',
            name='menuItemName',
        ),
        migrations.RemoveField(
            model_name='size',
            name='menuItemName',
        ),
        migrations.RemoveField(
            model_name='stones',
            name='menuItemName',
        ),
        migrations.RemoveField(
            model_name='theme',
            name='menuItemName',
        ),
    ]
