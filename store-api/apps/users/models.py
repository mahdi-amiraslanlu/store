from django.db import models

# Create your models here.

class Customer(models.Model):
    class Meta:
        verbose_name_plural = "مشتری ها"
        verbose_name = " مشتری"

    first_name = models.CharField(max_length=100 , verbose_name="نام")
    last_name = models.CharField(max_length=100 , verbose_name=" نام خانوادگی")
    email = models.CharField(max_length=100,verbose_name="ایمیل" ,null=True)
    password=models.CharField(max_length=100 ,verbose_name="رمز عبور")
    adress=models.CharField(max_length=250 ,verbose_name="آدرس", blank=True,null=True )
    phone_number=models.CharField(max_length=20 , verbose_name="شماره تماس",blank=True,null=True)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'

