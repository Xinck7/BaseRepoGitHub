from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User, models
from .models import SocialPost, SocialAccount

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
        }
        fields = ('title', 'post_time', 'message', 'picture', 'Facebook', 'Instagram', 'GroupMe')
     # https://tutorial.djangogirls.org/en/django_forms/

# class ManageCredentialForm(User):
#     class Meta:
#         model = SocialAccount
#         widgets = {
#             'myfield': forms.TextInput(attrs={'class': 'myfieldclass'}),
#         }
#         fields = ('username', 'password', 'account_type' )