from django.utils import timezone
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.text import slugify
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
from categoriesItems.models import Category,Collection,Color,Compatible,Stones,Metal,MetalName,PriceRange,Theme,Size

class MenuItem(MPTTModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)  # Unique slug
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')  # parent menu item
    categories = models.ManyToManyField(Category, related_name='menuItem', blank=True)
    compatibles = models.ManyToManyField(Compatible, related_name='menuItem', blank=True)
    stones = models.ManyToManyField(Stones,related_name='menuItem', blank=True)
    metals = models.ManyToManyField(Metal, related_name='menuItem', blank=True)
    metalNames = models.ManyToManyField(MetalName,related_name='menuItem', blank=True)
    colors = models.ManyToManyField(Color, related_name='menuItem', blank=True)
    collections = models.ManyToManyField(Collection, related_name='menuItem', blank=True)
    sizes = models.ManyToManyField(Size, related_name='menuItem', blank=True)
    boyutlar = models.TextField()
    themes = models.ManyToManyField(Theme, related_name='menuItem', blank=True)
    priceRange = models.ManyToManyField(PriceRange, related_name='menuItem', blank=True)
    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name
