from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, models

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254)
    #login = models.BooleanField(default=False)
    #I think this could work as an if else for the login for single page app 
    #single page becoming more trouble than worth quickly it seems backend wise
    class Meta:
        model = User
        widgets = {
            'myfield': forms.TextInput(attrs={'class': 'myfieldclass'}),
        }
        fields = ('username', 'password1', 'password2', 'email')

# class LoginForm(User):
#     user = User.objects.create_user()
#     widgets = {
#             'myfield': forms.TextInput(attrs={'class': 'myfieldclass'}),
#         }
#     fields = ('username', 'password', 'email')
