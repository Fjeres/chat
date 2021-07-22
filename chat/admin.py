from django.contrib import admin
from chat.models import *


# Register your models here.


class MessageAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'channel')
    list_display_links = ('nickname',)
    search_fields = ("nickname",)


admin.site.register(Message, MessageAdmin)
