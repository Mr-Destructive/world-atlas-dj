from django.urls import path
from . import views

urlpatterns=[
        path('play',views.play,name="play"),
        path('',views.home,name=""),
        path('bot',views.bot,name="bot"),
        ]
