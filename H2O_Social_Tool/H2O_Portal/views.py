from django.shortcuts import render
from django.template import context, loader
from django.http import HttpResponse

def home(request):
    context = {}
    return render(request, 'H2O_Portal/base.html', context)
    #return render(request, 'H2O_Portal/Social_Tool.html')


# Create your views here.
