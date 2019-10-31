import datetime
import calendar
import html

#html things

def init_username():
    while True:
        username = input("Input Username -> ")
        try:
            return username
        except ValueError:
            print("Not sure how you messed that up - try again")
            break

def init_password():
    while True:
        password = input("Input Password -> ")
        try:
            return password
        except ValueError:
            print("Not sure how you messed that up - try again")
            break
   
def init_day_of_week():
    while True:
        day_of_week = input("What day of the week do you want to post this? -> ")
        try:
            return day_of_week
        except ValueError:
            print("Not sure how you messed that up - try again")
            break    
  
def get_day():
    while True:
        #Use datetime.datetime to validate information and ensure this is an actual date
        time_of_day = input("Input Time you want to schedule the post for in X format -> ")
        try:
            return time_of_day
        except ValueError:
            print("Not sure how you messed that up - try again")
            break    
    
    

#def check_scheduled_posts():
    #schedule cron task every 30 mins to post and return into a file/csv/other?
    #schedule windows task every 30 mins to post and return into a file/csv/other?

#def schedule_post():
#def review_scheduled_posts():
#def review_calendar_format():      

#tried using classes asking about this tuesday
#Organizes a Social Post
# class SocialPost:
#     #def __class__(self, Insta_Usernam, Insta_Password, GroupMe_Username, Facebook_Username, Facebook_Password, DayofWeek, TimeofDay, Picture, PostText, StorageLocation):
#         # self.Insta_Username = init_username
#         # self.Insta_Password = init_password
#         # self.GroupMe_Username = init_username
#         # self.GroupMe_Password = init_password
#         # self.Facebook_Username = init_username
#         # self.Facebook_Password = init_password
#         # self.DayofWeek = day_of_week #day of week
#         # self.TimeofDay = time_of_day #time of day function
#         # self.Picture = 'x' #Picture
#         # self.PostText = 'y' 
#         # self.StorageLocation = 'z'
#     Post.Insta_Username = init_username
#     Post.Insta_Password = init_password
#     Post.GroupMe_Username = init_username
#     Post.GroupMe_Password = init_password
#     Post.Facebook_Username = init_username
#     Post.Facebook_Password = init_password
#     Post.DayofWeek = 'day_of_week' #day of week
#     Post.TimeofDay = 'time_of_day' #time of day function
#     Post.Picture = 'x' #Picture
#     Post.PostText = 'y' 
#     Post.StorageLocation = 'z'


#######Flow of actual operations##########
    ##before program 'starts'##
        #check OS and current user name
        #create folders on desktop or prompt for other destination during install
        #initialize and check for folders on execution pass if they exist
    ##During execution flow##
        #prompt for credentials
        #prompt for what social media site
        #prompt fo what picture and text to post
        #prompt when to post
        #queue job 
        #move pic to pending post folder
        #have job callable by calendar and listed available as well 
        #move pic to 
        #show completed/executed jobs
        