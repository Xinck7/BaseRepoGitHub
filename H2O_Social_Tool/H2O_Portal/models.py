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
    ''' 
    Model for Social Media Post:
    Fields available: 
    post_time (datetime),
    message(2000 char limit),
    picture (no videos available), 
    Facebook (boolean), 
    completed (boolean to determine table information and send status), 
    updated_by (selects last user to save)
    ''' 
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
    #GroupMeGroups?
    #GroupMeGroups = models.TextField(null=True)
    GroupMeGroups = []
    #https://stackoverflow.com/questions/1110153/what-is-the-most-efficient-way-to-store-a-list-in-the-django-models
    completed = models.BooleanField(default=False)
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        related_name='+',
        on_delete=models.CASCADE,
        )

    def __str__(self):
        return '{} {} {} {} {} {} {} {} {}'.format(
            self.post_time, 
            self.message, 
            self.picture, 
            self.Facebook, 
            self.GroupMe,
            self.GroupMeGroups,
            self.completed, 
            self.updated_by,
            )


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
    ##needs param for the groupme token when making for anyone
    ##https://stackoverflow.com/questions/5080828/how-to-group-the-choices-in-a-django-select-widget
    # user_token = User().gm_auth_token
    # def selectgroups(self, user_token, selection):
    #     user = client
    #     session = user.Session(user_token)
    #     client_session = user.Client(session)
    #     groups = list(client_session.groups.list_all())
    #     groupset = dict()
    #     i=0
    #     for i in range(0, len(groups)):
    #         groupname = groups[i].name
    #         groupset[i] = groupname

    #     selection_array = selection
    #     selected_groups = []
    #     for item in selection:
    #         selected_groups.append(groupset[item])
        
    #     return selected_groups

    def sendmessages(self, groupnames):
        # old set preserver until multi select based on user is completed
        user = client
        session = user.Session(config('GroupMe_AuthToken'))
        client_session = user.Client(session)
        groups = list(client_session.groups.list_all())
        #groupnames will be defined later as a part of the groupme_posts var so this would go after and within the if post.post_time processing
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
                if post.picture.name == '':
                    post_to_send.append(post.message)
                    attachments = None
                else:
                    post_to_send.append(post.message)
                    with open(post.picture.path, 'rb') as f:
                        upload = client_session.images.from_file(f)
                        post_attachments.append(upload)
                post.completed = True
                post.save()
        for to_send in post_to_send:
            for group in groups_to_send:
                group.post(text=to_send, attachments=post_attachments)


