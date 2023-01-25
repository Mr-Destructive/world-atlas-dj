from django.urls import path
from . import views

urlpatterns=[
        path('',views.home,name="home"),
        path('play/',views.play,name="play"),
        path('bot/',views.bot,name="bot"),
        path('room/',views.multiplayer,name="world-atlas-room"),
        path("room/wa/<str:name>/", views.world_atlas_room, name='world-atlas-room-index'),
        path("room/create/", views.world_atlas_room_create, name='world-atlas-room-create'),
        path("room/join/", views.world_atlas_room_join, name='world-atlas-room-join'),
]        
