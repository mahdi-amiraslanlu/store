from rest_framework import viewsets
from .permissions import IsCustomer
from rest_framework.permissions import IsAuthenticated
from .models import  Order,Order_Item,Wishlist,Cart
from .serializers import OrderSerializer , Order_ItemSerializer,WishlistSerializer,CartSerializer

#region order viewset

class OrderViewSet(viewsets.ModelViewSet):
        
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated,IsCustomer,)

#endregion


#region order_item viewset

class Order_ItemViewSet(viewsets.ModelViewSet):
        
    queryset = Order_Item.objects.all()
    serializer_class = Order_ItemSerializer
    permission_classes = (IsAuthenticated,IsCustomer,)

#endregion


#region washlist viewset

class WishlistViewSet(viewsets.ModelViewSet):
        
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    permission_classes = (IsAuthenticated,IsCustomer,)


#endregion


#region cart viewset

class CartViewSet(viewsets.ModelViewSet):
        
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = (IsAuthenticated,IsCustomer,)

#endregion


