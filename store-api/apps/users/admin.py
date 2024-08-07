from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.CustomerUser)
class CustomerUserAdmin(admin.ModelAdmin):
    list_display =[ 'name' , "email" ]
    fieldsets = [
        ('import your informations' , {'fields' :['name' ,'email'] }),
    ]
    search_fields=['email','name']

    
