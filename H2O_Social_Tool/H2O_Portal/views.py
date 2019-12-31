from django.contrib.auth import login as auth_login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from H2O_Portal.models import *
from H2O_Portal.forms import *
import json

# from allauth import account, socialaccount
# Create your views here.

def home(request):
    return render(request, 'H2O_Portal/base.html')

@login_required
def pagehome(request):
    return render(request, 'H2O_Portal/pagehome.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)            
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            return redirect('pagehome')
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
            post.gm_auth_token = form.cleaned_data.get('gm_auth_token')
            post.save()
            return redirect('pagehome')
    else:
        form = TokenStoreForm(instance=socialuser)
    return render(request, 'H2O_Portal/managecreds.html', {'form' : form} )    
    # try:
    #     facebook_login = socialaccount.objects.filter(provider='facebook', user_id=self.user.id)#sociallogin.account.provider #user.social_auth.get(provider='facebook')
    # except:# UserSocialAuth.DoesNotExist:
    #     facebook_login = None

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
        socialuser = request.user
        init_groupme = GroupMePosts()
        master_groups = GroupMePosts.getgroups(init_groupme, socialuser.gm_auth_token)
        reversed_groupme_groups = dict(request.POST)
        gm_list = []
        list_groupme_groups = reversed_groupme_groups.values()
        for var_groups in list_groupme_groups:
            for var_group in var_groups:
                for group in master_groups:
                    if var_group == group.name:
                        gm_list.append(var_group)

        if form.is_valid():
            post = form.save(commit=False)
            #add cleaning data
            post.GroupMeGroups = gm_list 
            post.updated_by = request.user
            post.save()
            return redirect('listscheduled')
    else:
        socialuser = request.user
        init_groupme = GroupMePosts()
        groups = GroupMePosts.getgroups(init_groupme, socialuser.gm_auth_token)
        form = SocialPostForm()
    return render(request, 'H2O_Portal/createpost.html', {'form' : form, 'groups': groups} )

@login_required
def editpost(request, value):
    user_posts = SocialPost.objects.filter(id=value).first()
    if request.method == 'POST':
        form = SocialPostForm(request.POST, request.FILES, instance=user_posts)
        socialuser = request.user
        init_groupme = GroupMePosts()
        master_groups = GroupMePosts.getgroups(init_groupme, socialuser.gm_auth_token)
        reversed_groupme_groups = dict(request.POST)
        gm_list = []
        list_groupme_groups = reversed_groupme_groups.values()
        for var_groups in list_groupme_groups:
            for var_group in var_groups:
                for group in master_groups:
                    if var_group == group.name:
                        gm_list.append(var_group)

        if form.is_valid(): 
            post = form.save(commit=True)
            #add cleaning data
            post.GroupMeGroups = gm_list 
            post.updated_by = request.user
            post.save()
            return redirect('listscheduled')
    else:
        socialuser = request.user
        init_groupme = GroupMePosts()
        groups = GroupMePosts.getgroups(init_groupme, socialuser.gm_auth_token)
        form = SocialPostForm(instance=user_posts)
    return render(request, 'H2O_Portal/editpost.html', {'Post' : user_posts, 'form' : form, 'groups': groups })

@login_required
def deletepost(request, value):
    user_post = SocialPost.objects.filter(id=value)
    user_post.delete()
    return redirect('listscheduled')

@login_required
def listscheduled(request):
    all_posts = SocialPost.objects.all().order_by('post_time')
    all_posts= all_posts.filter(completed=False)
    paginator = Paginator(all_posts, 10)
    page = request.GET.get('page' , 1)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'H2O_Portal/listscheduled.html', {'Posts': posts } )


@login_required
def listcompleted(request):
    all_posts = SocialPost.objects.all().order_by('-post_time')
    all_posts_filtered= all_posts.filter(completed=True)
    paginator = Paginator(all_posts_filtered, 10)
    page = request.GET.get('page' , 1)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'H2O_Portal/listcompleted.html', {'Posts': posts } )



