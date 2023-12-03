from django.urls import path
from .views import create_game_room, join_game_room, game_room, make_move

urlpatterns = [
    path('create/', create_game_room, name='create_game_room'),
    path('join/<int:room_id>/', join_game_room, name='join_game_room'),
    path('<int:room_id>/', game_room, name='game_room'),
    path('<int:room_id>/make_move/', make_move, name='make_move'),
]