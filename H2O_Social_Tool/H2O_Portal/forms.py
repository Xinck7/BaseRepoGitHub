from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import models
from django.forms import widgets
from .models import SocialPost, User, GroupMePosts#, SocialAccount
from django.forms.widgets import ClearableFileInput

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254)
    class Meta:
        model = User
        widgets = {
            'myfield': forms.TextInput(attrs={'class': 'myfieldclass'}),
        }
        fields = ('email', 'username', 'password1', 'password2')

class SocialPostForm(forms.ModelForm):
    class Meta():
        model = SocialPost
        model.GroupMeGroups = forms.ModelMultipleChoiceField(queryset=None)
        ClearableFileInput.input_text = 'Update File'
        ClearableFileInput.clear_checkbox_label = ''
        widgets = {
            'myfield': forms.TextInput(attrs={'class': 'myfieldclass'}),
            'myfield2': forms.FileInput(attrs={'class':'imageclass'}),
            'post_time': forms.DateTimeInput(attrs={'type':'datetime-local'}, format='%Y-%m-%dT%H:%M'),
        }
        fields = ('message', 'post_time', 'picture', 'Facebook', 'GroupMe')

class TokenStoreForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('gm_auth_token',)


#https://stackoverflow.com/questions/15261286/django-forms-disable-field-if-booleanfield-is-checked

