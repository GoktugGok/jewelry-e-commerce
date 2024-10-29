from django.db import models
from categoriesItems.models import Category,Collection,Color,Family,Compatible,Stones,Metal,MetalName,PriceRange,Theme,Size
from main.models import MenuItem
from django.utils.safestring import mark_safe
import random
import string

def generate_unique_code():
    numbers = ''.join(random.choices(string.digits, k=6))
    letters = ''.join(random.choices(string.ascii_uppercase, k=2))
    code = f'{numbers}{letters}'
    return code

class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=100,unique=True,blank=True)
    code = models.CharField(max_length=8,unique=True,default=generate_unique_code)
    family = models.ManyToManyField(Family,related_name='products',blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    mainCategories = models.ManyToManyField(MenuItem,related_name='MainCategoriesProducts',blank=True)
    stock = models.IntegerField(default=0)
    categories = models.ManyToManyField(Category, related_name='products', blank=True)
    compatibles = models.ManyToManyField(Compatible, related_name='products', blank=True)
    stones = models.ManyToManyField(Stones,related_name='products', blank=True)
    metals = models.ManyToManyField(Metal, related_name='products', blank=True)
    metalNames = models.ManyToManyField(MetalName,related_name='products', blank=True)
    colors = models.ManyToManyField(Color, related_name='products', blank=True)
    collections = models.ManyToManyField(Collection, related_name='products', blank=True)
    sizes = models.ManyToManyField(Size, related_name='products', blank=True)
    boyutlar = models.TextField()
    themes = models.ManyToManyField(Theme, related_name='products', blank=True)
    priceRange = models.ManyToManyField(PriceRange, related_name='products', blank=True)

    image = models.ImageField(blank=True, upload_to='images/', default="default.png")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.code:
            while True:
                new_code = generate_unique_code()
                if not Product.objects.filter(code=new_code).exists():
                    self.code = new_code
                    break
        super(Product, self).save(*args, **kwargs)

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'

    def img_preview(self):  # Yeni
        return mark_safe(f'<img src="{self.image.url}" width="300"/>')

class Images(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'