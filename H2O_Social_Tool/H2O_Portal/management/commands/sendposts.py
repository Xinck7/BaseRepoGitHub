from django.core.management.base import BaseCommand, CommandError
from H2O_Portal.models import *

class Command(BaseCommand):
    help = 'This Script will send the posts that have not been sent to their proper destinations'
    
    def handle(self, *args, **kwargs):
        unposted = SocialPost.objects.filter(completed=False)
        all_users = User.objects.all()
        for post in unposted:
            # if post.Facebook == True:
            #     init_posts = FacebookPosts()
            #     init_posts.sendpost()
            
            #####Needs modification##############
            if post.GroupMe == True:
                groupnames = post.GroupMeGroups
                user_name = post.updated_by
                filter_user = all_users.filter(username=user_name)
                user_db_info = filter_user.values('gm_auth_token')
                token_dict = user_db_info.get()
                auth_token = token_dict['gm_auth_token']
                if auth_token != None:
                    gmp = GroupMePosts()
                    gmp.sendmessages(auth_token, groupnames)
            # check time if its time to post
            # post if its time

