from rest_framework import generics
from h2o_portal.models import Post, Credentials
from h2o_portal.serializers import PostSerializer, CredentialSerializer


class PostViewSet(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    


class CredentialViewSet(generics.ListCreateAPIView):
    queryset = Credentials.objects.all()
    serializer_class = CredentialSerializer
    

