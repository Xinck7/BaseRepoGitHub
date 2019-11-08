from django.shortcuts import render
from django.template import context, loader

# Create your views here.

def home(request):
    return render(request, 'H2O_Portal/base.html')


