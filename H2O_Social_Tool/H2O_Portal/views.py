from django.contrib.auth import login as auth_login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from H2O_Portal.models import *
from H2O_Portal.forms import *
#from social_django.models import UserSocialAuth
from allauth import account, socialaccount
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
    try:
        facebook_login = socialaccount.objects.filter(provider='facebook', user_id=self.user.id)#sociallogin.account.provider #user.social_auth.get(provider='facebook')
    except:# UserSocialAuth.DoesNotExist:
        facebook_login = None
    try:
        instagram_login = socialaccount.objects.filter(provider='instagram', user_id=self.user.id)#user.social_auth.get(provider='instagram')
    except: #UserSocialAuth.DoesNotExist:
        instagram_login = None
    try:
        groupme_login = socialuser.gm_auth_token#user.social_auth.get(provider='groupme')
    except: 
        groupme_login = None

    can_disconnect =  socialaccount.forms.DisconnectForm #(user.social_auth.count() > 1)

    return render(request, 'H2O_Portal/managecreds.html', {
        'facebook_login': facebook_login,
        'instagram_login': instagram_login,
        'groupme_login': groupme_login,
        'can_disconnect': can_disconnect,
    })

# @login_required
# def managecreds(request):
#     if request.method == 'POST':
#         form = TokenStoreForm(request.POST)            
#         if form.is_valid():
#             token = form.save(commit=False)
#             token.save()
#             return redirect('/')
#         else:
#             form = TokenStoreForm()
#     return render(request, 'H2O_Portal/managecreds.html', {'form': form})

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
def listscheduled(request):
    all_posts = SocialPost.objects.all()
    return render(request, 'H2O_Portal/listscheduled.html', {'Posts': all_posts } )

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
        form = SocialPostForm()
    return render(request, 'H2O_Portal/editpost.html', {'Post' : user_posts, 'form' : form} )

@login_required
def deletepost(request, value):
    user = request.user
    user_post = SocialPost.objects.filter(id=value)
    user_post.delete()
    return redirect('listscheduled')

@login_required
def listcompleted(request):
    all_posts = SocialPost.objects.all()
    return render(request, 'H2O_Portal/listcompleted.html', {'Posts': all_posts } )


# https://api.groupme.com/v3/groups/:group_id/messages
# with a payload like:
# {
#    "message": {
#      "source_guid": "c8bf78dd-c17c-4d1d-9029-1689764436a1",
#      "text": "So text....."
#    }
# data = {"message":{"source_guid":"random_string","text":"message_to_send"}}
# send = requests.post("https://api.groupme.com/v3/groups/:group_id/message?token=my_access_token", json=data)
# print send.text
    

