from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Room

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

