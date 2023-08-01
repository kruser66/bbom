from rest_framework import viewsets, views
from rest_framework import permissions

from blog.models import User, Post
from blog.serializers import UserSerializer, PostSerializer
from blog.permissions import IsUserOrReadOnly


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint all users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint user's posts.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsUserOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)