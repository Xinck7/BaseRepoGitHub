from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render
from django.http import HttpResponse
from h2o_portal.models import Post, Credentials
from h2o_portal.serializers import PostSerializer, CredentialSerializer

def home(request):
    return HttpResponse('<h1>H2O Social Media Tool Home Page</h1>') 


class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class CredentialViewSet(ModelViewSet):
    serializer_class = CredentialSerializer
    queryset = Credentials.objects.all()

