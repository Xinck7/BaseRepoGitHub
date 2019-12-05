from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import models
from .models import SocialPost, User#, SocialAccount

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254)
    class Meta:
        model = User
        widgets = {
            'myfield': forms.TextInput(attrs={'class': 'myfieldclass'}),
        }
        fields = ('username', 'password1', 'password2', 'email')

class SocialPostForm(forms.ModelForm):
    class Meta:
        model = SocialPost
        model.post_time = forms.DateField(required=False)
        widgets = {
            'myfield': forms.TextInput(attrs={'class': 'myfieldclass'}),
            'myfield2': forms.FileInput(attrs={'class':'imageclass'}),
        }
        fields = ('title', 'post_time', 'message', 'picture', 'Facebook', 'Instagram', 'GroupMe')


