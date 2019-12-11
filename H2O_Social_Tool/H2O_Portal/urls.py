from django.urls import path, re_path
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    #Credentials
    path('signup/', views.signup, name='signup'),
    path('managecreds/', views.managecreds, name='managecreds'),
    path('managecreds/gm_auth_token<str:value>', views.managecreds, name='editcreds'),    
    
    #Posts
    path('createpost/', views.createpost, name='createpost'),
    path('createpostnoauth/', views.createpostnogroupmeauth, name='createpostnoauth'),
    path('editpost/editpost<int:value>', views.editpost, name='editpost'),
    path('editpost/deletepost<int:value>', views.deletepost, name='deletepost'),
    
    #All Post information
    path('listscheduled/', views.listscheduled, name='listscheduled'),
    path('listcompleted/', views.listcompleted, name='listcompleted'),
]

