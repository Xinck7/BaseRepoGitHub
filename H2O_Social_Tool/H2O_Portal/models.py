from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from decouple import config
#from groupy.client import Client, attachments
from groupy import client
import datetime
import pytz

# Create your models here.

class User(AbstractUser):
    # to add facebook 
    accounts = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='+',
        )
    # to add instagram
    insta_auth_token = models.TextField(null=True, help_text='Instagram Auth Token')
    # to add groupme
    gm_auth_token = models.TextField(null=True, help_text='GroupMe Auth Token')
    USERNAME_FIELD = 'username'

class SocialPost(models.Model):
    title = models.TextField(
        blank=True,
        max_length=200,
        help_text='(Not Required, but is helpful for reviewing)'
        )
    post_time = models.DateTimeField(
        max_length=30,
        help_text='(ex 1/31/2019 13:00)',
        )
    message = models.TextField(
        blank=True,
        max_length=2000,
        )
    picture = models.ImageField(null=True, upload_to='H2O_Portal/static')
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

    def sendmessages(self, groupnames):
        user = client
        session = user.Session(config('GroupMe_AuthToken'))
        client_session = user.Client(session)
        groups = list(client_session.groups.list_all())
        groups_to_send = []
        for group in groups:
            for names in groupnames:
                if group.name == names:
                    groups_to_send.append(group)
        post_to_send = []
        post_attachments = []
        groupme_posts = SocialPost.objects.filter(GroupMe=True, completed=False)
        utc=pytz.UTC
        for post in groupme_posts:
            if post.post_time <= utc.localize(datetime.datetime.now()):
                if post.picture == None:
                    post_to_send.append(post.message)
                    attachments = None
                else:
                    post_to_send.append(post.message)
                    with open(post.picture.path, 'rb') as f:
                        upload = client_session.images.from_file(f)
                        post_attachments.append(upload)
                post.completed = True
        for to_send in post_to_send:
            for group in groups_to_send:
                group.post(text=to_send, attachments=post_attachments)


#In progress to fixing users within the specific user and linking them together
#https://stackoverflow.com/questions/373335/how-do-i-get-a-cron-like-scheduler-in-python
#https://automatetheboringstuff.com/chapter15/
