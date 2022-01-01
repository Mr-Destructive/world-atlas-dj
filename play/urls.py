from django.urls import path
from . import views

urlpatterns=[
        path('play/',views.play,name="play"),
        path('bot/',views.bot,name="bot"),
        path('room/',views.multiplayer,name="multp"),
        ]
