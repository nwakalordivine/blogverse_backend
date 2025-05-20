from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.
class Blogpost(models.Model):
   
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogposts')
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000, blank=True)
    image = CloudinaryField('image', blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    tags = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
