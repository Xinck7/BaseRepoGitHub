from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class SocialPost(models.Model):
    title = models.TextField(blank=True, max_length=200)
    post_time = models.DateTimeField(max_length=30)
    message = models.TextField(blank=True, max_length=2000)
    picture = models.ImageField(blank=True)
    Facebook = models.BooleanField(default=False)
    Instagram = models.BooleanField(default=False)
    GroupMe = models.BooleanField(default=False) 
    completed = models.BooleanField(default=False)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE)

    def __str__(self):
        return '{} {} {} {} {} {} {}'.format(self.title, self.post_time, self.message, self.picture, self.Facebook, self.Instagram, self.GroupMe, self.completed self.updated_by)

    #def fbpost


    #def instapost

    
    #def gmpost

#In progress to fixing users within the specific user and linking them together

class SocialAccount(models.Model):
    ACCOUNT = (
        ('f', ('Facebook')),
        ('i', ('Instagram')),
        ('g', ('GroupMe')),
        ('n', ('Choose an Account type'))
    )
    account_type = models.CharField(
        max_length=30,
        choices=ACCOUNT,
        default='n',
    )
    username = models.CharField(blank=True, max_length=40)
    password = models.CharField(blank=True, max_length=40)

    def __str__(self):
        return '{} {}'.format(self.account_type, self.username)
