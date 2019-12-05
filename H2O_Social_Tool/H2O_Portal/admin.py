from django.contrib import admin
from .models import SocialPost, User#, SocialAccount

# Register your models here.
admin.site.register(SocialPost)
admin.site.register(User)
#admin.site.register(SocialAccount)

