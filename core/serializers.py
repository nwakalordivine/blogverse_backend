from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Userprofile

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password')

    def create(self, validated_data):
        email = validated_data['email']
        password = validated_data['password']
        user = User.objects.create_user(
            username=email,    
            email=email,
            password=password
        )
        return user

class UserprofileSerializer(serializers.ModelSerializer):
    avatar = serializers.ImageField(read_only=True)
    email = serializers.ReadOnlyField(source="user.username")
    class Meta:
        model = Userprofile
        fields = ['id', 'first_name', 'last_name', 'email', 'bio', 'avatar']
        read_only_fields = ['email']

    
    

class uploadSerializer(serializers.ModelSerializer):
    avatar = serializers.ImageField()
    class Meta:
        model = Userprofile
        fields = ['avatar']

    