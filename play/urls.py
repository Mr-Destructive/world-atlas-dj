from django.urls import include, path
from django.views.generic import TemplateView

from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register("places", views.PlaceViewSet)


urlpatterns=[
        path('',views.home,name="home"),
        path("api/", TemplateView.as_view(template_name='world-atlas-api.html')),
        path("api/", include(router.urls), name='api'),
        path('play/',views.play,name="play"),
        path('bot/',views.bot,name="bot"),
        path('room/',views.multiplayer,name="world-atlas-room"),
        path("room/wa/<str:name>/", views.world_atlas_room, name='world-atlas-room-index'),
        path("room/create/", views.world_atlas_room_create, name='world-atlas-room-create'),
        path("room/join/", views.world_atlas_room_join, name='world-atlas-room-join'),
]        
