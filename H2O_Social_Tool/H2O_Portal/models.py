from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from decouple import config
from groupy import client
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
    gm_auth_token = models.TextField(null=True, help_text='GroupMe Auth Token', blank=True)
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
    picture = models.ImageField(null=True, blank=True, upload_to='H2O_Portal/static', help_text='Only pictures are supported through this tool')
    Facebook = models.BooleanField(default=False)
    GroupMe = models.BooleanField(default=False)  
    GroupMeGroups = models.TextField(null=True)
    #https://stackoverflow.com/questions/1110153/what-is-the-most-efficient-way-to-store-a-list-in-the-django-models
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
    def sendmessages(self, user_token, groupnames):
        user = client
        session = user.Session(user_token)
        client_session = user.Client(session)
        post_to_send = []
        post_attachments = []
        utc=pytz.UTC
        for post in groupme_posts:
            if post.post_time <= utc.localize(datetime.datetime.now()):
                if post.picture.name == '':
                    post_to_send.append(post.message)
                    attachments = None
                else:
                    post_to_send.append(post.message)
                    #This may not work as intended need to think about how this should send as a list
                    #I think I may be able to save it overtop of the actual 'picture' file that is there on the post
                    #may work by accident since i'm doing the messages one at a time if I read right not 100%
                #BUT A DICTIONARY WILL!!
                    with open(post.picture.path, 'rb') as f:
                        upload = client_session.images.from_file(f)
                        post_attachments.append(upload)
                post.completed = True
                post.save()
        for to_send in post_to_send:
            for group in selected_groups:
                group.post(text=to_send, attachments=post_attachments)

#archive logic delete when officially working
        # groups = list(client_session.groups.list_all())
        # groupset = dict()
        # i=0
        # for i in range(0, len(groups)):
        #     groupname = groups[i].name
        #     groupset[i] = groupname

        # selection_array = list(groupnames)
        # selected_groups = []
        # for item in selection_array:
        #     for group in groups:
        #         if item == group.name:
        #             selected_groups.append(groupset[item])
