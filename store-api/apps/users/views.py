
from rest_framework import viewsets 
from rest_framework.permissions import IsAuthenticated

from .models import Customer
from .serializers import CustomerSerializer
# Create your views here.


class CustomerViewSet(viewsets.ModelViewSet):
        
    queryset = Customer.objects.filter()
    serializer_class = CustomerSerializer
    permission_classes = (IsAuthenticated,)


#class CustomerView(APIView):

#    def post(self , request):
#        email=request.data.get("email")

#        if not email:
#            return response(status=status.HTTP_400_BAD_REQUEST)
        
#        try:
#            customer=Customer.objects.get(email=email)
#            return response({'detail':'user already registerd!' } , 
#                            status=status.HTTP_400_BAD_REQUEST)
#        except Customer.DoesNotExist:
#            costumer=Customer.object.create(email=email)

        #Customer,created = Customer.oblect.get_or_create(email=email)

#        code=random.randint(10000, 99999)

        #save code in customer model 
        #send massage email   with  api panel  or save in cash memory

#        cache.set(int(email) , code, 2*60 )

#        return response({'code' : code})


#class GetTokenView(APIView):

#    def get(self,request):
#        email=request.data.get("email")
#        code = request.data.get(code)

#        cached_code = cache.get(int(email))

#        if code != cached_code:
#            return response(status=status.HTTP_403_FORBIDDEN)
        
#        token = str(uuid.uuid4())

#        return response({'token' : token})


