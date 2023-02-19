from django.shortcuts import render
from Account.models import User_create, User_Profile
from Account.serializer import UserSerializer, UserProfileSerializer
"""Import generics and mixins"""
from rest_framework import generics
from rest_framework import mixins
"""Authentication import"""
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser

# Create your views here.


class create_user(generics.CreateAPIView):
    """Create user api"""
    queryset = User_create.objects.all()
    serializer_class = UserSerializer


class user_list(generics.ListAPIView):
    """user list api"""
    queryset = User_create.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]


class user_profile(generics.ListCreateAPIView):
    """user profile create api and list"""
    queryset = User_Profile.objects.all()
    serializer_class = UserProfileSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class user_profile_update(generics.RetrieveUpdateDestroyAPIView):
    """user profile update , delete and details api"""
    queryset = User_Profile.objects.all()
    serializer_class = UserProfileSerializer
    lookup_field = 'id'
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
