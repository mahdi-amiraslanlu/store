from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['name']


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['category' , "sku" , 'description','price','stock']
    search_fields=['sku' , 'price','category']
    list_filter = ['price']



