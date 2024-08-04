from django.db import models
from django.core import validators

# Create your models here.

class Customer(models.Model):
    class Meta:
        verbose_name_plural = "مشتری ها"
        verbose_name = " مشتری"

    first_name = models.CharField(max_length=100 , verbose_name="نام")
    last_name = models.CharField(max_length=100 , verbose_name=" نام خانوادگی")
    email = models.CharField(max_length=100,verbose_name="ایمیل" ,null=True , unique=True)
    password=models.CharField(max_length=100 ,verbose_name="رمز عبور")
    adress=models.CharField(max_length=250 ,verbose_name="آدرس", blank=True,null=True )
    phone_number=models.BigIntegerField(verbose_name="شماره تماس",null=True , unique=True,
                                        
                                        validators=[
                                            validators.RegexValidator(r'^989[0-3,9]\d{8}$',
                                                                      ('enter a valid mobile number. '),
                                            )
                                        ],
                                        error_messages={
                                            'unique':(" A user with this mobile number already exists."),
                                        }
                                        
                                        )
#    is_staff=models.BooleanField(verbose_name="کاربر ادمین", default=True , 
#                                  help_text=("Designates wether this user can log into this admin site .")
#                                 )
    def __str__(self):
        return f'{self.first_name}, {self.last_name}'





