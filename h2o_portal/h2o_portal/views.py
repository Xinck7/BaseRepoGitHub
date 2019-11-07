from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from h2o_portal.models import Post, Credentials
from h2o_portal.serializers import PostSerializer, CredentialSerializer

def home(request):
    return HttpResponse('<h1>blog home</h1>')


class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class CredentialViewSet(ModelViewSet):
    serializer_class = CredentialSerializer
    queryset = Credentials.objects.all()

