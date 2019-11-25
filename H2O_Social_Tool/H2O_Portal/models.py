from django.db import models
# Create your models here.

class Post(models.Model):
    title = models.TextField(blank=True, max_length=200)
    post_time = models.DateTimeField(max_length=30)
    text = models.TextField(blank=True, max_length=2000)
    picture = models.ImageField(blank=True)
    dest_fb = models.BooleanField(default=False)
    dest_insta = models.BooleanField(default=False)
    dest_gm = models.BooleanField(default=False) 
    completed = models.BooleanField(default=False)
    updated_by = models.ForeignKey(User, null=True, related_name='+' )

    def __str__(self):
        return '{} {} {} {} {} {} {}'.format(self.title, self.post_time, self.text, self.picture, self.dest_fb, self.dest_insta, self.dest_gm, self.updated_by)

    #def fbpost


    #def instapost

    
    #def gmpost

#In progress to fixing users within the specific user and linking them together

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
