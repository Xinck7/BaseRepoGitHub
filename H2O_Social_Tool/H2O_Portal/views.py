from django.shortcuts import render, HttpResponse
from django.template import context, loader
from H2O_Portal.models import *

# Create your views here.

#def home(request):
#    return render(request, 'base.html')

def home(request):
    all_posts = Post.objects.all()
    posts_titles = list()
    for post in all_posts:
        posts_titles.append(post.title)
    response_html = '<br>'.join(posts_titles)
    return HttpResponse(response_html) 
    #return render(request, 'SchPost.html', {'Posts': posts})
    #return render(request, 'base.html')

