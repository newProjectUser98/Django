# from channels.routing import ProtocolTypeRouter, URLRouter
# from django.urls import path,include
# # from devices.consumers import EchoConsumer
# from devices.views import EchoConsumer
# # from rest_framework import routers
# # router = routers.DefaultRouter()




# application = ProtocolTypeRouter({
#     'websocket': URLRouter([
#         # path('ws/chat/', EchoConsumer()),
#         path('', EchoConsumer()),
#         # path('ws/chat/', include(router.urls)),
#     ])
# })
# ******************************************************************
# from django.urls import path
# from devices.consumers import MyConsumer

# websocket_urlpatterns = [
#     path('', MyConsumer.as_asgi()),
# ]


from django.urls import re_path

from devices import views

websocket_urlpatterns = [
    re_path(r'', views.EchoConsumer.as_asgi()),
]