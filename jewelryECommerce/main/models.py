from django.utils import timezone
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.text import slugify
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User

class MenuItem(MPTTModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)  # Unique slug
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')  # parent menu item

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name
