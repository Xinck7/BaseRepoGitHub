from django.core.management.base import BaseCommand, CommandError
from H2O_Portal.models import *

class Command(BaseCommand):
    help = 'This Script will send the posts that have not been sent to their proper destinations'
    
    def handle(self, *args, **kwargs):
        unposted = SocialPost.objects.filter(completed=False)
        for post in unposted:
            # if post.Facebook == True:
            #     init_posts = FacebookPosts()
            #     init_posts.sendpost()
            
            #####Needs modification##############
            if post.GroupMe == True:
                groupnames = post.GroupMeGroups
                #groupnames = 
                gmp = GroupMePosts()
                gmp.sendmessages(groupnames)
            # check time if its time to post
            # post if its time

