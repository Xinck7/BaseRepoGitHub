from django.shortcuts import render
from django.template import context, loader
from django.http import HttpResponse

def home(request):
    return render(request, 'H2O_Portal/base.html')
    #return render(request, 'H2O_Portal/Social_Tool.html')


# Create your views here.
