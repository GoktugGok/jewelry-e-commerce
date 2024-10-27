from django.contrib import admin
from .models import Category,Collection,Color,Family,Compatible,Stones,Metal,MetalName,PriceRange,Theme,Size
from mptt.admin import MPTTModelAdmin

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)


class CollectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Collection, CollectionAdmin)

class FamilyAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Family, FamilyAdmin)

class ColorAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug','color')
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Color, ColorAdmin)

class CompatibleAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Compatible, CompatibleAdmin)

class StonesAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Stones, StonesAdmin)

class MetalAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Metal, MetalAdmin)

class MetalNameAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(MetalName, MetalNameAdmin)

class PriceRangeAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(PriceRange, PriceRangeAdmin)

class SizeAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Size, SizeAdmin)

class ThemeAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Theme, ThemeAdmin)

    