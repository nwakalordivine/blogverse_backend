from rest_framework import generics
from .serializers import RegisterSerializer, UserprofileSerializer, uploadSerializer
from django.contrib.auth.models import User
from .models import Userprofile
from rest_framework.permissions import IsAuthenticated
from blogpost.permissions import IsAdmin

class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class UserprofileDetailAPIView(generics.RetrieveAPIView):
    queryset = Userprofile.objects.all()
    serializer_class = UserprofileSerializer
    permission_classes = [IsAuthenticated]


class AvatarUpdateAPIViews(generics.UpdateAPIView):
    serializer_class = uploadSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return Userprofile.objects.get(user=self.request.user)


class UserMeAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = UserprofileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return Userprofile.objects.get(user=self.request.user)
    
class UserProfileRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Userprofile.objects.all()
    serializer_class = UserprofileSerializer
    permission_classes = [IsAdmin]

    def perform_destroy(self, instance):
        user = instance.user
        instance.delete()
        user.delete()

class UserProfileListAPIView(generics.ListAPIView):
    queryset = Userprofile.objects.all()
    serializer_class = UserprofileSerializer
    permission_classes = [IsAdmin]

