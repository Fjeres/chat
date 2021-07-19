from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    nickname = models.ForeignKey(User, on_delete=models.CASCADE, related_name='nickname')
    channel = models.IntegerField()
    message = models.CharField(max_length=1200)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message

    class Meta:
        ordering = ('timestamp',)
