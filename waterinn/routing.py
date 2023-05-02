from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path,include
from devices.consumers import EchoConsumer
# from rest_framework import routers
# router = routers.DefaultRouter()

application = ProtocolTypeRouter({
    'websocket': URLRouter([
        path('ws/chat/', EchoConsumer()),
        # path('ws/chat/', include(router.urls)),
    ])
})
