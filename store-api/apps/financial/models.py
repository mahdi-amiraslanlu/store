from django.db import models
from django.utils import timezone

from apps.users.models import CustomerUser
from extentions.utils import jalali_convertor
# Create your models here.

class Shipment(models.Model):
    class Meta:
        verbose_name = "حمل و نقل"
        verbose_name_plural = " حمل و نقل ها "
    

    customer = models.ForeignKey(CustomerUser ,on_delete=models.CASCADE,null=True , verbose_name="مشتری ها ")
    shipment_date = models.DateField(auto_now_add=True, verbose_name="زمان ارسال")
    address = models.CharField(max_length=100 , verbose_name="آدرس")
    city =  models.CharField(max_length=100 , verbose_name="شهر",null=True)
    state = models.CharField(max_length=20 , verbose_name="استان",null=True)
    country = models.CharField(max_length=50 , verbose_name="کشور",null=True)
    zip_code = models.IntegerField( verbose_name="کد",null=True)

    def __str__(self):
        return self.customer.last_name
    
    
class Payment(models.Model):
    class Meta:
        verbose_name = "پرداخت"
        verbose_name_plural = "  پرداختها "

    customer = models.ForeignKey( CustomerUser ,on_delete=models.CASCADE,null=True, verbose_name="مشتری ها ")
    payment_date = models.DateTimeField(default=timezone.now , verbose_name="زمان پرداخت")
    Payment_meto = models.CharField(max_length=100 , verbose_name="متد پرداختی",null=True,blank=True)
    amount = models.DecimalField(max_digits=10 , decimal_places=2 , verbose_name="مبلغ", blank=True,null=True)
    
    def __str__(self):
        return self.customer.last_name
    
    def jpayment_date(self):
        return jalali_convertor(self.payment_date)
    jpayment_date.short_description = "زمان پرداخت"
    



    
    