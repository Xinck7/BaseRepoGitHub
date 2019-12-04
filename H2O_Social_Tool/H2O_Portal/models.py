from django.db import models
from django.contrib.auth.models import User
from groupy import Client, attachments
# Create your models here.

class SocialPost(models.Model):
    title = models.TextField(blank=True, max_length=200)
    post_time = models.DateTimeField(max_length=30, help_text='(ex 1/31/2019 13:00)')
    message = models.TextField(blank=True, max_length=2000)
    picture = models.ImageField(blank=True)
    Facebook = models.BooleanField(default=False)
    Instagram = models.BooleanField(default=False)
    GroupMe = models.BooleanField(default=False) 
    completed = models.BooleanField(default=False)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE)

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
            self.updated_by)
            
    class FacebookStatus(models.Model):
        class Meta:
            verbose_name_plural = 'Facebook Statuses'
            ordering = ['publish_timestamp']
        # STATUS = (
        #     ('draft', 'Draft'),
        #     ('approved', 'Approved'),
        # )
        # status = models.CharField(max_length=255, 
        #     choices=STATUS, default=STATUS[0][0])
        publish_timestamp = models.DateTimeField(null=True, blank=True)
        author = models.ForeignKey(User)
        message = models.TextField(max_length=255)
        link = models.URLField(null=True, blank=True)

        def __unicode__(self):
            return self.message

    class GroupMePosts(models.Model):
        def getgroups():
            client = Client.from_token('api_token')
            groups = list(client.groups.list_all())
        
        def sendmessage(socialmessage):
            groupstosend = getgroups()
            imageattachment = 
            for group in groupstosend:
                message.group.post(socialmessage)

    # if SocialPost.GroupMe = True:
    #     GroupMePosts.getgroups()


#In progress to fixing users within the specific user and linking them together
#https://stackoverflow.com/questions/373335/how-do-i-get-a-cron-like-scheduler-in-python
#https://automatetheboringstuff.com/chapter15/

# Likely not going to be used but don't want to migrate and delete steps
# Delete section when working on the actual post sending since itll read likely another place
# Don't forget to remove from admin.py as well
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
# End Delete section