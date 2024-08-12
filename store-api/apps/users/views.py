from rest_framework.permissions import  IsAdminUser , IsAuthenticated ,AllowAny
from apps.users.permissions import IsCustomer 
from rest_framework import viewsets
from .models import CustomerUser , Customer
from .serializers import CustomerUserSerializer ,CustomerSerializer 

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class CustomerUserViewSet(viewsets.ModelViewSet):
    permission_classes=(IsAdminUser,)
    queryset = CustomerUser.objects.all()
    serializer_class = CustomerUserSerializer
    filterset_fields = ["is_active" , "is_verified"]


class CustomerViewSet(viewsets.ModelViewSet): 
    permission_classes=(IsCustomer,IsAuthenticated )
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


# class RegisteAPI(APIView):
#     permission_classes = (AllowAny,)

#     def post(self , request):
#         try:
#             data = request.data
#             serializer = CustomerUserSerializer(data=data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response({
#                     'status':200 ,
#                     'message' : "registration successfilly check email",
#                     'data' : serializer.data ,
#                 })
            
#             return Response({
#                 'status' : 400 , 
#                 'message': "something went wrong",
#                 'data' : serializer.errors
#             })
#         except Exception as e :
#             print(e)

            





