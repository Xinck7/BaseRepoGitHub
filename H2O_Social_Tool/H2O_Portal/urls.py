from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='H2O-Home'),
    path('Credentials/', views.Credentials, name='StoredCredentials'),
    path('Posts/', views.Post, name='Posts')
]

