from rest_framework import serializers
from .models import Blogpost
from .models import Comment
class BlogpostSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(read_only=True)
    class Meta:
        model = Blogpost
        fields = ["id", "title", "image", "content", "category", "tags", "created_at"]

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