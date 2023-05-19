# """
# ASGI config for waterinn project.

# It exposes the ASGI callable as a module-level variable named ``application``.

# For more information on this file, see
# https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
# """

# import os

# from django.core.asgi import get_asgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'waterinn.settings')

# application = get_asgi_application()


# import os
# from django.core.asgi import get_asgi_application
# from channels.routing import ProtocolTypeRouter, URLRouter
# from django.urls import include
# # from .routing import websocket_urlpatterns
# from waterinn.routing import websocket_urlpatterns
# # from waterinn.routing import websocket_urlpatterns

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'waterinn.settings')

# # django_asgi_app = get_asgi_application()

# # application = ProtocolTypeRouter({
# #     "http": django_asgi_app,
# #     "websocket": URLRouter(websocket_urlpatterns)
# # })

# # # Add Django views to the ASGI application
# # application = get_asgi_application()
# # application = ProtocolTypeRouter({
# #     'http': get_asgi_application(),
# #     'websocket': URLRouter(websocket_urlpatterns)
# # })

# application = ProtocolTypeRouter({
#     'http': get_asgi_application(),
#     'websocket': URLRouter(websocket_urlpatterns),
# })
# import os
# from django.core.asgi import get_asgi_application
# from channels.routing import ProtocolTypeRouter, URLRouter
# from .routing import websocket_urlpatterns

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'waterinn.settings')

# application = ProtocolTypeRouter({
#     'http': get_asgi_application(),
#     'websocket': URLRouter(websocket_urlpatterns),
# })







# import os
# from django.core.asgi import get_asgi_application
# from channels.routing import ProtocolTypeRouter, URLRouter
# from channels.auth import AuthMiddlewareStack
# import waterinn.routing

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "waterinn.settings")

# application = ProtocolTypeRouter(
#     {
#         "http": get_asgi_application(),
#         "websocket": AuthMiddlewareStack(
#             URLRouter(
#                 waterinn.routing.websocket_urlpatterns
#             )
#         ),
#     }
# )


# websocket_project/asgi.py

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
import devices.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'waterinn.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter(devices.routing.websocket_urlpatterns),
})


# $ daphne waterinn.asgi:application
