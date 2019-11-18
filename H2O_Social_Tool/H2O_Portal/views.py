from django.shortcuts import render
from django.template import context, loader
from H2O_Portal.models import *

# Create your views here.

def home(request):
    return render(request, 'base.html')

def post(request):
    posts = Post.objects.all()
    return render(request, 'SchPost.html', {'Posts': posts})

