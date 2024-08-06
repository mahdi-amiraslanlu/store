from django.db import models

# Create your models here.
    
class Category(models.Model):
    class Meta:
        verbose_name_plural = " دسته بندی ها"
        verbose_name = "دسته بندی"

    name = models.CharField(max_length=100, verbose_name="نام", blank= False)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):

    class Meta:
        verbose_name_plural =  "محصولات"
        verbose_name = "محصول"

    category = models.ForeignKey(Category, on_delete=models.CASCADE , verbose_name="دسته بندی" )
    sku = models.CharField(max_length=100 ,verbose_name="بارکد" , blank=True , null=True)
    description = models.CharField(max_length=100 ,blank=True,null=True ,verbose_name = "تعریف محصول" )
    price = models.DecimalField(max_digits=10 , decimal_places=2,verbose_name="قیمت" )
    stock = models.IntegerField(verbose_name="موجودی",blank=True , null=True)

    def __str__(self):
        return self.description
