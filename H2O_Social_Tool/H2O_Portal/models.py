from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.TextField(blank=True, max_length=200)
    post_time = models.DateTimeField(max_length=30)
    text = models.TextField(blank=True, max_length=2000)
    picture = models.ImageField(blank=True)
    
    def __str__(self):
        return '{} {} {} {}'.format(self.title, self,post_time, self.text, self.picture)

class Credentials(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    ACCOUNTTYPES = [
        ('F', 'Facebook'),
        ('I', 'Instagram'),
        ('G', 'GroupMe'),
    ] 
    accounttype = models.CharField(max_length=1, choices=ACCOUNTTYPES)
    accountowner = models.ForeignKey(User, related_name='Credentials', on_delete=models.CASCADE)

    def __str__(self):
        return '{} {} {} {}'.format(self.username, self,password, self.accounttype, self.accountowner)

