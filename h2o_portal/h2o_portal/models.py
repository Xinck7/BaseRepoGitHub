from django.db import models


class Post(models.Model):
    post_time = models.DateTimeField()
    text = models.CharField()
    picture = models.ImageField()
