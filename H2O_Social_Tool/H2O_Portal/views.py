from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from H2O_Portal.models import Post
from H2O_Portal.forms import SignUpForm
# Create your views here.

def home(request):
    all_posts = Post.objects.all()
    #all_users = Webusers.objects.all()
    return render(request, 'H2O_Portal/base.html', {'Posts': all_posts })

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

    

