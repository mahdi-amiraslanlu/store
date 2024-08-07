from django.urls import path , include

from . import views
from rest_framework.routers import DefaultRouter

router= DefaultRouter()
router.register('', views.CustomerUserViewSet)


urlpatterns = [

    path('customer/<user_id>',include(router.urls)),
]


