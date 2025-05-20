from rest_framework import serializers
from .models import Blogpost

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

