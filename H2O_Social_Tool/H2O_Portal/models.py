from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.TextField(blank=True, max_length=200)
    post_time = models.DateTimeField(max_length=30)
    text = models.TextField(blank=True, max_length=2000)
    picture = models.ImageField(blank=True)
    author = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE)
    destination = models.ForeignKey(User, null=True, related_name='Credentials', on_delete=models.CASCADE)


class Credentials(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    ACCOUNT_TYPES = (
        ('F', 'Facebook'),
        ('I', 'Instagram'),
        ('G', 'GroupMe')
    ) 
    account = models.CharField(max_length=1, choices=ACCOUNT_TYPES)


