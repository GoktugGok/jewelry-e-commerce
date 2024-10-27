from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from main.models import MenuItem
from productItems.models import Product
from .models import Category, Collection,Color,Compatible,Metal,PriceRange ,Size,Theme
from jewelryECommerce.views import get_menus
import json

def category(request, category_slug):
    menu_items = MenuItem.objects.all()  # Tüm menü öğelerini al
    menus_json = get_menus()
    category = MenuItem.objects.get(slug=category_slug)
    ParentDetail = None
    if category.parent != None:
        ParentDetail = category.parent

    categoryMenus = Category.objects.all()
    collectionMenus = Collection.objects.all()
    colorMenus = Color.objects.all()
    compatibleyMenus = Compatible.objects.all()
    metalMenus = Metal.objects.all()
    priceRangeMenus = PriceRange.objects.all()
    sizeMenus = Size.objects.all()
    themeMenus = Theme.objects.all()

    products = Product.objects.filter(mainCategories__slug=category_slug)
    total = products.count()

    print(total)
    context = {
        'menus_json': json.dumps(menus_json),  
        'menu_items': menu_items, 
        'category': category,
        'ParentDetail':ParentDetail,
        'categoryMenus':categoryMenus,
        'collectionMenus':collectionMenus,
        'colorMenus':colorMenus,
        'compatibleyMenus':compatibleyMenus,
        'metalMenus':metalMenus,
        'priceRangeMenus':priceRangeMenus,
        'sizeMenus':sizeMenus,
        'themeMenus':themeMenus,
        'products':products,
        'total':total
    }
    
    return render(request, 'category.html', context)

