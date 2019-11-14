from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='H2OHome'),
    path('Posts/', views.post, name='posts')
    #path('Credentials/', views.Credentials, name='StoredCredentials'),
    #path('Posts/', views.Post, name='Posts')
]

