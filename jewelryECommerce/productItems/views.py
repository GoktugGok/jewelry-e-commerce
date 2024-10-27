from django.shortcuts import render, get_object_or_404
from main.models import MenuItem
from .models import Product
from jewelryECommerce.views import get_menus
import json

def product(request, product_slug):
    menu_items = MenuItem.objects.all()  # Tüm menü öğelerini al
    menus_json = get_menus()
    product = Product.objects.get(slug=product_slug)

    pageDetail = [pageDetail.slug for pageDetail in product.mainCategories.all()]
    pageRoad = MenuItem.objects.filter(slug__in=pageDetail)
    
    page_hierarchy = []
    added_slugs = set()
    
    for item in pageRoad:
        parent_items = item.get_ancestors(include_self=True)
        for parent in parent_items:
            if parent.slug not in added_slugs:
                page_hierarchy.append(parent)
                added_slugs.add(parent.slug)

    productDetails = {}
    compatibles = product.compatibles.all()
    if compatibles:
        compatible_names = [compatible.name for compatible in compatibles]
        productDetails.update({'compatibles': compatible_names})

    collections = product.collections.all()
    if collections:
        collection_names = [collection.name for collection in collections]
        productDetails.update({'collections': collection_names})

    stones = product.stones.all()
    if stones:
        stone_name = [stone.name for stone in stones]
        productDetails.update({'stones': stone_name})
    
    colors = product.colors.all()
    if colors:
        color_name = [color.name for color in colors]
        productDetails.update({'colors': color_name})

    themes = product.themes.all()
    if themes:
        theme_name = [theme.name for theme in themes]
        productDetails.update({'themes': theme_name})

    categories = product.categories.all()
    if categories:
        category_name = [category.name for category in categories]
        productDetails.update({'categories': category_name})

    metals = product.metals.all()
    if metals:
        metal_name = [metal.name for metal in metals]
        productDetails.update({'metals':metal_name})
    
    metalNames = product.metalNames.all()
    if metalNames:
        metalName_name = [metal.name for metal in metalNames]
        productDetails.update({'metalNames':metalName_name})

    product_images = product.images.all()

    metals_set = set()  # Tekrarsız metaller seti
    selected_metals = product.metals.all()  # Şu anki ürünün metallerini al
    print(selected_metals)
    if product.family.exists():
        family_name = product.family.first().name 
        family_products = Product.objects.filter(family__name=family_name)
        
        for family_product in family_products:
            metals_set.add(family_product)
            print(family_product.metals.all())

    return render(request, 'product.html', {
        'menus_json': json.dumps(menus_json),  
        'menu_items': menu_items ,
        'product':product,
        'productDetails':productDetails,
        'page_hierarchy':page_hierarchy,
        'product_images':product_images,
        'metals_set': metals_set,
        'selected_metals': selected_metals,
})
