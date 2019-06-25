from django.db.models import Q

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from django.contrib.auth.models import User

from chat_room.models import Room, Chat
from chat_room.serializers import (RoomSerializers, ChatSerializers, ChatPostSerializers,  UserSerializer)


class Rooms(APIView):
    """Комнаты чата"""
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        print('request',request)
        rooms = Room.objects.filter(Q(creater=request.user) | Q(invited=request.user))
        serializer = RoomSerializers(rooms, many=True)
        return Response({"data": serializer.data})

    def post(self, request):
        Room.objects.create(creater=request.user)
        return Response(status=201)


class Dialog(APIView):
    permission_classes =[permissions.IsAuthenticated]
    # permission_classes = [permissions.AllowAny]

    def get(self,request):
        print('request_dialog', request)
        room = request.GET.get('room')
        print('room',room)
        chat = Chat.objects.filter(room=room)
        serializer = ChatSerializers(chat,many=True)
        return Response({'data':serializer.data})


    def post(self,request):
        # room = request.data.get('room')
        dialog = ChatPostSerializers(data=request.data)
        if dialog.is_valid():
            dialog.save(user=request.user)
            return Response({'status':'add'})
        else:
            return Response({'status':'error'})

