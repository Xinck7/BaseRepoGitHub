from rest_framework.viewsets import ModelViewSet

from h2o_portal.models import Post
from h2o_portal.serializers import PostSerializer


class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
