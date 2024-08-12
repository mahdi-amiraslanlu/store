from rest_framework import serializers
from .models import Category,Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']
        


class ProductSerializer(serializers.ModelSerializer):
    def get_category(self,obj):
        return obj.category.name

    category = serializers.SerializerMethodField("get_category")

    class Meta:
        model = Product
        fields ="__all__"



