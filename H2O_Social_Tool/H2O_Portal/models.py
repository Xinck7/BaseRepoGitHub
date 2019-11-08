from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    post_time = models.DateTimeField(max_length=30)
    text = models.CharField(max_length=30)
    picture = models.ImageField(upload_to='media/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.post_time

class Credentials(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    accounttype = models.CharField(max_length=30)
    
    def __str__(self):
        return self.username, self.accounttype

