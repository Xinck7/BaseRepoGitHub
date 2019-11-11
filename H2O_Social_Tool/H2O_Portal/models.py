from django.db import models
from django.contrib.auth.models import User
import json

# Create your models here.

class Post(models.Model):
    title = models.TextField(blank=False)
    post_time = models.DateTimeField(max_length=30)
    text = models.TextField(blank=True)
    picture = models.ImageField(upload_to='media/')
    
    def __str__(self):
        return self.title

class Credentials(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    ACCOUNT_TYPES = (
        ('F', 'Facebook'),
        ('I', 'Instagram'),
        ('G', 'GroupMe')
    ) 
    account = models.CharField(max_length=1, choices=ACCOUNT_TYPES)

class Users(models.Model):
    
    pass 
