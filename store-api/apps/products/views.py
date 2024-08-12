from rest_framework import request
from rest_framework import generics , mixins

from .models import Category,Product
from .serializers import CategorySerializer,ProductSerializer

# Create your views here.

class CategoryApiView(mixins.ListModelMixin ,generics.GenericAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self , request:request):
        return self.list(request)
    

class ProductApiView(mixins.ListModelMixin ,generics.GenericAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self , request:request):
        return self.list(request)


