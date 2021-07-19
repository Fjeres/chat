# chat/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import User
from chat.views import *


class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Получение сообщения от сокета
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)

        message = text_data_json['message']
        username = text_data_json['username']
        channel = text_data_json['channel']
        data = {"nickname": username,
                "channel": channel,
                "message": message
                }
        await update_data_base(data)
        # Send message to room group

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username,
                'channel': channel,
            }
        )

        # Receive message from room group

    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        channel = event['channel']

        # Отправить сообщение в WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'channel': channel,

        }))
