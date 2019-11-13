from django.contrib.auth.models import User, Group
from rest_framework import serializers
from H2O_Portal.models import Post, Credentials

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'password', 'social account/ H2O app']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name', 'type']


class PostSerializer(serializers.ListSerializer):
    class Meta:
        model = Post
        fields '__all__'


class CredentialSerializer(serializers.ListSerializer):
    class Meta:
        model = Post
        fields '__all__'