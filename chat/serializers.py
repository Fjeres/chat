from rest_framework import serializers
from chat.models import Message


# Message Serializer
class MessageSerializer(serializers.ModelSerializer):
    """For Serializing Message"""
    nickname = serializers.CharField(max_length=100)
    channel = serializers.IntegerField()
    message = serializers.CharField(max_length=1200)

    class Meta:
        model = Message
        fields = ['nickname', 'channel', 'message', 'timestamp']
