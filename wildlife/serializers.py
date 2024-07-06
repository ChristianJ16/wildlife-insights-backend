from rest_framework import serializers
from .models import FavoriteList, Animal

class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = '__all__'

class FavoriteListSerializer(serializers.ModelSerializer):
    animals = AnimalSerializer(many=True, read_only=True)

    class Meta:
        model = FavoriteList
        fields = '__all__'


