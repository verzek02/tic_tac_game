from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import GameRoom
from .forms import MoveForm

@login_required
def create_game_room(request):
    pass

@login_required
def join_game_room(request, room_id):
    pass

@login_required
def game_room(request, room_id):
    pass

@login_required
def make_move(request, room_id):
    pass
