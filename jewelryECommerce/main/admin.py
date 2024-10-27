from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from mptt.admin import DraggableMPTTAdmin
from .models import MenuItem 

# class ProductImagesInline(admin.TabularInline):
#     model = Images
#     extra = 5
#     readonly_fields = ['image_tag']

admin.site.register(MenuItem, DraggableMPTTAdmin,
    prepopulated_fields = {"slug": ("name",)},
    list_display=(
        'tree_actions',
        'indented_title',
        # ...more fields if you feel like it...
    ),
    list_display_links=(
        'indented_title',
    ),)






# @admin.register(Product)
# class ShoesDetailAdmin(admin.ModelAdmin):
#     list_display = ['name', 'image_tag', 'active']
#     search_fields = ('name','category',)
#     readonly_fields = ('image_tag',)
#     inlines=[ProductImagesInline]
#     prepopulated_fields = {"slug": ("name",)}

# @admin.register(Images)
# class ImagesAdmin(admin.ModelAdmin):
#     list_display = ['title','product', 'image_tag']
#     readonly_fields = ['image_tag']
