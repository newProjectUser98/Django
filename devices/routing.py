from django.urls import re_path

from . import views

websocket_urlpatterns = [
    re_path(r'', views.EchoConsumer.as_asgi()),
]