from django.urls import path, re_path
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('managecreds/', views.managecreds, name='managecreds'),
    path('createpost/', views.createpost, name='createpost'),
    path('listscheduled/', views.listscheduled, name='listscheduled'),
    #path('editpost/', views.editpost, name='editpost'),
    path('editpost/editpost<int:value>', views.editpost, name='editpost'),
    path('editpost/deletepost<int:value>', views.deletepost, name='deletepost'),
    path('listcompleted/', views.listcompleted, name='listcompleted'),
]

