from django.urls import path , include

from . import views
from rest_framework.routers import DefaultRouter

router1 = DefaultRouter()
router1.register('', views.ShipmentViewSet)

router2 = DefaultRouter()
router2.register('', views.PaymentViewSet)

urlpatterns = [

    path('Shipment/',include(router1.urls)),
    path('Payment/',include(router2.urls)),

]

