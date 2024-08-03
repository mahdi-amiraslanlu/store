from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['shipment','payment','customer','order_date','total_price']
    list_display_links = ("shipment","payment","customer")
    search_fields=['customer']

@admin.register(models.Order_Item)
class Order_ItemAdmin(admin.ModelAdmin):
    list_display = ['product',"order","quantity" , 'price']
    list_display_links = ("order","product")
    search_fields=['price']

@admin.register(models.Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ['product'] 
    list_display_links = ["product"]

@admin.register(models.Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['product' , "customer" , "quantity"] 
    list_display_links = ["product" , "customer"]
 




