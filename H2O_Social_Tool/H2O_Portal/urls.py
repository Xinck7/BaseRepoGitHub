from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.home, name='home')
    #path('Posts/', views.post, name='posts')
    #path('Credentials/', views.Credentials, name='StoredCredentials'),
    #path('Posts/', views.Post, name='Posts')
]

