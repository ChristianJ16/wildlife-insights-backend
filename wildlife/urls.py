from django.urls import path
from .views import (
    get_animal_info,
    FavoriteListListCreateAPIView,
    FavoriteListRetrieveUpdateDestroyAPIView,
    add_animal_to_list,
)

urlpatterns = [
    path('animal/', get_animal_info),
    path('favorite-lists/', FavoriteListListCreateAPIView.as_view()),
    path('favorite-lists/<int:pk>/', FavoriteListRetrieveUpdateDestroyAPIView.as_view()),
    path('favorite-lists/<int:pk>/add-animal/', add_animal_to_list),
]


