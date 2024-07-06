from django.db import models

class Animal(models.Model):
    name = models.CharField(max_length=255)
    scientific_name = models.CharField(max_length=255, blank=True, null=True)
    habitat = models.CharField(max_length=255, blank=True, null=True)
    diet = models.CharField(max_length=255, blank=True, null=True)

class FavoriteList(models.Model):
    name = models.CharField(max_length=255)
    animals = models.ManyToManyField(Animal, related_name='favorite_lists')

