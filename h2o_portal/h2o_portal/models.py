from django.db import models


class Post(models.Model):
    post_time = models.DateTimeField(max_length=30)
    text = models.CharField(max_length=30)
    picture = models.ImageField(upload_to='h2o_portal/', default= 'h2o_portal/h2oLogo.png')

class Credentials(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    authtype = models.CharField(max_length=30)