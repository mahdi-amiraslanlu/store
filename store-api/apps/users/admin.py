from django.contrib import admin
from . import models
from .models import CustomerUser
# Register your models here.


class CustomUserAdmin(admin.ModelAdmin):

    list_display =[ 'name' , "email","adress", "phone_number",'is_active',"is_staff","is_verified"]
    fieldsets = [
        ('import your informations' , {'fields' :['name' ,'email',"adress", "phone_number","password"] }),
        ('import user permission' , {'fields' : ["is_active"  , "is_staff","is_verified" ]}),
    ]
    search_fields=['email','name']
admin.site.register(CustomerUser , CustomUserAdmin)


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin): 

    list_display =[ 'name' , "email","adress", "phone_number",'is_active',"is_staff"]
    fieldsets = [
        ('import your informations' , {'fields' :['name' ,'email',"adress", "phone_number","password"] }),
        ('import user permission' , {'fields' : ["is_active"  , "is_staff" ]}),
         ]
    search_fields=['email','name']



