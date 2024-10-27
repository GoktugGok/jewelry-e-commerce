# Generated by Django 5.0.6 on 2024-10-09 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_categorysmenu'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='menu_items', to='main.categorysmenu'),
        ),
    ]
