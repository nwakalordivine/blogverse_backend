from rest_framework import generics
from .serializers import RegisterSerializer, UserprofileSerializer, uploadSerializer
from django.contrib.auth.models import User
from .models import Userprofile
from blogpost.permissions import IsOwnerOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class UserprofileDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Userprofile.objects.all()
    serializer_class = UserprofileSerializer
    lookup_field = 'pk'
    permission_classes = [IsOwnerOrReadOnly]


class AvatarUpdateAPIViews(generics.UpdateAPIView):
    serializer_class = uploadSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return Userprofile.objects.get(user=self.request.user)

class UserMeAPIView(APIView):
    permission_classes = [IsAuthenticated]
    """
    get:
    Return the current user's profile.
    
    put:
    Update the current user's profile.

    patch:
    Partially update the current user's profile.
    """
    def get(self, request):
        profile = Userprofile.objects.get(user=request.user)
        serializer = UserprofileSerializer(profile)
        return Response(serializer.data)

    def put(self, request):
        profile = Userprofile.objects.get(user=request.user)
        serializer = UserprofileSerializer(profile, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def patch(self, request):
        profile = Userprofile.objects.get(user=request.user)
        serializer = UserprofileSerializer(profile, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)