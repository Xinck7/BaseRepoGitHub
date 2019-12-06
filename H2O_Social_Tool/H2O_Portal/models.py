from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
from decouple import config
from groupy import Client
# Create your models here.

class User(AbstractUser):
    accounts = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='+',
        )
    USERNAME_FIELD = 'username'

class SocialPost(models.Model):
    title = models.TextField(
        blank=True,
        max_length=200,
        )
    post_time = models.DateTimeField(
        max_length=30,
        help_text='(ex 1/31/2019 13:00)',
        )
    message = models.TextField(
        blank=True,
        max_length=2000,
        )
    picture = models.ImageField(blank=True)
    Facebook = models.BooleanField(default=False)
    Instagram = models.BooleanField(default=False)
    GroupMe = models.BooleanField(default=False)     
    completed = models.BooleanField(default=False)
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        related_name='+',
        on_delete=models.CASCADE,
        )

    def __str__(self):
        return '{} {} {} {} {} {} {} {} {}'.format(
            self.title, 
            self.post_time, 
            self.message, 
            self.picture, 
            self.Facebook, 
            self.Instagram, 
            self.GroupMe, 
            self.completed, 
            self.updated_by,
            )
    


class FacebookStatus(models.Model):
    class Meta:
        verbose_name_plural = 'Facebook Statuses'
        ordering = ['publish_timestamp']
    STATUS = (
        ('draft', 'Draft'),
        ('approved', 'Approved'),
    )
    status = models.CharField(
        max_length=255, 
        choices=STATUS,
        default=STATUS[0][0]
        )
    publish_timestamp = models.DateTimeField(
        null=True,
        blank=True
        )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE
        )
    message = models.TextField(max_length=255)
    link = models.URLField(
        null=True,
        blank=True
        )

    def __unicode__(self):
        return self.message

class GroupMePosts(models.Model):
    def getgroups():
        client_token = Client.from_token(config('GroupMe_AuthToken'))
        groups = list(client_token.groups.list_all())
        return groups
    
    def sendmessages():
        groups_to_send = getgroups()
        groupme_posts = SocialPost.objects.filter(GroupMe=True)
        post_to_send = []
        for message in groupme_posts:
            if message.post_time >= datetime.datetime.now():
                if message.picture != None:
                    post_to_send.message += message.message
                    post_to_send.picture += message.picture
                else:
                    post_to_send.message += message.message
        for post in post_to_send:
            for group in groups_to_send:
                message.group.post(text=post_to_send.message)

    if SocialPost.GroupMe == True:
        GroupMePosts.getgroups()


#In progress to fixing users within the specific user and linking them together
#https://stackoverflow.com/questions/373335/how-do-i-get-a-cron-like-scheduler-in-python
#https://automatetheboringstuff.com/chapter15/
