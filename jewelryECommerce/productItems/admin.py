from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Product , Images
from django.contrib import admin
from django.urls import path
from django.utils.html import format_html
from .models import Product
from django.shortcuts import redirect
# Register your models here.
class ProductImagesInline(admin.TabularInline):
    model = Images
    extra = 5  # Boş form alanları ekler
    readonly_fields = ['image_tag']  # Görüntü önizlemesi
    # Bu aşağıdaki satırı eklemeyi unutmayın.
    fields = ['title', 'image', 'image_tag']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'image_tag', 'available_status']  # available yerine özel fonksiyon
    readonly_fields = ('image_tag',)
    inlines = [ProductImagesInline]
    prepopulated_fields = {'slug': ('name',)}

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('toggle-available/<int:pk>/', self.admin_site.admin_view(self.toggle_available), name='toggle-available'),
        ]
        return custom_urls + urls

    def available_status(self, obj):
        # available durumuna göre simge ve tıklama bağlantısı
        if obj.available:
            return format_html('<a href="{}"><img src="/static/admin/img/icon-yes.svg" alt="Available" /></a>',
                               self.get_toggle_available_url(obj.id))
        else:
            return format_html('<a href="{}"><img src="/static/admin/img/icon-no.svg" alt="Not Available" /></a>',
                               self.get_toggle_available_url(obj.id))
    available_status.short_description = 'Available'
    available_status.allow_tags = True

    def get_toggle_available_url(self, obj_id):
        return f"toggle-available/{obj_id}/"

    def toggle_available(self, request, pk):
        product = Product.objects.get(pk=pk)
        product.available = not product.available
        product.save()
        return redirect(request.META.get('HTTP_REFERER'))

admin.site.register(Product, ProductAdmin)