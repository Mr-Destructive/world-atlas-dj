from django.urls import path
from .views import ifPlace, getPlace, PlaceList #RoomView,RoomList,CreateRoomView, 
urlpatterns = [
        #path('', PlaceList.as_view(), name='placelist'),
        #path('/<str:letter>', getPlace.as_view(), name='list'),
        path('/<str:place>', ifPlace.as_view(), name='tf'),
        
        #path('/room-<str:id>',RoomView.as_view(),name="code"),
        #path('/create',CreateRoomView.as_view(),name="create"),
        #path('/delete-<str:id>',RoomView.as_view(),name="delete"),
        ]


