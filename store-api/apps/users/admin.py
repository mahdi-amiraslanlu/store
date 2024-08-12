from django.contrib import admin
from . import models
from .models import CustomerUser
# Register your models here.


class CustomUserAdmin(admin.ModelAdmin):

    list_display =["username","is_staff","is_verified", "email","password","phone_number"]
    fieldsets = [
         ('import your informations',{'fields':["username", "first_name","last_name"
                                                 ,"password", "email","phone_number"] }),
         ('import user permission' , {'fields' : ["is_verified","is_staff","is_superuser" ]}),
      ]
    search_fields=['username','email']
admin.site.register(CustomerUser , CustomUserAdmin)


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin): 

    list_display =[ "adress","user"]
    # fieldsets = [
    #    ('import your informations' , {'fields' :['name' ,'email',"adress", "phone_number","password"] }),
    #    ('import user permission' , {'fields' : ["is_active"  , "is_staff" ]}),
    #     ]
    # search_fields=['email','name']



