from django.urls import path , include

from . import views
from rest_framework.routers import DefaultRouter

router1 = DefaultRouter()
router1.register('', views.CategoryViewSet)

router2 = DefaultRouter()
router2.register('', views.ProductViewSet)


urlpatterns = [

    path('category/',include(router1.urls)),
    path('product/',include(router2.urls), name='product'),

]