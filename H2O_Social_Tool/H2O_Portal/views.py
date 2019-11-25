from django.contrib.auth import login as auth_login, authenticate
from django.shortcuts import render, redirect
from H2O_Portal.models import *
from H2O_Portal.forms import SignUpForm #, LoginForm
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


def managecreds(request):
    return render(request, 'H2O_Portal/managecreds.html')


def createpost(request):
    return render(request, 'H2O_Portal/createpost.html')


def listscheduled(request):
    all_posts = Post.objects.all()
    return render(request, 'H2O_Portal/listscheduled.html', {'Posts': all_posts } )


def listcompleted(request):
    all_posts = Post.objects.all()
    return render(request, 'H2O_Portal/listcompleted.html' ,{'Posts': all_posts } )


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
    

