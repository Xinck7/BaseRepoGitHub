from django.urls import path
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
    path(r'^editpost/(?P<post_to_edit>\d+)/$', views.editpost, name='editpost'),
    path('listcompleted/', views.listcompleted, name='listcompleted'),
]

