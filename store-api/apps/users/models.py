from django.db import models
from django.contrib.auth.models import AbstractUser 

# Create your models here.

class CustomerUser(AbstractUser): 
    class Meta:
        verbose_name_plural = " مدیریت ادمین "
        verbose_name = "کاربر"

    email = models.EmailField(verbose_name="ایمیل", unique=True,null=True )
    phone_number=models.BigIntegerField(verbose_name="شماره تماس",null=True )
#    otp=models.CharField(max_length=6 , null=True , blank=True)
    is_verified = models.BooleanField(default=False)
    user_permissions=None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS=['username']

    def __str__(self):
        return self.username


class Customer(models.Model):
    class Meta:
        verbose_name_plural = "مشتری ها"
        verbose_name = "مشتری"

    user = models.OneToOneField(CustomerUser , on_delete=models.CASCADE , verbose_name="مشتری",null=True)
    adress=models.CharField(max_length=250 ,verbose_name="آدرس", blank=True,null=True )

#    phone_number=models.BigIntegerField(verbose_name="شماره تماس",null=True )
#    first_name = models.CharField(max_length=50 , null=True , verbose_name="نام")
#    last_name = models.CharField(max_length=100 , null=True , verbose_name=" نام خانوادگی")
#    email = models.EmailField(verbose_name="ایمیل", unique=True,null=True )
#    phone_number=models.BigIntegerField(verbose_name="شماره تماس",null=True )

    def __str__(self):
        return self.user.username 
    

