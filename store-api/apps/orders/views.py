from django.shortcuts import render
from rest_framework import viewsets

from .models import  Order,Order_Item,Wishlist,Cart
from .serializers import OrderSerializer , Order_ItemSerializer,WishlistSerializer,CartSerializer

#region order viewset

class OrderViewSet(viewsets.ModelViewSet):
        
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

#endregion


#region order_item viewset

class Order_ItemViewSet(viewsets.ModelViewSet):
        
    queryset = Order_Item.objects.all()
    serializer_class = Order_ItemSerializer

#endregion


#region washlist viewset

class WishlistViewSet(viewsets.ModelViewSet):
        
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer

#endregion


#region cart viewset

class CartViewSet(viewsets.ModelViewSet):
        
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

#endregion


