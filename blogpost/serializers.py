from rest_framework import serializers
from .models import Blogpost, Comment, Notification


class BlogpostSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False, allow_null=True)
    like_count = serializers.IntegerField(read_only=True)
    is_liked = serializers.SerializerMethodField()
    tags = serializers.ListField(
        child=serializers.CharField(),
        required=False
    )

    class Meta:
        model = Blogpost
        fields = ["id", "title", "image", "content", "category", "tags", "created_at", "like_count", "is_liked"]

    def get_like_count(self, obj):
        # Use the annotated value if present (from trending view), else fallback to the property
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


class CommentSerializer(serializers.ModelSerializer):
    author_first_name = serializers.CharField(source='author.userprofile.first_name', read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'author_first_name', 'content', 'created_at', 'updated_at']
        read_only_fields = ['author', 'author_first_name', 'created_at', 'updated_at']


class NotificationSerializer(serializers.ModelSerializer):
    sender_first_name = serializers.CharField(source='sender.userprofile.first_name', read_only=True)

    class Meta:
        model = Notification
        fields = ['id', 'recipient', 'sender', 'sender_first_name', 'post', 'notification_type', 'message', 'created_at', 'is_read']

class AuthorDashboardSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    avatar = serializers.CharField()
    total_likes = serializers.IntegerField()
    posts = BlogpostSerializer(many=True)

