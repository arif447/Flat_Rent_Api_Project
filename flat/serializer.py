from rest_framework import serializers
from flat.models import Category, Flat


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title']


class FlatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flat
        fields = ['category', 'house_name', 'house_number', 'area', 'flat_size', 'flat_rent', 'bad', 'bath']
