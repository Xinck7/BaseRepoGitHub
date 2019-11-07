from rest_framework import generics
from h2o_portal.models import Post, Credentials
from h2o_portal.serializers import PostSerializer, CredentialSerializer

class PostViewSet(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class CredentialViewSet(generics.ListCreateAPIView):
    serializer_class = CredentialSerializer
    queryset = Credentials.objects.all()

