from django.shortcuts import render
from rest_framework import viewsets

from .models import Shipment , Payment
from .serializers import ShipmentSerializer , PaymentSerializer
# Create your views here.

#region viewset

class ShipmentViewSet(viewsets.ModelViewSet):
        
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer

#endregion


#region viewset

class PaymentViewSet(viewsets.ModelViewSet):
        
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

#endregion


