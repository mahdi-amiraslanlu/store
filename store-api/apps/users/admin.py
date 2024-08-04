from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display =[ 'first_name' , "last_name" , "email" , "phone_number" ]
    fieldsets = [
        ('import your informations' , {'fields' :['first_name' , 'last_name','email','phone_number' , 'adress'] }),
    ]
    search_fields=['email']

    


