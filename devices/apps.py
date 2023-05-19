# from django.apps import AppConfig


# class DevicesConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'devices'
from django.apps import AppConfig

class DevicesConfig(AppConfig):
    name = 'devices'

    # def ready(self):
    #     from devices import async_code
    #     async_code.setup()
