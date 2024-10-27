from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import MenuItem
from jewelryECommerce.views import get_menus
import json

def index(request):

    menu_items = MenuItem.objects.all()  # Tüm menü öğelerini al
    menus_json = get_menus()
    
    return render(request, 'index.html', {
        'menus_json': json.dumps(menus_json),  # JSON formatında veriyi hazırla
        'menu_items': menu_items  # Menü için Django template'ine veri gönder
        
})


