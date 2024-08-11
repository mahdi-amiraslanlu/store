from django.urls import path , include

from . import views


urlpatterns = [

    path  ('category/', views.CategoryApiView.as_view()),
    path  ('product/', views.ProductApiView.as_view()),

]