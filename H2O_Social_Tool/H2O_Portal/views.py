from django.contrib.auth import login as auth_login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from H2O_Portal.models import *
from H2O_Portal.forms import *

# from allauth import account, socialaccount
# Create your views here.

def home(request):
    return render(request, 'H2O_Portal/base.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)            
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()

    return render(request, 'H2O_Portal/signup.html', {'form' : form} )

@login_required
def managecreds(request):
    socialuser = request.user
    if request.method == 'POST':
        form = TokenStoreForm(request.POST, instance=socialuser)            
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('/')
    else:
        form = TokenStoreForm(instance=socialuser)
    return render(request, 'H2O_Portal/managecreds.html', {'form' : form} )    
    # try:
    #     facebook_login = socialaccount.objects.filter(provider='facebook', user_id=self.user.id)#sociallogin.account.provider #user.social_auth.get(provider='facebook')
    # except:# UserSocialAuth.DoesNotExist:
    #     facebook_login = None
    # try:
    #     groupme_login = socialuser.gm_auth_token#user.social_auth.get(provider='groupme')
    # except: 
    #     groupme_login = None

    # can_disconnect =  socialaccount.forms.DisconnectForm #(user.social_auth.count() > 1)

    # return render(request, 'H2O_Portal/managecreds.html', {
    #     'facebook_login': facebook_login,
    #     'groupme_login': groupme_login,
    #     'can_disconnect': can_disconnect,
    # })

@login_required
def createpost(request):
    if request.method == 'POST':
        form = SocialPostForm(request.POST, request.FILES)            
        if form.is_valid():
            post = form.save(commit=False)
            post.updated_by = request.user
            post.save()
            return redirect('listscheduled')
    else:
        form = SocialPostForm()
    return render(request, 'H2O_Portal/createpost.html', {'form' : form} )


@login_required
def editpost(request, value):
    user_posts = SocialPost.objects.filter(id=value).first()
    if request.method == 'POST':
        form = SocialPostForm(request.POST, instance=user_posts)            
        if form.is_valid(): 
            post = form.save(commit=False)
            post.updated_by = request.user
            post.save()
            return redirect('listscheduled')
    else:
        form = SocialPostForm(instance=user_posts)
    return render(request, 'H2O_Portal/editpost.html', {'Post' : user_posts, 'form' : form})

@login_required
def deletepost(request, value):
    user = request.user
    user_post = SocialPost.objects.filter(id=value)
    user_post.delete()
    return redirect('listscheduled')

@login_required
def listscheduled(request):
    all_posts = SocialPost.objects.all()
    page = request.GET.get('page' , 1)
    paginator = Paginator(all_posts, 10)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    #return render(request, 'H2O_Portal/listscheduled.html', {'Posts': all_posts } )
    return render(request, 'H2O_Portal/listscheduled.html', {'Posts': posts } )


@login_required
def listcompleted(request):
    all_posts = SocialPost.objects.all()
    page = request.GET.get('page' , 1)
    paginator = Paginator(all_posts, 10)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'H2O_Portal/listcompleted.html', {'Posts': all_posts } )



