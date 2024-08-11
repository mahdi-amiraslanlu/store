from django.db import models
from django.contrib.auth.models import AbstractUser 
from django.contrib.auth.models import BaseUserManager

# Create your models here.


class UserAccountManager(BaseUserManager):
    def create_user(self,email,name,password=None):
        if not email:
            raise ValueError("user most have imail !")
        else:
            email = self.normalize_email(email)
            user = self.model(email = email , name=name)
            user.set_password(password)
            user.save()
            return user
    
    def create_superuser(self,email , name , password):
        user = self.create_user(email=email , name=name ,password=password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class CustomerUser(AbstractUser): 

    class Meta:
        verbose_name_plural = " مدیریت ادمین "
        verbose_name = "کاربر"

    name = models.CharField(max_length=200 , verbose_name="نام" , null=True)
    email = models.EmailField(verbose_name="ایمیل", unique=True )
    password=models.CharField(max_length=100 ,verbose_name="رمز عبور")
    adress=models.CharField(max_length=250 ,verbose_name="آدرس", blank=True,null=True )
    phone_number=models.BigIntegerField(verbose_name="شماره تماس",null=True )
    otp=models.CharField(max_length=6 , null=True , blank=True)

    is_verified=models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    username = None
    objects = UserAccountManager()
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def __str__(self):
        return self.name




class Customer(models.Model):

    class Meta:
        verbose_name_plural = "مشتری ها"
        verbose_name = "مشتری"

    customer = models.OneToOneField(CustomerUser , on_delete=models.CASCADE , verbose_name="مشتری",null=True)
    name = models.CharField(max_length=200 , verbose_name="نام" , null=True)
    email = models.EmailField(max_length=100,verbose_name="ایمیل", unique=True)
    password=models.CharField(max_length=100 ,verbose_name="رمز عبور")
    adress=models.CharField(max_length=250 ,verbose_name="آدرس", blank=True,null=True )
    phone_number=models.BigIntegerField(verbose_name="شماره تماس",null=True )
    username = None

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return self.name 
    

