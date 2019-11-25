from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, models

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254)
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
