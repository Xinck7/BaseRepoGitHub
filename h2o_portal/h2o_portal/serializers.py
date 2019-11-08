from rest_framework import serializers
from h2o_models import Credentials, Post

#PostSerializer, CredentialSerializer
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class CredentialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credentials
        fields = '__all__'
