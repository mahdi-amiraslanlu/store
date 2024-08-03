from django.shortcuts import render
from rest_framework import viewsets

from .models import Customer
from .serializers import CustomerSerializer
# Create your views here.


#region order viewset

class CustomerViewSet(viewsets.ModelViewSet):
        
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

#endregion
