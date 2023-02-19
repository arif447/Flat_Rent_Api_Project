from django.shortcuts import render
"""import authentication class"""
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAdminUser

"""import models and serializers"""
from flat.models import Flat, Category
from flat.serializer import CategorySerializer, FlatSerializer

"""import generics and mixins class"""
from rest_framework import generics, mixins


class add_category(generics.ListCreateAPIView,):
    """Add category api and list api"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]


class update_category(generics.RetrieveUpdateAPIView, mixins.DestroyModelMixin):
    """Update and delete category  api"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class add_flat(generics.ListAPIView, mixins.CreateModelMixin):
    """Add flat and list flat api"""
    queryset = Flat.objects.all()
    serializer_class = FlatSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class update_flat(generics.RetrieveAPIView, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    """Details , update and delete API"""
    queryset = Flat.objects.all()
    serializer_class = FlatSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)




