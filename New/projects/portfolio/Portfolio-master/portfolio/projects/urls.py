from django.urls import path
from . import views

urlpatterns = [
    path('',views.project,name = "project"),
    path('articles', views.article,name = "article"),
    path('paintings',views.paintings,name = "painting")
]