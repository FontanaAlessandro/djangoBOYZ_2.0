from django.contrib import admin
from .models import Post
from .models import Chat
from .models import ChatMessage


class ChatMessageInline(admin.TabularInline):
    model = ChatMessage


class ChatAdmin(admin.ModelAdmin):
    inlines = [
        ChatMessageInline,
    ]
admin.site.register(Post)
admin.site.register(Chat)

admin.site.register(ChatMessage)