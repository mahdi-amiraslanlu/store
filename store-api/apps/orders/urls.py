from django.urls import path , include

from . import views
from rest_framework.routers import DefaultRouter

router1 = DefaultRouter()
router1.register('', views.OrderViewSet)

router2 = DefaultRouter()
router2.register('', views.Order_ItemViewSet)

router3 = DefaultRouter()
router3.register('', views.WishlistViewSet)

router4 = DefaultRouter()
router4.register('', views.CartViewSet)

urlpatterns = [

    path('Order/',include(router1.urls)),
    path('Order_Item/',include(router2.urls)),
    path('Wishlist/',include(router3.urls)),
    path('Cart/',include(router4.urls)),
]



