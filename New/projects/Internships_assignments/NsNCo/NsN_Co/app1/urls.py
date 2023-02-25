from django.urls import path
from . import  views

urlpatterns = [
    path('',views.home,name="app1-home"),
    path('register/',views.register,name="app1-register")
]