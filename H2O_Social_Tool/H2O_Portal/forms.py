from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import models
from .models import SocialPost, User, GroupMePosts#, SocialAccount

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
        widgets = {
            'myfield': forms.TextInput(attrs={'class': 'myfieldclass'}),
            'myfield2': forms.FileInput(attrs={'class':'imageclass'}),
        }
        fields = ('message', 'post_time', 'picture', 'Facebook', 'GroupMe')

class TokenStoreForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('gm_auth_token',)



