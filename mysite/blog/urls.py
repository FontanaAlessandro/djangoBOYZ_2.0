from django import views
from django.contrib import admin
from django.urls import include, path
from .views import *
from . import views

app_name="blog"

urlpatterns = [
    #path('post/<int:pk>/', post_detail, name='post_detail'),
    path('<int:user_pk>/', chat_list, name='chat_list'),
    path('api/get-users/', api_get_users, name='api get users'),    
    path('api/get-message/', api_get_message, name='api get message'),
    path('api/ricevi-messaggio',riceviMessaggio, name='ricevi_messaggio'),
    path("admin/", admin.site.urls),
    path("chat/<str:room>/", chat_room, name="chat_room"),
    path('', chat_list, name='chat_list'),
]

