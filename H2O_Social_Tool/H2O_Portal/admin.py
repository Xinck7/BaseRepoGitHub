from django.contrib import admin
from .models import SocialPost, user#, SocialAccount

# Register your models here.
admin.site.register(SocialPost)
admin.site.register(user)
#admin.site.register(SocialAccount)

