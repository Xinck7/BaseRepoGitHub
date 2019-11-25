from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    # path('login/', views.loginuser, name='loginuser' ),
    # path('managecreds/', views.creds, name='managecreds'),
    # path('createpost/', views.createpost, name='createpost'),
    path('listscheduled/', views.listscheduled, name='listscheduled'),
    path('listcompleted/', views.listcompleted, name='listcompleted'),
]

