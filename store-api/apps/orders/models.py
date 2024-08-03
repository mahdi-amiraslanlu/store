from django.db import models
from apps.users.models import Customer
from apps.products.models import Product
from apps.financial.models import Shipment,Payment

class Order(models.Model):
    class Meta:
        verbose_name_plural = "سفارشات"
        verbose_name = " سفارش "

    shipment = models.ForeignKey( Shipment ,on_delete=models.CASCADE,null=True , blank=True)
    payment = models.ForeignKey( Payment ,on_delete=models.CASCADE , null=True)
    customer = models.ForeignKey( Customer ,on_delete=models.CASCADE,null=True)
    order_date = models.DateTimeField(auto_now_add=True ,verbose_name="زمان سفارش")
    total_price = models.DecimalField(max_digits=10 , decimal_places=2,verbose_name="قیمت کل" , null=True)

    def __str__(self):
        return self.customer.last_name
    
class Order_Item(models.Model):

    class Meta:
        verbose_name_plural = "آیتم های سفارشات"
        verbose_name = " آیتم سفارش"

    product = models.ForeignKey( Product ,on_delete=models.CASCADE , blank=True , null=True)
    order = models.ForeignKey(Order  , on_delete=models.CASCADE , blank=True , null=True)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10 , decimal_places=2 , verbose_name= "قیمت ",null=True)

    def __str__(self):
        return self.product.description
    
class Wishlist(models.Model):
    class Meta:
        verbose_name = " علاقه مندی ها"
    product = models.ForeignKey( Product ,on_delete=models.CASCADE,blank=True,null=True)    
    
    def __str__(self):
        return self.product.description

class Cart(models.Model):

    class Meta:
        verbose_name = " کارت"

    customer = models.ForeignKey( Customer ,on_delete=models.CASCADE,null=True)
    product = models.ForeignKey( Product ,on_delete=models.CASCADE,null=True)
    quantity = models.IntegerField(verbose_name="تعداد",null=True)

    def __str__(self):
        return self.customer.first_name
    


