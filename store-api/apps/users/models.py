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

    name = models.CharField(max_length=200 , verbose_name="نام")
    email = models.CharField(max_length=100,verbose_name="ایمیل" ,null=True , unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]


    def __str__(self):
        return self.name






#c#lass Customer(models.Model):
#    class Meta:
#        verbose_name_plural = "مشتری ها"
#        verbose_name = " مشتری"

 #   first_name = models.CharField(max_length=100 , verbose_name="نام")
 #   last_name = models.CharField(max_length=100 , verbose_name=" نام خانوادگی")
 #   email = models.CharField(max_length=100,verbose_name="ایمیل" ,null=True , unique=True)
 #   password=models.CharField(max_length=100 ,verbose_name="رمز عبور")
 #   adress=models.CharField(max_length=250 ,verbose_name="آدرس", blank=True,null=True )
 #   phone_number=models.BigIntegerField(verbose_name="شماره تماس",null=True , unique=True,
                                        
 #                                       validators=[
 #                                           validators.RegexValidator(r'^989[0-3,9]\d{8}$',
 #                                                                     ('enter a valid mobile number. '),
 #                                           )
#                                        ],
 #                                       error_messages={
 #                                           'unique':(" A user with this mobile number already exists."),
 #                                       }
 #                                       
 #                                       )
#    is_staff=models.BooleanField(verbose_name="کاربر ادمین", default=True , 
#                                  help_text=("Designates wether this user can log into this admin site .")
#                                 )


  #  def __str__(self):
  #      return f'{self.first_name} {self.last_name}'
    





