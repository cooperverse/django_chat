from django.shortcuts import render
from rest_framework import generics
from .models import Message
from .serializers import MessageSerializer

class ChatHistoryListView(generics.ListAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        room_name = self.kwargs.get('room_name')
        return Message.objects.filter(room=room_name).order_by('-timestamp')