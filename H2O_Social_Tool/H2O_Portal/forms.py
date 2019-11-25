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

class SocialPostForm(forms.ModelForm):
    class Meta:
        model = SocialPost
        fields = ('Title', 'Post Time', 'Message', 'Picture', 'Facebook?', 'Instagram?', 'GroupMe?')
    # title = models.TextField(blank=True, max_length=200)
    # post_time = models.DateTimeField(max_length=30)
    # text = models.TextField(blank=True, max_length=2000)
    # picture = models.ImageField(blank=True)
    # dest_fb = models.BooleanField(default=False)
    # dest_insta = models.BooleanField(default=False)
    # dest_gm = models.BooleanField(default=False) 
    # completed = models.BooleanField(default=False)
    # updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE)
    # https://tutorial.djangogirls.org/en/django_forms/