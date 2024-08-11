from rest_framework import serializers
from .models import CustomerUser ,Customer

class CustomerUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerUser
        fields = "__all__" 


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ["name", 'email' , 'password','adress','phone_number']


