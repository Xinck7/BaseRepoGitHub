from django.shortcuts import render
from django.template import context, loader
from H2O_Portal.models import *

# Create your views here.

def home(request):
    return render(request, 'H2O_portal/base.html')

def post(request):
    posts = Post.objects.all()
    post_titles = list()

    for post in posts:
        post_titles.append(Post.title)
    
    response_html = '<br>'.join(post_titles)
    return render(request, 'H2O_portal/SchPost.html')

