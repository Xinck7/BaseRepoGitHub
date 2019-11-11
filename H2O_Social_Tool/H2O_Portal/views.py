from django.shortcuts import render
from django.template import context, loader
from H2O_Portal.models import *

# Create your views here.

def home(request):
    return render(request, 'H2O_Portal/base.html')

def post(request, title, post_time, text, picture):
    
