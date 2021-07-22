from django.db import models



class Message(models.Model):
    nickname = models.CharField(max_length=100)
    channel = models.IntegerField()
    message = models.CharField(max_length=1200)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message

    class Meta:
        ordering = ('timestamp',)
