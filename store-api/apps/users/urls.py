from django.urls import path , include

from . import views
from rest_framework.routers import DefaultRouter
#from .views import RegisteAPI

router1= DefaultRouter()
router1.register('', views.CustomerUserViewSet)

router2= DefaultRouter()
router2.register('', views.CustomerViewSet)



urlpatterns = [

    path('customeruser/',include(router1.urls)),
    path('customer/',include(router2.urls)),
#    path('register/' , RegisteAPI.as_view()),
]


