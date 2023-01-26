import random
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

from play.serializers import PlaceSerializer

from .models import Places, Room

class PlaceViewSet(ModelViewSet):
    queryset = Places.objects.all()
    serializer_class = PlaceSerializer

    @action(detail=False, methods=['GET',], url_path='lists/(?P<letter>[^/.]+)')
    def lists(self, request, letter:str):
        places = Places.objects.filter(name__startswith=letter).values_list(
            "name", flat=True
        )
        return JsonResponse({letter: list(places)})
    
    @action(detail=False, methods=['GET',], url_path='get/(?P<letter>[^/.]+)')
    def get_random_place(self, request, letter):
        places = Places.objects.filter(name__startswith=letter).values_list('name', flat=True)
        place = random.choice(places)
        return JsonResponse({letter: place})
    
    @action(detail=False, methods=['GET',], url_path='exists/(?P<place>[^/.]+)')
    def place_exists(self, request, place):
        place = place.lower()
        place_exists = Places.objects.filter(name=place).exists()
        if place_exists:
            return JsonResponse({"result": True})
        else:
            return JsonResponse({"result": False})

def home(request):
    return render(request,'index.html')

def play(request):
    return render(request,'play/index.html')

def bot(request):
    return render(request,'play/bot.html')

def multiplayer(request):
    return render(request, 'play/multiplayer.html')

def world_atlas_room(request, name):
    room = Room.objects.get(slug=name)
    return render(request, 'play/room.html', {'name': room.name, 'slug': room.slug})

def world_atlas_room_create(request):
    #create a room
    if request.method == "POST":
        room_name = request.POST["room_name"]
        room_slug= room_name.replace(' ', '_').replace("'", "_")
        room = Room.objects.create(name=room_name, slug=room_slug)
        return redirect(reverse('world-atlas-room', kwargs={'name': room.slug}))
    else:
        return render(request, 'play/user-room.html')

def world_atlas_room_join(request):
    if request.method == "POST":
        room_name = request.POST["room_name"]
        room = Room.objects.get(name=room_name)
        return redirect(reverse('world-atlas-room', kwargs={'name': room.slug}))
    else:
        return render(request, 'play/user-join.html')

