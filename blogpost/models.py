from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.
class Blogpost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogposts')
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000, blank=True)
    image = CloudinaryField('image', blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    tags = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
   

class Comment(models.Model):
    post = models.ForeignKey('Blogpost', related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"
