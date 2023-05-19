import os
from django.core.asgi import get_asgi_application
from daphne.server import Server

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'waterinn.settings')

application = get_asgi_application()
server = Server(application)

if __name__ == '__main__':
    server.run()
