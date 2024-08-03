from django.urls import path , include

from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', views.CustomerViewSet)


urlpatterns = [

    path('Customer/',include(router.urls))

]
