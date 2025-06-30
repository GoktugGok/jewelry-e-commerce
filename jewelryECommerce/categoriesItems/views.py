from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from main.models import MenuItem
from productItems.models import Product
from .models import Category, Collection, Color, Compatible, Metal, PriceRange, Size, Theme
from jewelryECommerce.views import get_menus
from django.template.loader import render_to_string
import json

def category(request, category_slug):
    # Menü öğelerini al, navbar falan için
    menu_items = MenuItem.objects.all()
    menus_json = get_menus()

    # İstenen kategoriyi bul, yoksa 404 ver
    category = get_object_or_404(MenuItem, slug=category_slug)

    # Eğer kategori bir alt kategori ise, üstünü al, yoksa None
    ParentDetail = category.parent if category.parent else None

    # Bu kategoriye ait ve satışta olan tüm ürünler
    all_products = Product.objects.filter(mainCategories__slug=category_slug, available=True)

    # GET parametrelerinden filtre değerlerini al (örn: color=Mavi, metal=925 ... gibi)
    filters = {
        'categories': request.GET.getlist('category'),
        'metals': request.GET.getlist('metal'),
        'colors': request.GET.getlist('color'),
        'themes': request.GET.getlist('theme'),
        'collections': request.GET.getlist('collection'),
        'priceRange': request.GET.getlist('price'),
    }

    # Filtreleme yap (eğer filtre var ise, o filtreye göre süz)
    products = all_products
    for field, values in filters.items():
        if values:
            # Örnek: categories__name__in = ['Mavi', 'Kırmızı']
            q = {f"{field}__name__in": values}
            products = products.filter(**q).distinct()

    # Filtrelenmiş ürün sayısı
    total = products.count()

    # Her filtre tipi için kaç ürün var sayısını hesapla
    def count_items(filtered_queryset, attr_name):
        counts = {}
        for product in filtered_queryset:
            for item in getattr(product, attr_name).all():
                counts[item.name] = counts.get(item.name, 0) + 1
        return counts

    metal_counts = count_items(products, 'metals')
    color_counts = count_items(products, 'colors')
    collection_counts = count_items(products, 'collections')
    theme_counts = count_items(products, 'themes')
    priceRange_counts = count_items(products, 'priceRange')
    categories_counts = count_items(products, 'categories')

    # Metals_set: ürün ailesindeki metal çeşitlerini topla (ürün bazlı)
    metals_set = set()
    for product in products:
        if product.family.exists():
            family_name = product.family.first().name
            family_products = Product.objects.filter(family__name=family_name)
            for family_product in family_products:
                metals_set.add(family_product)

    # Ana kategori mi değil mi kontrol et (sayfada kullanılacak)
    is_main_category = category.parent is None

    # Eğer AJAX isteği ise (filtrelerde sayfa yenilemeden değişiklik için)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        # Sadece ürün listesini render et ve json ile döndür
        html = render_to_string('product_list.html', {
            'products': products,
            'metals_set': metals_set,
            'category': category,
            'menu_items': menu_items,
            'menus_json': json.dumps(menus_json),
            'total': total,
            'categories_counts': categories_counts,
            'metal_counts': metal_counts,
            'color_counts': color_counts,
            'collection_counts': collection_counts,
            'theme_counts': theme_counts,
            'priceRange_counts': priceRange_counts,
            'ParentDetail': ParentDetail,
            'is_main_category': is_main_category,
        }, request=request)
        return JsonResponse({'html': html,
    'total': total})

    # AJAX değilse normal tam sayfa render et
    context = {
        'menus_json': json.dumps(menus_json),
        'menu_items': menu_items,
        'category': category,
        'ParentDetail': ParentDetail,
        'products': products,
        'total': total,
        'metals_set': metals_set,
        'categories_counts': categories_counts,
        'metal_counts': metal_counts,
        'color_counts': color_counts,
        'collection_counts': collection_counts,
        'theme_counts': theme_counts,
        'priceRange_counts': priceRange_counts,
        'is_main_category': is_main_category,
    }

    return render(request, 'category.html', context)
