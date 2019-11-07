from django.db import models


class Post(models.Model):
    post_time = models.DateTimeField()
    text = models.CharField()
    picture = models.ImageField()

class Credentials(models.Model):
    username = models.CharField()
    password = models.CharField()
    authtype = models.CharField()