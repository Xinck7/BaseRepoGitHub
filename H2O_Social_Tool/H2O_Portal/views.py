from django.contrib.auth import login as auth_login, authenticate
from django.shortcuts import render, redirect
from H2O_Portal.models import *
from H2O_Portal.forms import SignUpForm#, LoginForm
# Create your views here.

def home(request):
    all_posts = Post.objects.all()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            return redirect('')
    else:
        form = SignUpForm()
        # if form.is_valid():
        #     username = form.cleaned_data.get('username')
        #     raw_password = form.cleaned_data.get('password1')
        #     auth_login(request, user)
        #     return redirect('')    
    return render(request, 'H2O_Portal/base.html', {'Posts': all_posts, 'form':form })

def Signup(request):
    if request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        auth_login(request, user)
        return redirect('')
    else:
        form = SignUpForm()

def LoginUser(request):
    pass

def CreatePost(request):
    pass

def ListScheduled(request):
    pass

def ListCompleted(request):
    pass


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
    

