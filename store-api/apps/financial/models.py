from django.db import models

from apps.users.models import Customer
# Create your models here.

class Shipment(models.Model):
    class Meta:
        verbose_name = "حمل و نقل"

    customer = models.ForeignKey(Customer ,on_delete=models.CASCADE,null=True)
    shipment_date = models.DateField(auto_now_add=True , verbose_name="زمان ارسال",null=True)
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

    customer = models.ForeignKey( Customer ,on_delete=models.CASCADE,null=True)
    payment_date = models.DateTimeField(auto_now_add=True , verbose_name="زمان پرداخت")
    Payment_meto = models.CharField(max_length=100 , verbose_name="متد پرداختی",null=True,blank=True)
    amount = models.DecimalField(max_digits=10 , decimal_places=2 , verbose_name="مبلغ", blank=True,null=True)
    
    def __str__(self):
        return self.customer.last_name
    
    