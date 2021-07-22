from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from chat.models import Message  # Our Message model
from chat.serializers import MessageSerializer
from asgiref.sync import sync_to_async


# Create your views here.
def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })


@csrf_exempt
def message_list(request, nickname=None):
    if request.method == 'GET':
        messages = Message.objects.filter(nickname=nickname)
        serializer = MessageSerializer(messages, many=True, context={'request': request})
        return JsonResponse(serializer.data, safe=False, status=200)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MessageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@sync_to_async
def update_data_base(data):
    serializer = MessageSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
