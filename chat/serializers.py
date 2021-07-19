from rest_framework import serializers
from chat.models import Message
from django.contrib.auth.models import User


# Message Serializer
class MessageSerializer(serializers.ModelSerializer):
    """For Serializing Message"""
    nickname = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())
    channel = serializers.IntegerField()
    message = serializers.CharField(max_length=1200)

    class Meta:
        model = Message
        fields = ['nickname', 'channel', 'message', 'timestamp']
