from rest_framework import serializers
from blog.models import User, Post


class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())
    
    class Meta:
        model = User
        fields = ['url', 'id', 'name', 'email', 'posts']


class PostSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    
    class Meta:
        model = Post
        fields = ['url', 'id', 'user', 'title', 'body']