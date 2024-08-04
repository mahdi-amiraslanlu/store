from django.urls import path , include

from .views import CustomerView ,GetTokenView

urlpatterns = [

    path('Get-Token/' ,GetTokenView.as_view() ),
    path('Customer/' ,CustomerView.as_view() ),
]


