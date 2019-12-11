from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from .models import SocialPost, User#, SocialAccount

class MyUserAdmin(UserAdmin):
    model = User
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ['gm_auth_token']}),
    )

# Register your models here.
admin.site.register(SocialPost)
admin.site.register(User, MyUserAdmin)

