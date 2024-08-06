from django.contrib import admin
from . import models
from extentions.utils import jalali_convertor
# Register your models here.

@admin.register(models.Shipment)
class ShipmentAdmin(admin.ModelAdmin):
        
    list_display = ['customer','shipment_date','address','city','state','country']
    search_fields = ['customer','city','state','country']
    list_filter = ['city']

@admin.register(models.Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['customer','jpayment_date','Payment_meto','amount']
    search_fields = ['amount','customer']
    list_filter = ["amount"]



    