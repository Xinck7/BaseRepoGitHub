from django.db import models
from django.forms import forms, PasswordInput, CharField
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title = models.TextField(blank=True, max_length=200)
    post_time = models.DateTimeField(max_length=30)
    text = models.TextField(blank=True, max_length=2000)
    picture = models.ImageField(blank=True)
    dest_fb = models.BooleanField(default=False)
    dest_insta = models.BooleanField(default=False)
    dest_gm = models.BooleanField(default=False) 
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return '{} {} {} {} {} {} {} {}'.format(self.title, self.post_time, self.text, self.picture, self.dest_fb, self.dest_insta, self.dest_gm, self.completed)

    #def fbpost


    #def instapost

    
    #def gmpost

#In progress to fixing users within the specific user and linking them together
class PasswordField(CharField):
    widget = PasswordInput()

class PasswordModelField(models.CharField):

    def formfield(self, **kwargs):
        defaults = {'form_class': PasswordField}
        defaults.update(kwargs)
        return super(PasswordModelField, self).formfield(**defaults)

class Social(models.Model):
    ACCOUNT = (
        ('f', ('facebook')),
        ('i', ('instagram')),
        ('g', ('groupme')),
        ('n', ('null'))
    )
    account_type = models.CharField(
        max_length=30,
        choices=ACCOUNT,
        default='n',
    )
    username = models.CharField(blank=True, max_length=40)
    password = PasswordModelField()

    def __str__(self):
        return '{} {} {}'.format(self.account_type, self.username, self.password)