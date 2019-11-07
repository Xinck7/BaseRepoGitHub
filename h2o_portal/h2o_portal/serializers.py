from django.contrib.auth.models import User, Group
from rest_framework import serializers

#PostSerializer, CredentialSerializer
class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class CredentialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']