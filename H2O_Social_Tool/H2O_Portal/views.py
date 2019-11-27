from django.contrib.auth import login as auth_login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from H2O_Portal.models import *
from H2O_Portal.forms import *

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
    # if request.method == 'POST':
    #     form = ManageCredentialForm(request.POST)            
    #     if form.is_valid():
    #         post = form.save(commit=False)
    #         post.author = request.user
    #         post.save()
    #         return redirect('/')
    # else:
    #     form = ManageCredentialForm()    
    return render(request, 'H2O_Portal/managecreds.html')#, {'form' : form})

@login_required
def createpost(request):
    if request.method == 'POST':
        form = SocialPostForm(request.POST)            
        if form.is_valid():
            post = form.save(commit=False)
            post.updated_by = request.user
            post.save()
            return redirect('/')
    else:
        form = SocialPostForm()
    return render(request, 'H2O_Portal/createpost.html', {'form' : form} )

@login_required
def listscheduled(request):
    all_posts = SocialPost.objects.all()
    return render(request, 'H2O_Portal/listscheduled.html', {'Posts': all_posts } )

@login_required
def editpost(request, post_to_edit):
    #need title drop down
    user = request.user
    user_posts = SocialPost.objects.filter(updated_by=user, id=post_to_edit)
    return render(request, 'H2O_Portal/editpost.html', {'Posts' : user_posts})

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
    

