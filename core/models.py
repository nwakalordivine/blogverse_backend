from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.
from django.contrib.auth.models import User

class Userprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    bio = models.TextField(blank=True, default="Hi i'm new here")
    avatar = CloudinaryField('avatar', blank=True)
    is_author = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
