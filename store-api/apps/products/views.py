from django.shortcuts import render
from rest_framework import viewsets

from .models import Category,Product
from .serializers import CategorySerializer,ProductSerializer

# Create your views here.

#region order viewset

class CategoryViewSet(viewsets.ModelViewSet):
        
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

#endregion


#region order viewset

class ProductViewSet(viewsets.ModelViewSet):
        
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

#endregion

