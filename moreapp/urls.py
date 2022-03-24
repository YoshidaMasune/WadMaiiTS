from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('login/', views.signin),
    path('register/', views.register),
    path('createuser/', views.createuser),
    path('about/', views.about),
]
