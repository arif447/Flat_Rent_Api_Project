from rest_framework import serializers
from Account.models import User_create, User_Profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_create
        fields = ['id', 'user_name', 'email', 'password']


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Profile
        fields = ['author', 'firstname', 'lastname', 'address']



