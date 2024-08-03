from rest_framework import serializers
from .models import Order,Order_Item,Wishlist,Cart



class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__" 


class Order_ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order_Item
        fields = "__all__" 


class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = "__all__" 


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"   


