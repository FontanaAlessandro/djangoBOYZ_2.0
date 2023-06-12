from django.urls import path
from .views import *
app_name="blog"

urlpatterns = [
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('', post_list, name='post_list'),
]

