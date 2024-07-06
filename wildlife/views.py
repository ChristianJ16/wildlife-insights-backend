import os
import requests
from dotenv import load_dotenv
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .models import FavoriteList, Animal
from .serializers import FavoriteListSerializer, AnimalSerializer

load_dotenv()
RAPIDAPI_KEY = os.getenv('RAPIDAPI_KEY')

@api_view(['GET'])
def get_animal_info(request):
    animal_name = request.GET.get('name')
    if not animal_name:
        return Response({"error": "No animal name provided"}, status=400)

    url = "https://animals-by-api-ninjas.p.rapidapi.com/v1/animals"
    querystring = {"name": animal_name}
    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": "animals-by-api-ninjas.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code != 200:
        return Response({"error": "Failed to fetch data from API"}, status=response.status_code)

    return Response(response.json())

class FavoriteListListCreateAPIView(generics.ListCreateAPIView):
    queryset = FavoriteList.objects.all()
    serializer_class = FavoriteListSerializer

class FavoriteListRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FavoriteList.objects.all()
    serializer_class = FavoriteListSerializer

@api_view(['POST'])
def add_animal_to_list(request, pk):
    try:
        list_instance = FavoriteList.objects.get(pk=pk)
    except FavoriteList.DoesNotExist:
        return Response({"error": "Favorite list not found"}, status=404)
    
    animal_data = request.data.get('animal')
    if not animal_data:
        return Response({"error": "No animal data provided"}, status=400)

    animal, created = Animal.objects.get_or_create(
        name=animal_data.get('name'),
        defaults={
            'scientific_name': animal_data.get('scientific_name'),
            'habitat': animal_data.get('habitat'),
            'diet': animal_data.get('diet'),
        },
    )
    list_instance.animals.add(animal)
    return Response(FavoriteListSerializer(list_instance).data)

@api_view(['POST'])
def add_animal_to_favorite_list(request, pk):
    try:
        favorite_list = FavoriteList.objects.get(pk=pk)
    except FavoriteList.DoesNotExist:
        return Response({"error": "Favorite list not found"}, status=404)

    animal_data = request.data.get('animal')
    if not animal_data:
        return Response({"error": "No animal data provided"}, status=400)

    animal, created = Animal.objects.get_or_create(
        name=animal_data.get('name'),
        defaults={
            'scientific_name': animal_data.get('scientific_name'),
            'habitat': animal_data.get('habitat'),
            'diet': animal_data.get('diet'),
        }
    )

    favorite_list.animals.add(animal)
    favorite_list.save()

    return Response({"success": "Animal added to the favorite list"}, status=200)
