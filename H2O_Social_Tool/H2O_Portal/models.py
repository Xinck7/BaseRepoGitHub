from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from decouple import config
from groupy import client
from picklefield.fields import PickledObjectField
import facebook 
import datetime
import pytz


class User(AbstractUser):
    # to add facebook 
    
    # accounts = models.ManyToManyField(
    #     settings.AUTH_USER_MODEL,
    #     related_name='+',
    #     )   
    # to add groupme
    gm_auth_token = models.TextField(null=True, help_text='GroupMe Authentication Token', blank=True)
    USERNAME_FIELD = 'username'

class SocialPost(models.Model):
    post_time = models.DateTimeField(
        max_length=30,
        help_text='(example: 1/31/2019 15:00)',
        )
    message = models.TextField(
        blank=True,
        max_length=2000,
        )
    picture = models.ImageField(null=True, blank=True, help_text='Only pictures are supported through this tool', upload_to='H2O_Portal/media')
    Facebook = models.BooleanField(default=False)
    GroupMe = models.BooleanField(default=False)  
    GroupMeGroups = PickledObjectField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        related_name='+',
        on_delete=models.CASCADE,
        )

    def __str__(self):
        return '{} {} {} {} {} {} {} {}'.format(
            self.post_time, 
            self.message, 
            self.picture, 
            self.Facebook, 
            self.GroupMe,
            self.GroupMeGroups,
            self.completed, 
            self.updated_by,
            )


#https://facebook-sdk.readthedocs.io/en/latest/api.html#get-object
# if and when Facebook is authenticated 
# class FacebookPosts(models.Model):
    
#     def gettoken(self):
#         pass

#     def sendpost(self):
#         access_token = config('FB_Token')
#         session = facebook.GraphAPI(access_token)
#         facebook_posts = SocialPost.objects.filter(Facebook=True, completed=False)
#         post_to_send = []
#         for post in facebook_posts:
#             if post.post_time <= utc.localize(datetime.datetime.now()):
#                 if post.picture.name == '':
#                     session.put_object("me", "feed", message=post.message)  
#                 else:
#                     session.put_photo(image=open(post.picture.path, 'rb'), message=post.message)
#                 post.completed = True
#                 post.save()


class GroupMePosts(models.Model):
    
    def getgroups(self, user_token):
        user = client
        session = user.Session(user_token)
        client_session = user.Client(session)
        groups = list(client_session.groups.list_all())
        return groups

    #####Needs modification##############
    def sendmessages(self, user_token, groupnames, groupme_post):
        user = client
        session = user.Session(user_token)
        client_session = user.Client(session)
        post_to_send = dict()
        groups = list(client_session.groups.list_all())
        utc=pytz.UTC
        post = groupme_post
        groups_to_match = groupnames
        selected_groups = []
        for group in groups:
            for sel_group in groups_to_match:
                if group.name == sel_group:
                    selected_groups.append(group)

        if post.post_time <= utc.localize(datetime.datetime.now()):
            if post.picture.name == '':
                message = post.message
                attachments = None
                post_to_send[message] = attachments
            else:
                message = post.message
                with open(post.picture.path, 'rb') as f:
                    attachments = client_session.images.from_file(f)
                    post_to_send[message] = attachments
            post.completed = True
            post.save()
        for key in post_to_send:
            for group in selected_groups:
                if post_to_send[key] == None:
                    attachment_to_send = None
                else:
                    attachment_to_send = []
                    attachment_to_send.append(post_to_send[key])
                group.post(text=key, attachments=attachment_to_send)


