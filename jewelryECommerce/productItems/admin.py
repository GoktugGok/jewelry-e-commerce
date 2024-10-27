from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Product , Images

# Register your models here.
class ProductImagesInline(admin.TabularInline):
    model = Images
    extra = 5  # Boş form alanları ekler
    readonly_fields = ['image_tag']  # Görüntü önizlemesi
    # Bu aşağıdaki satırı eklemeyi unutmayın.
    fields = ['title', 'image', 'image_tag']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'image_tag', 'active']
    readonly_fields = ('image_tag',)
    inlines = [ProductImagesInline]
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Product, ProductAdmin)