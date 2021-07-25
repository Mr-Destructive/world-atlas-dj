from rest_framework import generics,status
from .serializers import PlaceASerializer,PlaceBSerializer, PlaceListSerializer #, RoomSerializer, CreateRoomSerializer, 
from .models import A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z#Room 
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view

# Create your views here.
class ifPlace(APIView):
    def get(self, request, place):
        if place[0] == 'a':
            if A.objects.filter(a=place).exists():
                return JsonResponse({'result':True})
            else:
                return JsonResponse({'result':False})

class PlaceList(APIView):
    def get(self, request):
        place=Atlas.objects.all()
        serializer = PlaceListSerializer(place, many=True)
        return Response(serializer.data)

class getPlace(APIView):
    def get(self, request,letter):
        place=Atlas.objects.get(place=letter)
        serializer = getPlaceSerializer(place, many=False)
        return Response(serializer.data)

'''
class Place(APIView):
    serializer_class = PlaceSerializer
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        place= Atlas(place=place)
        place.save()
            
        return Response(RoomSerializer(place).data,status=status.HTTP_201_CREATED)
    

class RoomList(APIView):
    def get(self,request):
        Room1 = Room.objects.all()
        serializer = RoomSerializer(Room1,many=True)
        return Response(serializer.data)
    
class RoomView(APIView):
    def get(self,request,id):
        room= Room.objects.get(id=id)
        serializer = RoomSerializer(room,many=False)
        return Response(serializer.data)

    def delete(self,request,id):
        room=Room.objects.get(id=id)
        room.delete()
        return Response(serializer.data)

        

class CreateRoomView(APIView):

    serializer_class = CreateRoomSerializer
    def post(self,request,format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name=serializer.data.get('name')
            host=self.request.session.session_key
            code = serializer.data.get('code')
            queryset = Room.objects.filter(host=host)
            if queryset.exists():
                room = queryset[0]
                room.name=name
                room.save(update_fields=['name'])
            else:
                room = Room(host=host, name=name )
                room.save()
            
            return Response(RoomSerializer(room).data,status=status.HTTP_201_CREATED)

        return Response(RoomSerializer(room).data,status=status.HTTP_200_OK)

    def delete(self,request,id):
        room=Room.objects.get(id=id)
        room.delete()
        return Response(serializer.data)
'''
