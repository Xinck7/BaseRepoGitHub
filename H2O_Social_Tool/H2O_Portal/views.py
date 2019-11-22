from django.shortcuts import render
from django.template import loader
from H2O_Portal.models import *

# Create your views here.

#def home(request):
#    return render(request, 'base.html')

def home(request):
    all_posts = Post.objects.all()
    return render(request, 'H2O_Portal/base.html', {'Posts': all_posts })

    #posts_titles = list()
    #for post in all_posts:
    #    posts_titles.append(post.title)
    #response_html = '<br>'.join(posts_titles)
    #return HttpResponse(response_html) 
    #return render(request, 'SchPost.html', {'Posts': posts})
    

