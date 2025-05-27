from rest_framework import serializers
from .models import Blogpost, Comment, Notification


class CommentSerializer(serializers.ModelSerializer):
    author_first_name = serializers.CharField(source='author.userprofile.first_name', read_only=True)
    author_avatar = serializers.ImageField(source='author.userprofile.avatar', read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'author_avatar', 'author_first_name', 'content', 'created_at', 'updated_at']
        read_only_fields = ['author', 'author_first_name', 'created_at', 'updated_at', 'author_avatar']


class BlogpostSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False, allow_null=True)
    like_count = serializers.IntegerField(read_only=True)
    is_liked = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)
    tags = serializers.ListField(
        child=serializers.CharField(),
        required=False
    )
    author_first_name = serializers.CharField(source='author.userprofile.first_name', read_only=True)
    author_last_name = serializers.CharField(source='author.userprofile.last_name', read_only=True)
    author_avatar = serializers.ImageField(source='author.userprofile.avatar', read_only=True)
    author_bio = serializers.CharField(source='author.userprofile.bio', read_only=True)

    class Meta:
        model = Blogpost
        fields = [
            "id", "title", "image", "content", "category", "comments", "tags",
            "created_at", "like_count", "is_liked",
            "author_first_name", "author_last_name", "author_avatar", "author_bio"
        ]

    def get_like_count(self, obj):
        return getattr(obj, 'num_likes', obj.like_count)
    
    def get_is_liked(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            return obj.likes.filter(id=user.id).exists()
        return False


class BlogimageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    class Meta:
        model = Blogpost
        fields = ["image"]


class NotificationSerializer(serializers.ModelSerializer):
    sender_first_name = serializers.CharField(source='sender.userprofile.first_name', read_only=True)

    class Meta:
        model = Notification
        fields = ['id', 'recipient', 'sender', 'sender_first_name', 'post', 'notification_type', 'message', 'created_at', 'is_read']

class AuthorDashboardSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    avatar = serializers.CharField(allow_null=True)
    total_likes = serializers.IntegerField()
    posts = BlogpostSerializer(many=True)
