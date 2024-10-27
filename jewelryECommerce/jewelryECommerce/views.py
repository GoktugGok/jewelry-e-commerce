from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from main.models import MenuItem
import json

def get_menus():
    menu_items = MenuItem.objects.all()  # Tüm menü öğelerini al
    menus_json = {}
    for item in menu_items:
        if item.parent is None:
            menus_json[item.id] = {
                'name': item.name,
                'slug': item.slug,
                'children': []
            }
            for child in item.get_children():
                child_data = {
                    'MainId': item.name,
                    'title': child.name,
                    'slug': child.slug,
                    'items': [{'name': subchild.name, 'slug': subchild.slug} for subchild in child.get_children()]
                }
                menus_json[item.id]['children'].append(child_data)
    return menus_json
