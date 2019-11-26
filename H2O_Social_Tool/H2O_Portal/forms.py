from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, models
from .models import SocialPost

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
        model.post_time = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'] )
        widgets = {
            'myfield': forms.TextInput(attrs={'class': 'myfieldclass'}),
        }
        fields = ('title', 'post_time', 'message', 'picture', 'Facebook', 'Instagram', 'GroupMe')
     # https://tutorial.djangogirls.org/en/django_forms/