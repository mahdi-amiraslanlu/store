from django.db import models
from apps.users.models import Customer
from apps.products.models import Product
from apps.financial.models import Shipment,Payment
from extentions.utils import jalali_convertor


class Order(models.Model):
    class Meta:
        verbose_name = " سفارش "
        verbose_name_plural = "سفارشات"
        ordering = ["-order_date"]

    shipment = models.ForeignKey( Shipment ,on_delete=models.CASCADE,null=True , blank=True, verbose_name=" حمل و نقل ")
    payment = models.ForeignKey( Payment ,on_delete=models.CASCADE , null=True, verbose_name=" پرداخت ")
    customer = models.ForeignKey( Customer ,on_delete=models.CASCADE,null=True, verbose_name=" مشتری ")
    order_date = models.DateTimeField(auto_now_add=True ,verbose_name="زمان سفارش")
    total_price = models.DecimalField(max_digits=10 , decimal_places=2,verbose_name="قیمت کل" , null=True)

    def __str__(self):
        return self.customer.name
    
    def jorder_date(self):
        return jalali_convertor(self.order_date)
    jorder_date.short_description="زمان سفارش"

    
class Order_Item(models.Model):

    class Meta:
        verbose_name = " آیتم سفارش"
        verbose_name_plural = "آیتم های سفارشات"

    product = models.ForeignKey( Product ,on_delete=models.CASCADE , blank=True , null=True, verbose_name=" محصولات ")
    order = models.ForeignKey(Order  , on_delete=models.CASCADE , blank=True , null=True, verbose_name=" سفارشات ")
    quantity = models.IntegerField( verbose_name=" تعداد ")
    price = models.DecimalField(max_digits=10 , decimal_places=2 , verbose_name= "قیمت ",null=True)

    def __str__(self) -> str:
        return super().__str__()
    
class Wishlist(models.Model):
    class Meta:
        verbose_name = " علاقه مندی "
        verbose_name_plural = "علاقه مندی ها "
    product = models.ForeignKey( Product ,on_delete=models.CASCADE,blank=True,null=True, verbose_name=" محصولات ")    
    
    def __str__(self):
        return self.product.description

class Cart(models.Model):

    class Meta:
        verbose_name = " کارت"
        verbose_name_plural = " کارت ها "

    customer = models.ForeignKey( Customer ,on_delete=models.CASCADE,null=True, verbose_name="مشتری ها ")
    product = models.ForeignKey( Product ,on_delete=models.CASCADE,null=True, verbose_name=" محصولات ")
    quantity = models.IntegerField(verbose_name="تعداد",null=True)

    def __str__(self):
        return self.customer.name
    


