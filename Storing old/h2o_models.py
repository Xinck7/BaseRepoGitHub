import datetime
import calendar

# Organizes a Social Post

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
        # Use datetime.datetime to validate information and ensure this is an actual date
        time_of_day = input("Input Time you want to schedule the post for in X format -> ")
        try:
            return time_of_day
        except ValueError:
            print("Not sure how you messed that up - try again")
            break


class Credentials:
    def __init__(self, username, password, authtype):
        self.username = username
        self.password = password
        self.authtype = authtype


class Post:
    def __init__(self, post_time, text, picture):
        self.post_time = post_time
        self.text = text
        self.picture = picture

#######Flow of actual operations##########
##before program 'starts'##
# check OS and current user name
# create folders on desktop or prompt for other destination during install
# initialize and check for folders on execution pass if they exist
##During execution flow##
# prompt for credentials
# prompt for what social media site
# prompt fo what picture and text to post
# prompt when to post
# queue job
# move pic to pending post folder
# have job callable by calendar and listed available as well
# move pic to
# show completed/executed jobs
