from rest_framework import serializers
from .models import Category,Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']
        


class ProductSerializer(serializers.HyperlinkedModelSerializer):

    category = CategorySerializer()

    class Meta:
        model = Product
        fields =['category','sku','description','price','stock' , 'url']
