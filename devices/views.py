from django.shortcuts import render
from .models import *
from django.utils import timezone
from dateutil.relativedelta import relativedelta
import datetime
import pytz
import json
import ast
from rest_framework import viewsets
from tzlocal import get_localzone # $ pip install tzlocal
from channels.generic.websocket import AsyncWebsocketConsumer
import asyncio
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.http import HttpResponse,Http404
from channels.generic.websocket import WebsocketConsumer
import json
import time

from django.http import HttpResponse, Http404
from datetime import datetime

# get local timezone    
local_tz = get_localzone()

from .serializers import *
msgo="hello"
from django.http import JsonResponse
from .mqttconn import client as mqtt_client
from channels.consumer import SyncConsumer
from devices.views import msgo
import json

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from channels.consumer import StopConsumer

import traceback
from django.shortcuts import render
from channels.generic.websocket import AsyncWebsocketConsumer


channel_layer = get_channel_layer()
eg=''
# set DJANGO_SETTINGS_MODULE=waterinn.settings
from django_init import *

# Now you can access Django settings and models
from django.conf import settings
from django.contrib.auth.models import User

# Use settings and models as needed

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'waterinn.settings')
django.setup()



def send_error_message_to_websocket(error_message):
    # Establish a WebSocket connection
    # websocket_url = "ws://localhost:8000/ws/echo/"  # Replace with your WebSocket URL
    websocket_url = "ws://localhost:8000/"  # Replace with your WebSocket URL
    # Send the error message as a WebSocket message
    # You can use a WebSocket client library or Django Channels to send the message
    # Example using Django Channels:
    from channels.layers import get_channel_layer
    from asgiref.sync import async_to_sync

    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.send)("websocket_send", {"type": "websocket.send", "text": error_message})




# def send_exception_message(error_message):
#     message = {
#         'type': 'websocket.send',
#         'text': error_message
#     }
#     async_to_sync(channel_layer.group_send)('websocket.send', message)

# class EchoConsumer(SyncConsumer):
#     def websocket_connect(self, event):
#         print("connect event is called")

#         self.send({
#             'type': 'websocket.accept'
#         })

#     def websocket_receive(self, event):
#         print("event in receive", event)
#         # msg=input("Enter message: ")
#         # msg=input("Enter masage:")
#         msg=input("Enter msg:")
#         if msg:
#             try:
#             # Simulate an exception
#              1 / 0
#             except Exception as e:
#                 # Send the exception message to the WebSocket client
#                 self.send({
#                     'type': 'websocket.send',
#                      # 'text': event.get('text')
#                     'text': str(e),
                    
#                 })


#             # self.send({
#             #     'type': 'websocket.send',
#             #     # 'text': event.get('text')
#             #     'text': msg
#             # })
#             self.websocket_receive(event)

#     def websocket_disconnect(self, event):
#         print("connection is disconnected")


#     async def send_exception(self, exception):
#         await self.send_json({
#             'type': 'exception',
#             'message': str(exception),
#         })
    # def disconnect(self, close_code):
    # # Leave room group
    #     async_to_sync(self.channel_layer.group_discard)(
    #         self.room_group_name,
    #         self.channel_name
    #     )
    #     raise StopConsumer()


# from channels.generic.websocket import AsyncWebsocketConsumer

# class MyConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         await self.accept()

#     async def disconnect(self, close_code):
#         pass

#     async def receive(self, text_data):
#         await self.send(text_data="You said: " + text_data)
# from waterinn import mqttconn.mqttconn
# from mqttconn.mqtt import client as mqtt_client
# from mqttconn import mqtt
# Create your views here.
# from pymongo import MongoClient
# # connection_string = mongodb+srv://<username>:<password>@<atlas cluster>
# # /<myFirstDatabase>?retryWrites=true&w=majority
# client = pymongo.MongoClient('connection_string')
# db = client['db_name']


# makemyrx_db = client['sample_medicines']
# #collection object
# medicines_collection = makemyrx_db['medicinedetails']
# send=str()
#**************************************************************************
# msgo=0

##############################
# async def echo_consumer(websocket,receive, send):
#     await websocket.accept()
    
#     while True:
#         receive_data = await websocket.receive_text()
#         print("Received data:", receive_data)
        
#         # Process the received data or perform any other actions
        
#         # Example: Sending a response back to the client
#         response = f"You sent: {receive_data}"
#         await websocket.send_text(response)
###########################
from channels.consumer import SyncConsumer


msgo=str()
class EchoConsumer(SyncConsumer):
    def websocket_connect(self, event):
       
        print("connect event is called")

        self.send({
            'type': 'websocket.accept'
        })
    def websocket_receive(self, event):
       
        print("event in receive", event)
        # msg=input("Enter message: ")
        # print("Error is:",eg)
                # Send the exception message to the WebSocket client
        if eg:
           self.send({
                'type': 'websocket.send',
                # 'text': event.get('text')
                'text':str(eg),
                
            })
       
    
        
        

    def websocket_disconnect(self, event):
        print("connection is disconnected")

#     async def disconnect(self, close_code):
#  # Leave room group
#         async_to_sync(self.channel_layer.group_discard)(
#             self.room_group_name,
#             self.channel_name
#         )
#         raise StopConsumer()
    # ****************************************************************************  
# from channels.generic.websocket import AsyncWebsocketConsumer

# # class EchoConsumer(AsyncWebsocketConsumer):
# class MyConsumer(AsyncWebsocketConsumer):
#     async def websocket_connect(self, event):
#         print("Connect event is called")
#         await self.accept()

#     async def websocket_receive(self, event):
#         print("Event in receive", event)

#         # Process received message or perform any necessary actions
#         # eg = ...

#         if eg:
#             await self.send(text_data=str(eg))

#     async def disconnect(self, close_code):
#         # Perform any necessary cleanup or disconnection handling
#         pass
 
def dateandtime():
    year=datetime.today().strftime('%Y')
    month=datetime.today().strftime('%m')
    day=datetime.today().strftime('%d')
    hour=datetime.now().strftime('%H')
    minit=datetime.now().strftime('%M')
    second=datetime.now().strftime('%S')
    return year,month,day,hour,minit,second



qs={}

# class get_treat_rwpViewset(viewsets.ModelViewSet):
#     # define queryset
#         @action(detail=False, methods=['get'])
#         def get_rwp(self, request, *args, **kwargs):
#             data_dict = json.loads(request.body)
#             value_list = list(data_dict.values())
#             dinfo = device_info.objects.filter(componant_name=value_list[2], unit_type=value_list[0], company_name=value_list[1])
#             for x in dinfo:
#                 did = x.Device_id
#                 cmpname = x.componant_name
#             qs = treat_rwp.objects.filter(device_id=did).order_by('-id')[:1:1]
#             data = serialize("json", qs)
#             return Response(data)




class updated_treat_rwpViewset(viewsets.ModelViewSet):
    def dispatch(self, request, *args, **kwargs):
        try:
            did = 0
            data_dict = json.loads(request.body)
            value_list = list(data_dict.values())
            dinfo = device_info.objects.filter(componant_name=value_list[2], unit_type=value_list[0], company_name=value_list[1])
            
            for x in dinfo:
                did = x.Device_id
                cmpname = x.componant_name
            
            qs = treat_rwp.objects.filter(device_id=did).order_by('-id')[:1:1]
            fields_to_exclude = ['model', 'pk']
            
            data = serialize("json", qs)
            data = json.loads(data)
            
            for item in data:
                item['fields'] = {k: v for k, v in item['fields'].items() if k not in fields_to_exclude}
            
            
            if not data:
                response_data = {
                    'data': [],  # Include the 'data' field
                    'status': 200,  # Add the status field
                    'message': "Data not found"  # Add the message field
                }
            else:     
                data = json.dumps(data[0]["fields"])
                data = json.loads(data)
                data = [data]
                response_data = {
                    'data': data[0],  # Include the 'data' field
                    'status': 200,  # Add the status field
                    'message': "Data get successfully"  # Add the message field
                }
            response_data=[response_data]
        except Exception as e:
                    response_data = {
                        'data':e,  # Include the 'data' field
                        'status': 200,  # Add the status field
                        'message': "Exception found"  # Add the message field
                    }
        
        return JsonResponse(response_data, safe=False, content_type="application/json")



class updated_treat_cnd_tds_senViewset(viewsets.ModelViewSet):
	# define queryset
        
    def dispatch(self, request, *args, **kwargs):
        try:
            did = 0
            data_dict = json.loads(request.body)
            value_list = list(data_dict.values())
            dinfo = device_info.objects.filter(componant_name=value_list[2], unit_type=value_list[0], company_name=value_list[1])
            
            for x in dinfo:
                did = x.Device_id
                cmpname = x.componant_name
            
            qs = treat_cnd_tds_sen.objects.filter(device_id=did).order_by('-id')[:1:1]
            fields_to_exclude = ['model', 'pk']
            
            data = serialize("json", qs)
            data = json.loads(data)
            
            for item in data:
                item['fields'] = {k: v for k, v in item['fields'].items() if k not in fields_to_exclude}
            
            
            if not data:
                response_data = {
                    'data': [],  # Include the 'data' field
                    'status': 200,  # Add the status field
                    'message': "Data not found"  # Add the message field
                }
            else:     
                data = json.dumps(data[0]["fields"])
                data = json.loads(data)
                data = [data]
                response_data = {
                    'data': data[0],  # Include the 'data' field
                    'status': 200,  # Add the status field
                    'message': "Data get successfully"  # Add the message field
                }
            response_data=[response_data]
        except Exception as e:
                    response_data = {
                        'data':e,  # Include the 'data' field
                        'status': 200,  # Add the status field
                        'message': "Exception found"  # Add the message field
                    }
        
        return JsonResponse(response_data, safe=False, content_type="application/json")


class updated_treat_hppViewset(viewsets.ModelViewSet):
	# define queryset
                            
    def dispatch(self, request, *args, **kwargs):
        try:
            did = 0
            data_dict = json.loads(request.body)
            value_list = list(data_dict.values())
            dinfo = device_info.objects.filter(componant_name=value_list[2], unit_type=value_list[0], company_name=value_list[1])
            
            for x in dinfo:
                did = x.Device_id
                cmpname = x.componant_name
            
            qs = treat_hpp.objects.filter(device_id=did).order_by('-id')[:1:1]
            fields_to_exclude = ['model', 'pk']
            
            data = serialize("json", qs)
            data = json.loads(data)
            
            for item in data:
                item['fields'] = {k: v for k, v in item['fields'].items() if k not in fields_to_exclude}
            
            
            if not data:
                response_data = {
                    'data': [],  # Include the 'data' field
                    'status': 200,  # Add the status field
                    'message': "Data not found"  # Add the message field
                }
            else:     
                data = json.dumps(data[0]["fields"])
                data = json.loads(data)
                data = [data]
                response_data = {
                    'data': data[0],  # Include the 'data' field
                    'status': 200,  # Add the status field
                    'message': "Data get successfully"  # Add the message field
                }
            response_data=[response_data]
        except Exception as e:
                    response_data = {
                        'data':e,  # Include the 'data' field
                        'status': 200,  # Add the status field
                        'message': "Exception found"  # Add the message field
                    }
        
        return JsonResponse(response_data, safe=False, content_type="application/json")


class updated_treat_ampv1Viewset(viewsets.ModelViewSet):
	# define queryset
    def dispatch(self, request, *args, **kwargs):
        try:
            did = 0
            data_dict = json.loads(request.body)
            value_list = list(data_dict.values())
            dinfo = device_info.objects.filter(componant_name=value_list[2], unit_type=value_list[0], company_name=value_list[1])
            
            for x in dinfo:
                did = x.Device_id
                cmpname = x.componant_name
            
            qs = treat_ampv1.objects.filter(device_id=did).order_by('-id')[:1:1]
            fields_to_exclude = ['model', 'pk']
            
            data = serialize("json", qs)
            data = json.loads(data)
            
            for item in data:
                item['fields'] = {k: v for k, v in item['fields'].items() if k not in fields_to_exclude}
            
            
            if not data:
                response_data = {
                    'data': [],  # Include the 'data' field
                    'status': 200,  # Add the status field
                    'message': "Data not found"  # Add the message field
                }
            else:     
                data = json.dumps(data[0]["fields"])
                data = json.loads(data)
                data = [data]
                response_data = {
                    'data': data[0],  # Include the 'data' field
                    'status': 200,  # Add the status field
                    'message': "Data get successfully"  # Add the message field
                }
            response_data=[response_data]
        except Exception as e:
                    response_data = {
                        'data':e,  # Include the 'data' field
                        'status': 200,  # Add the status field
                        'message': "Exception found"  # Add the message field
                    }
        
        return JsonResponse(response_data, safe=False, content_type="application/json")


class updated_treat_ampv2Viewset(viewsets.ModelViewSet):
	# define queryset
    def dispatch(self, request, *args, **kwargs):
        try:
            did = 0
            data_dict = json.loads(request.body)
            value_list = list(data_dict.values())
            dinfo = device_info.objects.filter(componant_name=value_list[2], unit_type=value_list[0], company_name=value_list[1])
            
            for x in dinfo:
                did = x.Device_id
                cmpname = x.componant_name
            
            qs = treat_ampv2.objects.filter(device_id=did).order_by('-id')[:1:1]
            fields_to_exclude = ['model', 'pk']
            
            data = serialize("json", qs)
            data = json.loads(data)
            
            for item in data:
                item['fields'] = {k: v for k, v in item['fields'].items() if k not in fields_to_exclude}
            
            
            if not data:
                response_data = {
                    'data': [],  # Include the 'data' field
                    'status': 200,  # Add the status field
                    'message': "Data not found"  # Add the message field
                }
            else:     
                data = json.dumps(data[0]["fields"])
                data = json.loads(data)
                data = [data]
                response_data = {
                    'data': data[0],  # Include the 'data' field
                    'status': 200,  # Add the status field
                    'message': "Data get successfully"  # Add the message field
                }
            response_data=[response_data]
        except Exception as e:
                    response_data = {
                        'data':e,  # Include the 'data' field
                        'status': 200,  # Add the status field
                        'message': "Exception found"  # Add the message field
                    }
        
        return JsonResponse(response_data, safe=False, content_type="application/json")

    

class updated_treat_panelViewset(viewsets.ModelViewSet):
	# define queryset
    def dispatch(self, request, *args, **kwargs):
        try:
            did = 0
            data_dict = json.loads(request.body)
            value_list = list(data_dict.values())
            dinfo = device_info.objects.filter(componant_name=value_list[2], unit_type=value_list[0], company_name=value_list[1])
            
            for x in dinfo:
                did = x.Device_id
                cmpname = x.componant_name
            
            qs = treat_panel.objects.filter(device_id=did).order_by('-id')[:1:1]
            fields_to_exclude = ['model', 'pk']
            
            data = serialize("json", qs)
            data = json.loads(data)
            
            for item in data:
                item['fields'] = {k: v for k, v in item['fields'].items() if k not in fields_to_exclude}
            
            
            if not data:
                response_data = {
                    'data': [],  # Include the 'data' field
                    'status': 200,  # Add the status field
                    'message': "Data not found"  # Add the message field
                }
            else:     
                data = json.dumps(data[0]["fields"])
                data = json.loads(data)
                data = [data]
                response_data = {
                    'data': data[0],  # Include the 'data' field
                    'status': 200,  # Add the status field
                    'message': "Data get successfully"  # Add the message field
                }
            response_data=[response_data]
        except Exception as e:
                    response_data = {
                        'data':e,  # Include the 'data' field
                        'status': 200,  # Add the status field
                        'message': "Exception found"  # Add the message field
                    }
        
        return JsonResponse(response_data, safe=False, content_type="application/json")

class updated_treat_flowsenViewset(viewsets.ModelViewSet):
	# define queryset
    def dispatch(self, request, *args, **kwargs):
        try:
            did = 0
            data_dict = json.loads(request.body)
            value_list = list(data_dict.values())
            dinfo = device_info.objects.filter(componant_name=value_list[2], unit_type=value_list[0], company_name=value_list[1])
            
            for x in dinfo:
                did = x.Device_id
                cmpname = x.componant_name
            
            qs = treat_flowsen.objects.filter(device_id=did).order_by('-id')[:1:1]
            fields_to_exclude = ['model', 'pk']
            
            data = serialize("json", qs)
            data = json.loads(data)
            
            for item in data:
                item['fields'] = {k: v for k, v in item['fields'].items() if k not in fields_to_exclude}
            
            
            if not data:
                response_data = {
                    'data': [],  # Include the 'data' field
                    'status': 200,  # Add the status field
                    'message': "Data not found"  # Add the message field
                }
            else:     
                data = json.dumps(data[0]["fields"])
                data = json.loads(data)
                data = [data]
                response_data = {
                    'data': data[0],  # Include the 'data' field
                    'status': 200,  # Add the status field
                    'message': "Data get successfully"  # Add the message field
                }
            response_data=[response_data]
        except Exception as e:
                    response_data = {
                        'data':e,  # Include the 'data' field
                        'status': 200,  # Add the status field
                        'message': "Exception found"  # Add the message field
                    }
        
        return JsonResponse(response_data, safe=False, content_type="application/json")


class updated_disp_atmViewset(viewsets.ModelViewSet):
	# define queryset
    def dispatch(self, request, *args, **kwargs):
        try:
            did = 0
            data_dict = json.loads(request.body)
            value_list = list(data_dict.values())
            dinfo = device_info.objects.filter(componant_name=value_list[2], unit_type=value_list[0], company_name=value_list[1])
            
            for x in dinfo:
                did = x.Device_id
                cmpname = x.componant_name
            
            qs = disp_atm.objects.filter(device_id=did).order_by('-id')[:1:1]
            fields_to_exclude = ['model', 'pk']
            
            data = serialize("json", qs)
            data = json.loads(data)
            
            for item in data:
                item['fields'] = {k: v for k, v in item['fields'].items() if k not in fields_to_exclude}
            
            
            if not data:
                response_data = {
                    'data': [],  # Include the 'data' field
                    'status': 200,  # Add the status field
                    'message': "Data not found"  # Add the message field
                }
            else:     
                data = json.dumps(data[0]["fields"])
                data = json.loads(data)
                data = [data]
                response_data = {
                    'data': data[0],  # Include the 'data' field
                    'status': 200,  # Add the status field
                    'message': "Data get successfully"  # Add the message field
                }
            response_data=[response_data]
        except Exception as e:
                    response_data = {
                        'data':e,  # Include the 'data' field
                        'status': 200,  # Add the status field
                        'message': "Exception found"  # Add the message field
                    }
        
        return JsonResponse(response_data, safe=False, content_type="application/json")


class updated_disp_tap1Viewset(viewsets.ModelViewSet):
	# define queryset
    def dispatch(self, request, *args, **kwargs):
        try:
            did = 0
            data_dict = json.loads(request.body)
            value_list = list(data_dict.values())
            dinfo = device_info.objects.filter(componant_name=value_list[2], unit_type=value_list[0], company_name=value_list[1])
            
            for x in dinfo:
                did = x.Device_id
                cmpname = x.componant_name
            
            qs = disp_tap1.objects.filter(device_id=did).order_by('-id')[:1:1]
            fields_to_exclude = ['model', 'pk']
            
            data = serialize("json", qs)
            data = json.loads(data)
            
            for item in data:
                item['fields'] = {k: v for k, v in item['fields'].items() if k not in fields_to_exclude}
            
            
            if not data:
                response_data = {
                    'data': [],  # Include the 'data' field
                    'status': 200,  # Add the status field
                    'message': "Data not found"  # Add the message field
                }
            else:     
                data = json.dumps(data[0]["fields"])
                data = json.loads(data)
                data = [data]
                response_data = {
                    'data': data[0],  # Include the 'data' field
                    'status': 200,  # Add the status field
                    'message': "Data get successfully"  # Add the message field
                }
            response_data=[response_data]
        except Exception as e:
                    response_data = {
                        'data':e,  # Include the 'data' field
                        'status': 200,  # Add the status field
                        'message': "Exception found"  # Add the message field
                    }
        
        return JsonResponse(response_data, safe=False, content_type="application/json")


class updated_disp_tap2Viewset(viewsets.ModelViewSet):
	# define queryset
    def dispatch(self, request, *args, **kwargs):
        try:
            did = 0
            data_dict = json.loads(request.body)
            value_list = list(data_dict.values())
            dinfo = device_info.objects.filter(componant_name=value_list[2], unit_type=value_list[0], company_name=value_list[1])
            
            for x in dinfo:
                did = x.Device_id
                cmpname = x.componant_name
            
            qs = disp_tap2.objects.filter(device_id=did).order_by('-id')[:1:1]
            fields_to_exclude = ['model', 'pk']
            
            data = serialize("json", qs)
            data = json.loads(data)
            
            for item in data:
                item['fields'] = {k: v for k, v in item['fields'].items() if k not in fields_to_exclude}
            
            
            if not data:
                response_data = {
                    'data': [],  # Include the 'data' field
                    'status': 200,  # Add the status field
                    'message': "Data not found"  # Add the message field
                }
            else:     
                data = json.dumps(data[0]["fields"])
                data = json.loads(data)
                data = [data]
                response_data = {
                    'data': data[0],  # Include the 'data' field
                    'status': 200,  # Add the status field
                    'message': "Data get successfully"  # Add the message field
                }
            response_data=[response_data]
        except Exception as e:
                    response_data = {
                        'data':e,  # Include the 'data' field
                        'status': 200,  # Add the status field
                        'message': "Exception found"  # Add the message field
                    }
        
        return JsonResponse(response_data, safe=False, content_type="application/json")


class updated_disp_tap3Viewset(viewsets.ModelViewSet):
	# define queryset
    def dispatch(self, request, *args, **kwargs):
        try:
            did = 0
            data_dict = json.loads(request.body)
            value_list = list(data_dict.values())
            dinfo = device_info.objects.filter(componant_name=value_list[2], unit_type=value_list[0], company_name=value_list[1])
            
            for x in dinfo:
                did = x.Device_id
                cmpname = x.componant_name
            
            qs = disp_tap3.objects.filter(device_id=did).order_by('-id')[:1:1]
            fields_to_exclude = ['model', 'pk']
            
            data = serialize("json", qs)
            data = json.loads(data)
            
            for item in data:
                item['fields'] = {k: v for k, v in item['fields'].items() if k not in fields_to_exclude}
            
            
            if not data:
                response_data = {
                    'data': [],  # Include the 'data' field
                    'status': 200,  # Add the status field
                    'message': "Data not found"  # Add the message field
                }
            else:     
                data = json.dumps(data[0]["fields"])
                data = json.loads(data)
                data = [data]
                response_data = {
                    'data': data[0],  # Include the 'data' field
                    'status': 200,  # Add the status field
                    'message': "Data get successfully"  # Add the message field
                }
            response_data=[response_data]
        except Exception as e:
                    response_data = {
                        'data':e,  # Include the 'data' field
                        'status': 200,  # Add the status field
                        'message': "Exception found"  # Add the message field
                    }
        
        return JsonResponse(response_data, safe=False, content_type="application/json")

class updated_disp_tap4Viewset(viewsets.ModelViewSet):
	# define queryset
    def dispatch(self, request, *args, **kwargs):
        try:
            did = 0
            data_dict = json.loads(request.body)
            value_list = list(data_dict.values())
            dinfo = device_info.objects.filter(componant_name=value_list[2], unit_type=value_list[0], company_name=value_list[1])
            
            for x in dinfo:
                did = x.Device_id
                cmpname = x.componant_name
            
            qs = disp_tap4.objects.filter(device_id=did).order_by('-id')[:1:1]
            fields_to_exclude = ['model', 'pk']
            
            data = serialize("json", qs)
            data = json.loads(data)
            
            for item in data:
                item['fields'] = {k: v for k, v in item['fields'].items() if k not in fields_to_exclude}
            
            
            if not data:
                response_data = {
                    'data': [],  # Include the 'data' field
                    'status': 200,  # Add the status field
                    'message': "Data not found"  # Add the message field
                }
            else:     
                data = json.dumps(data[0]["fields"])
                data = json.loads(data)
                data = [data]
                response_data = {
                    'data': data[0],  # Include the 'data' field
                    'status': 200,  # Add the status field
                    'message': "Data get successfully"  # Add the message field
                }
            response_data=[response_data]
        except Exception as e:
                    response_data = {
                        'data':e,  # Include the 'data' field
                        'status': 200,  # Add the status field
                        'message': "Exception found"  # Add the message field
                    }
        
        return JsonResponse(response_data, safe=False, content_type="application/json")


class updated_disp_consenViewset(viewsets.ModelViewSet):
	# define queryset
        
    def dispatch(self, request, *args, **kwargs):
        try:
            did = 0
            data_dict = json.loads(request.body)
            value_list = list(data_dict.values())
            dinfo = device_info.objects.filter(componant_name=value_list[2], unit_type=value_list[0], company_name=value_list[1])
            
            for x in dinfo:
                did = x.Device_id
                cmpname = x.componant_name
            
            qs = disp_consen.objects.filter(device_id=did).order_by('-id')[:1:1]
            fields_to_exclude = ['model', 'pk']
            
            data = serialize("json", qs)
            data = json.loads(data)
            
            for item in data:
                item['fields'] = {k: v for k, v in item['fields'].items() if k not in fields_to_exclude}
            
            
            if not data:
                response_data = {
                    'data': [],  # Include the 'data' field
                    'status': 200,  # Add the status field
                    'message': "Data not found"  # Add the message field
                }
            else:     
                data = json.dumps(data[0]["fields"])
                data = json.loads(data)
                data = [data]
                response_data = {
                    'data': data[0],  # Include the 'data' field
                    'status': 200,  # Add the status field
                    'message': "Data get successfully"  # Add the message field
                }
            response_data=[response_data]
        except Exception as e:
                    response_data = {
                        'data':e,  # Include the 'data' field
                        'status': 200,  # Add the status field
                        'message': "Exception found"  # Add the message field
                    }
        
        return JsonResponse(response_data, safe=False, content_type="application/json")


    
class updated_disp_flowsenViewset(viewsets.ModelViewSet):
	# define queryset
    def dispatch(self, request, *args, **kwargs):
        try:
            did = 0
            data_dict = json.loads(request.body)
            value_list = list(data_dict.values())
            dinfo = device_info.objects.filter(componant_name=value_list[2], unit_type=value_list[0], company_name=value_list[1])
            
            for x in dinfo:
                did = x.Device_id
                cmpname = x.componant_name
            
            qs = disp_flowsen.objects.filter(device_id=did).order_by('-id')[:1:1]
            fields_to_exclude = ['model', 'pk']
            
            data = serialize("json", qs)
            data = json.loads(data)
            
            for item in data:
                item['fields'] = {k: v for k, v in item['fields'].items() if k not in fields_to_exclude}
            
            
            if not data:
                response_data = {
                    'data': [],  # Include the 'data' field
                    'status': 200,  # Add the status field
                    'message': "Data not found"  # Add the message field
                }
            else:     
                data = json.dumps(data[0]["fields"])
                data = json.loads(data)
                data = [data]
                response_data = {
                    'data': data[0],  # Include the 'data' field
                    'status': 200,  # Add the status field
                    'message': "Data get successfully"  # Add the message field
                }
            response_data=[response_data]
        except Exception as e:
                    response_data = {
                        'data':e,  # Include the 'data' field
                        'status': 200,  # Add the status field
                        'message': "Exception found"  # Add the message field
                    }
        
        return JsonResponse(response_data, safe=False, content_type="application/json")


class cnd_tds_YearlyViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = cnd_tds_repo_yearly.objects.all()

	# specify serializer to be used
	serializer_class = cnd_tds_YearlySerializer
                
        
class cnd_tds_HourlyViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = cnd_tds_repo_hourly.objects.all()

	# specify serializer to be used
	serializer_class = cnd_tds_HourlySerializer
        
class cnd_tds_MonthlyViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = cnd_tds_repo_monthly.objects.all()

	# specify serializer to be used
	serializer_class = cnd_tds_MonthlySerializer
        
class cnd_tds_DailyViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = cnd_tds_repo_daily.objects.all()

	# specify serializer to be used
	serializer_class = cnd_tds_DailySerializer

class rwp_YearlyViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = rwp_repo_yearly.objects.all()

	# specify serializer to be used
	serializer_class = rwp_YearlySerializer
                
        
class rwp_HourlyViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = rwp_repo_hourly.objects.all()

	# specify serializer to be used
	serializer_class = rwp_HourlySerializer
        
class rwp_MonthlyViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = rwp_repo_monthly.objects.all()

	# specify serializer to be used
	serializer_class = rwp_MonthlySerializer
        
class rwp_DailyViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = rwp_repo_daily.objects.all()

	# specify serializer to be used
	serializer_class = rwp_DailySerializer

class hpp_YearlyViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = hpp_repo_yearly.objects.all()

	# specify serializer to be used
	serializer_class = hpp_YearlySerializer
                
        
class hpp_HourlyViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = hpp_repo_hourly.objects.all()

	# specify serializer to be used
	serializer_class = hpp_HourlySerializer
        
class hpp_MonthlyViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = hpp_repo_monthly.objects.all()

	# specify serializer to be used
	serializer_class = hpp_MonthlySerializer
        
class hpp_DailyViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = hpp_repo_daily.objects.all()

	# specify serializer to be used
	serializer_class = hpp_DailySerializer
        

class panel_YearlyViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = hpp_repo_yearly.objects.all()

	# specify serializer to be used
	serializer_class = hpp_YearlySerializer
                
        
class panel_HourlyViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = panel_repo_hourly.objects.all()

	# specify serializer to be used
	serializer_class = panel_HourlySerializer
        
class panel_MonthlyViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = panel_repo_monthly.objects.all()

	# specify serializer to be used
	serializer_class = panel_MonthlySerializer
        
class panel_DailyViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = panel_repo_daily.objects.all()

	# specify serializer to be used
	serializer_class = panel_DailySerializer
        

class flowsen_YearlyViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = flowsen_repo_yearly.objects.all()

	# specify serializer to be used
	serializer_class = flowsen_YearlySerializer
                
        
class flowsen_HourlyViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = flowsen_repo_hourly.objects.all()

	# specify serializer to be used
	serializer_class = flowsen_HourlySerializer
        
class flowsen_MonthlyViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = flowsen_repo_monthly.objects.all()

	# specify serializer to be used
	serializer_class = flowsen_MonthlySerializer
        
class flowsen_DailyViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = flowsen_repo_daily.objects.all()

	# specify serializer to be used
	serializer_class = flowsen_DailySerializer       
        

class ampv1_YearlyViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = ampv1_repo_yearly.objects.all()

	# specify serializer to be used
	serializer_class = ampv1_YearlySerializer
                
        
class ampv1_HourlyViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = ampv1_repo_hourly.objects.all()

	# specify serializer to be used
	serializer_class = ampv1_HourlySerializer
        
class ampv1_MonthlyViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = ampv1_repo_monthly.objects.all()

	# specify serializer to be used
	serializer_class = ampv1_MonthlySerializer
        
class ampv1_DailyViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = ampv1_repo_daily.objects.all()

	# specify serializer to be used
	serializer_class = ampv1_DailySerializer       
        
class ampv2_YearlyViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = ampv2_repo_yearly.objects.all()

	# specify serializer to be used
	serializer_class = ampv2_YearlySerializer
                
        
class ampv2_HourlyViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = ampv2_repo_hourly.objects.all()

	# specify serializer to be used
	serializer_class = ampv2_HourlySerializer
        
class ampv2_MonthlyViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = ampv2_repo_monthly.objects.all()

	# specify serializer to be used
	serializer_class = ampv2_MonthlySerializer
        
class ampv2_DailyViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = ampv2_repo_daily.objects.all()

	# specify serializer to be used
	serializer_class = ampv2_DailySerializer       
        
class ampv3_YearlyViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = ampv3_repo_yearly.objects.all()

	# specify serializer to be used
	serializer_class = ampv3_YearlySerializer
                
        
class ampv3_HourlyViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = ampv3_repo_hourly.objects.all()

	# specify serializer to be used
	serializer_class = ampv3_HourlySerializer
        
class ampv3_MonthlyViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = ampv3_repo_monthly.objects.all()

	# specify serializer to be used
	serializer_class = ampv3_MonthlySerializer
        
class ampv3_DailyViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = ampv3_repo_daily.objects.all()

	# specify serializer to be used
	serializer_class = ampv3_DailySerializer       
        
class ampv4_YearlyViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = ampv4_repo_yearly.objects.all()

	# specify serializer to be used
	serializer_class = ampv4_YearlySerializer
                
        
class ampv4_HourlyViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = ampv4_repo_hourly.objects.all()

	# specify serializer to be used
	serializer_class = ampv4_HourlySerializer
        
class ampv4_MonthlyViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = ampv4_repo_monthly.objects.all()

	# specify serializer to be used
	serializer_class = ampv4_MonthlySerializer
        
class ampv4_DailyViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = ampv4_repo_daily.objects.all()

	# specify serializer to be used
	serializer_class = ampv4_DailySerializer       
        
class ampv5_YearlyViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = ampv5_repo_yearly.objects.all()

	# specify serializer to be used
	serializer_class = ampv5_YearlySerializer
                
        
class ampv5_HourlyViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = ampv5_repo_hourly.objects.all()

	# specify serializer to be used
	serializer_class = ampv5_HourlySerializer
        
class ampv5_MonthlyViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = ampv5_repo_monthly.objects.all()

	# specify serializer to be used
	serializer_class = ampv5_MonthlySerializer
        
class ampv5_DailyViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = ampv5_repo_daily.objects.all()

	# specify serializer to be used
	serializer_class = ampv5_DailySerializer       
class tap1_YearlyViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = tap1_repo_yearly.objects.all()

	# specify serializer to be used
	serializer_class = tap1_YearlySerializer
                
        
class tap1_HourlyViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = tap1_repo_hourly.objects.all()

	# specify serializer to be used
	serializer_class = tap1_HourlySerializer
        
class tap1_MonthlyViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = tap1_repo_monthly.objects.all()

	# specify serializer to be used
	serializer_class = tap1_MonthlySerializer
        
class tap1_DailyViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = tap1_repo_daily.objects.all()

	# specify serializer to be used
	serializer_class = tap1_DailySerializer       
class tap2_YearlyViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = tap2_repo_yearly.objects.all()

	# specify serializer to be used
	serializer_class = tap2_YearlySerializer
                
        
class tap2_HourlyViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = tap2_repo_hourly.objects.all()

	# specify serializer to be used
	serializer_class = tap2_HourlySerializer
        
class tap2_MonthlyViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = tap2_repo_monthly.objects.all()

	# specify serializer to be used
	serializer_class = tap2_MonthlySerializer
        
class tap2_DailyViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = tap2_repo_daily.objects.all()

	# specify serializer to be used
	serializer_class = tap2_DailySerializer       
class tap3_YearlyViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = tap3_repo_yearly.objects.all()

	# specify serializer to be used
	serializer_class = tap3_YearlySerializer
                
        
class tap3_HourlyViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = tap3_repo_hourly.objects.all()

	# specify serializer to be used
	serializer_class = tap3_HourlySerializer
        
class tap3_MonthlyViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = tap3_repo_monthly.objects.all()

	# specify serializer to be used
	serializer_class = tap3_MonthlySerializer
        
class tap3_DailyViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = tap3_repo_daily.objects.all()

	# specify serializer to be used
	serializer_class = tap3_DailySerializer       
class tap4_YearlyViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = tap4_repo_yearly.objects.all()

	# specify serializer to be used
	serializer_class = tap4_YearlySerializer
                
        
class tap4_HourlyViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = tap4_repo_hourly.objects.all()

	# specify serializer to be used
	serializer_class = tap4_HourlySerializer
        
class tap4_MonthlyViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = tap4_repo_monthly.objects.all()

	# specify serializer to be used
	serializer_class = tap4_MonthlySerializer
        
class tap4_DailyViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = tap4_repo_daily.objects.all()

	# specify serializer to be used
	serializer_class = tap4_DailySerializer       
        
class consen_YearlyViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = consen_repo_yearly.objects.all()

	# specify serializer to be used
	serializer_class = tap4_YearlySerializer
                
        
class consen_HourlyViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = consen_repo_hourly.objects.all()

	# specify serializer to be used
	serializer_class = consen_HourlySerializer
        
class consen_MonthlyViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = consen_repo_monthly.objects.all()

	# specify serializer to be used
	serializer_class = consen_MonthlySerializer
        
class consen_DailyViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = consen_repo_daily.objects.all()

	# specify serializer to be used
	serializer_class = consen_DailySerializer


class atm_YearlyViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = atm_repo_yearly.objects.all()

	# specify serializer to be used
	serializer_class = atm_YearlySerializer
                
        
class atm_HourlyViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = atm_repo_hourly.objects.all()

	# specify serializer to be used
	serializer_class = atm_HourlySerializer
        
class atm_MonthlyViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = atm_repo_monthly.objects.all()

	# specify serializer to be used
	serializer_class = atm_MonthlySerializer
        
class atm_DailyViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = atm_repo_daily.objects.all()

	# specify serializer to be used
	serializer_class = atm_DailySerializer


# # import mongoengine
# # mongoengine.connect(db=waterinn, host=localhost:27017, username=username, password=pwc)
class TopicViewSet(viewsets.ModelViewSet):
	# define queryset
	queryset = topics.objects.all()

	# specify serializer to be used
	serializer_class = TopicSerializer
        
# graphdata = graph_info.objects.last()
# print("graph data is:",graphdata.service_name,graphdata.device_id)

# servi=graphdata.service_name
# ds_id=graphdata.device_id
# class YearlyViewset(viewsets.ModelViewSet):
# 	# define queryset
#     global servi,ds_id
#     queryset = cnd_tds_repo_yearly.objects.filter(service=servi,device_id=ds_id)
#     # graphdata = graph_info.objects.last()
#     # print("graph data is:",graphdata.service_name,graphdata.device_id)
    

# 	# specify serializer to be used
#     serializer_class = YearlySerializer
        
class DeviceViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = device_info.objects.all()

	# specify serializer to be used
	serializer_class = DeviceSerializer
        
class keyViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = key_info.objects.all()

	# specify serializer to be used
	serializer_class = KeySerializer
        
class RwpstateViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = Rwp_state.objects.all()

	# specify serializer to be used
	serializer_class = RwpstateSerializer

# def dosome():
#     response = requests.get('http://127.0.0.1:8000/topicapirwp_setting/')

#     if response.status_code == 200:
#         print("HELLO",response.json()[-1])
# response = requests.get('http://127.0.0.1:8000/topicapirwp_setting/')
rwp=rwp_setting.objects.last()

dinfo=device_info.objects.filter(componant_name=rwp.componant_name,unit_type=rwp.unit_type,company_name=rwp.company_name)
for x in dinfo:
    print("did id:",x.Device_id)
    did=x.Device_id
    cmpname=x.componant_name
    print("ddddid is",did)

class rwpsettingViewset(viewsets.ModelViewSet):
	# define queryset
    print("hi ok ")
    queryset = rwp_setting.objects.all()
    print("queryset is",queryset)

    data=queryset.last()
    print("OLc",data.olc)
    data = {'olc':data.olc,'drc':data.drc,'spn':data.spn,'units_type':data.unit_type,'company_name':data.company_name,'component_name':data.componant_name}
    print('data is:',data)
    # dosome()
    print("Hi Satish")
    
    
	# specify serializer to be used
    serializer_class = rwpsettingSerializer
    
    def dispatch(self, request, *args, **kwargs):
        
        try:
            data_dict = json.loads(request.body)
            unwanted_keys = ["unit_type", "water_treatment","company_name","componant_name"]  # Example of unwanted keys
            print("dict data is:",data_dict)
            value_list=list(data_dict.values())
            dinfo=device_info.objects.filter(componant_name=value_list[2],unit_type=value_list[1],company_name=value_list[0])
            for x in dinfo:
                print("did id:",x.Device_id)
                did=x.Device_id
                cmpname=x.componant_name
                print("ddddid is",did)
            for key in unwanted_keys:
                if key in data_dict:
                    del data_dict[key]
            mqtt_client.publish(f'wd/{did}/updset/{cmpname}',str(data_dict))

                
            
        except:
            print("Error")
        return super().dispatch(request)
        
    def desptroy(self, request):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
        except Http404:
            pass

class hppstateViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = hpp_state.objects.all()

	# specify serializer to be used
	serializer_class = hppstateSerializer
        
class hppsettingViewset(viewsets.ModelViewSet):
        # define queryset
        queryset = hpp_setting.objects.all()
        # specify serializer to be used
        serializer_class = hppsettingSerializer
        def dispatch(self, request, *args, **kwargs):
        
            try:
                data_dict = json.loads(request.body)
                print("Request",request.body)
                unwanted_keys = ["unit_type","company_name","componant_name"]  # Example of unwanted keys
                print("dict data is:",data_dict)
                value_list=list(data_dict.values())
                comp=value_list[2]
                print("comp is",comp)
                print("value_list isaaaa:",value_list)

                dinfo=device_info.objects.filter(componant_name=value_list[2],unit_type=value_list[1],company_name=value_list[0])
                print(dinfo)
                for x in dinfo:
                    print("did id:",x.Device_id)
                    did=x.Device_id
                    cmpname=x.componant_name
                    print("ddddid is",did)
                for key in unwanted_keys:
                    if key in data_dict:
                        del data_dict[key]
                mqtt_client.publish(f'wd/{did}/updset/{cmpname}',str(data_dict))
                print(did,cmpname,data_dict)
            except:
                print("Error")
            return super().dispatch(request)
            


class cndsettingViewset(viewsets.ModelViewSet):
	# define queryset
        queryset = cnd_setting.objects.all()
        serializer_class = cndsettingSerializer
        def dispatch(self, request, *args, **kwargs):
        
            try:
                data_dict = json.loads(request.body)
                print("Request",request.body)
                unwanted_keys = ["unit_type","company_name","componant_name"]  # Example of unwanted keys
                print("dict data is:",data_dict)
                value_list=list(data_dict.values())
                comp=value_list[2]
                print("comp is",comp)
                print("value_list isaaaa:",value_list)

                dinfo=device_info.objects.filter(componant_name=value_list[2],unit_type=value_list[1],company_name=value_list[0])
                print(dinfo)
                for x in dinfo:
                    print("did id:",x.Device_id)
                    did=x.Device_id
                    cmpname=x.componant_name
                    print("ddddid is",did)
                for key in unwanted_keys:
                    if key in data_dict:
                        del data_dict[key]
                mqtt_client.publish(f'wd/{did}/updset/{cmpname}',str(data_dict))
                print(did,cmpname,data_dict)
            except:
                print("Error")
            return super().dispatch(request)
        
class tdssettingViewset(viewsets.ModelViewSet):
        # define queryset
        queryset = tds_setting.objects.all()

        # specify serializer to be used
        serializer_class = tdssettingSerializer
        
        def dispatch(self, request, *args, **kwargs):
        
            try:
                data_dict = json.loads(request.body)
                print("Request",request.body)
                unwanted_keys = ["unit_type","company_name","componant_name"]  # Example of unwanted keys
                print("dict data is:",data_dict)
                value_list=list(data_dict.values())
                comp=value_list[2]
                print("comp is",comp)
                print("value_list isaaaa:",value_list)

                dinfo=device_info.objects.filter(componant_name=value_list[2],unit_type=value_list[1],company_name=value_list[0])
                print(dinfo)
                for x in dinfo:
                    print("did id:",x.Device_id)
                    did=x.Device_id
                    cmpname=x.componant_name
                    print("ddddid is",did)
                for key in unwanted_keys:
                    if key in data_dict:
                        del data_dict[key]
                mqtt_client.publish(f'wd/{did}/updset/{cmpname}',str(data_dict))
                print(did,cmpname,data_dict)
            except:
                print("Error")
            return super().dispatch(request)
    
class FflowsensettingViewset(viewsets.ModelViewSet):
        # define queryset
        queryset = F_flowsen_setting.objects.all()

        # specify serializer to be used
        serializer_class = FflowsensettingSerializer
        def dispatch(self, request, *args, **kwargs):
        
            try:
                data_dict = json.loads(request.body)
                print("Request",request.body)
                unwanted_keys = ["unit_type","company_name","componant_name"]  # Example of unwanted keys
                print("dict data is:",data_dict)
                value_list=list(data_dict.values())
                comp=value_list[2]
                print("comp is",comp)
                print("value_list isaaaa:",value_list)

                dinfo=device_info.objects.filter(componant_name=value_list[2],unit_type=value_list[1],company_name=value_list[0])
                print(dinfo)
                for x in dinfo:
                    print("did id:",x.Device_id)
                    did=x.Device_id
                    cmpname=x.componant_name
                    print("ddddid is",did)
                for key in unwanted_keys:
                    if key in data_dict:
                        del data_dict[key]
                mqtt_client.publish(f'wd/{did}/updset/{cmpname}',str(data_dict))
                print(did,cmpname,data_dict)
            except:
                print("Error")
            return super().dispatch(request)
        
class PflowsensettingViewset(viewsets.ModelViewSet):
	# define queryset
        queryset = P_flowsen_setting.objects.all()

        # specify serializer to be used
        serializer_class =PflowsensettingSerializer
        def dispatch(self, request, *args, **kwargs):
        
            try:
                data_dict = json.loads(request.body)
                print("Request",request.body)
                unwanted_keys = ["unit_type","company_name","componant_name"]  # Example of unwanted keys
                print("dict data is:",data_dict)
                value_list=list(data_dict.values())
                comp=value_list[2]
                print("comp is",comp)
                print("value_list isaaaa:",value_list)

                dinfo=device_info.objects.filter(componant_name=value_list[2],unit_type=value_list[1],company_name=value_list[0])
                print(dinfo)
                for x in dinfo:
                    print("did id:",x.Device_id)
                    did=x.Device_id
                    cmpname=x.componant_name
                    print("ddddid is",did)
                for key in unwanted_keys:
                    if key in data_dict:
                        del data_dict[key]
                mqtt_client.publish(f'wd/{did}/updset/{cmpname}',str(data_dict))
                print(did,cmpname,data_dict)
            except:
                print("Error")
            return super().dispatch(request)
class panelsettingViewset(viewsets.ModelViewSet):
	# define queryset
        queryset = panel_setting.objects.all()

        # specify serializer to be used
        serializer_class = panelsettingSerializer
        def dispatch(self, request, *args, **kwargs):
        
            try:
                data_dict = json.loads(request.body)
                print("Request",request.body)
                unwanted_keys = ["unit_type","company_name","componant_name"]  # Example of unwanted keys
                print("dict data is:",data_dict)
                value_list=list(data_dict.values())
                comp=value_list[2]
                print("comp is",comp)
                print("value_list isaaaa:",value_list)

                dinfo=device_info.objects.filter(componant_name=value_list[2],unit_type=value_list[1],company_name=value_list[0])
                print(dinfo)
                for x in dinfo:
                    print("did id:",x.Device_id)
                    did=x.Device_id
                    cmpname=x.componant_name
                    print("ddddid is",did)
                for key in unwanted_keys:
                    if key in data_dict:
                        del data_dict[key]
                mqtt_client.publish(f'wd/{did}/updset/{cmpname}',str(data_dict))
                print(did,cmpname,data_dict)
            except:
                print("Error")
            return super().dispatch(request)
class atmsettingViewset(viewsets.ModelViewSet):
	# define queryset
        queryset = atm_setting.objects.all()

        # specify serializer to be used
        serializer_class = atmsettingSerializer
        def dispatch(self, request, *args, **kwargs):
        
            try:
                data_dict = json.loads(request.body)
                print("Request",request.body)
                unwanted_keys = ["unit_type","company_name","componant_name"]  # Example of unwanted keys
                print("dict data is:",data_dict)
                value_list=list(data_dict.values())
                comp=value_list[2]
                print("comp is",comp)
                print("value_list isaaaa:",value_list)

                dinfo=device_info.objects.filter(componant_name=value_list[2],unit_type=value_list[1],company_name=value_list[0])
                print(dinfo)
                for x in dinfo:
                    print("did id:",x.Device_id)
                    did=x.Device_id
                    cmpname=x.componant_name
                    print("ddddid is",did)
                for key in unwanted_keys:
                    if key in data_dict:
                        del data_dict[key]
                mqtt_client.publish(f'wd/{did}/updset/{cmpname}',str(data_dict))
                print(did,cmpname,data_dict)
            except:
                print("Error")
            return super().dispatch(request)
        
# class consensettingViewset(viewsets.ModelViewSet):
# 	# define queryset
# 	queryset = consen_setting.objects.all()

# 	# specify serializer to be used
# 	serializer_class = consensettingSerializer
class ampv1stateViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = ampv1_state.objects.all()

	# specify serializer to be used
	serializer_class = ampv1stateSerializer
class ampv1settingViewset(viewsets.ModelViewSet):
# 	# define queryset
        queryset = ampv1_setting.objects.all()

        # specify serializer to be used
        serializer_class = ampv1settingSerializer
        def dispatch(self, request, *args, **kwargs):
        
            try:
                data_dict = json.loads(request.body)
                print("Request",request.body)
                unwanted_keys = ["unit_type","company_name","componant_name"]  # Example of unwanted keys
                print("dict data is:",data_dict)
                value_list=list(data_dict.values())
                comp=value_list[2]
                print("comp is",comp)
                print("value_list isaaaa:",value_list)

                dinfo=device_info.objects.filter(componant_name=value_list[2],unit_type=value_list[1],company_name=value_list[0])
                print(dinfo)
                for x in dinfo:
                    print("did id:",x.Device_id)
                    did=x.Device_id
                    cmpname=x.componant_name
                    print("ddddid is",did)
                for key in unwanted_keys:
                    if key in data_dict:
                        del data_dict[key]
                mqtt_client.publish(f'wd/{did}/updset/{cmpname}',str(data_dict))
                print(did,cmpname,data_dict)
            except:
                print("Error")
            return super().dispatch(request)
class ampv2stateViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = ampv2_state.objects.all()

	# specify serializer to be used
	serializer_class = ampv2stateSerializer
class ampv2settingViewset(viewsets.ModelViewSet):
	# define queryset
        queryset = ampv2_setting.objects.all()

        # specify serializer to be used
        serializer_class = ampv2settingSerializer
        def dispatch(self, request, *args, **kwargs):
        
            try:
                data_dict = json.loads(request.body)
                print("Request",request.body)
                unwanted_keys = ["unit_type","company_name","componant_name"]  # Example of unwanted keys
                print("dict data is:",data_dict)
                value_list=list(data_dict.values())
                comp=value_list[2]
                print("comp is",comp)
                print("value_list isaaaa:",value_list)

                dinfo=device_info.objects.filter(componant_name=value_list[2],unit_type=value_list[1],company_name=value_list[0])
                print(dinfo)
                for x in dinfo:
                    print("did id:",x.Device_id)
                    did=x.Device_id
                    cmpname=x.componant_name
                    print("ddddid is",did)
                for key in unwanted_keys:
                    if key in data_dict:
                        del data_dict[key]
                mqtt_client.publish(f'wd/{did}/updset/{cmpname}',str(data_dict))
                print(did,cmpname,data_dict)
            except:
                print("Error")
            return super().dispatch(request)

class tap1settingViewset(viewsets.ModelViewSet):
	# define queryset
        queryset = tap1_setting.objects.all()

        # specify serializer to be used
        serializer_class = tap1settingSerializer
        def dispatch(self, request, *args, **kwargs):
        
            try:
                data_dict = json.loads(request.body)
                print("Request",request.body)
                unwanted_keys = ["unit_type","company_name","componant_name"]  # Example of unwanted keys
                print("dict data is:",data_dict)
                value_list=list(data_dict.values())
                comp=value_list[2]
                print("comp is",comp)
                print("value_list isaaaa:",value_list)

                dinfo=device_info.objects.filter(componant_name=value_list[2],unit_type=value_list[1],company_name=value_list[0])
                print(dinfo)
                for x in dinfo:
                    print("did id:",x.Device_id)
                    did=x.Device_id
                    cmpname=x.componant_name
                    print("ddddid is",did)
                for key in unwanted_keys:
                    if key in data_dict:
                        del data_dict[key]
                mqtt_client.publish(f'wd/{did}/updset/{cmpname}',str(data_dict))
                print(did,cmpname,data_dict)
            except:
                print("Error")
            return super().dispatch(request)
class tap2settingViewset(viewsets.ModelViewSet):
	# define queryset
        queryset = tap2_setting.objects.all()

        # specify serializer to be used
        serializer_class = tap2settingSerializer
        def dispatch(self, request, *args, **kwargs):
        
            try:
                data_dict = json.loads(request.body)
                print("Request",request.body)
                unwanted_keys = ["unit_type","company_name","componant_name"]  # Example of unwanted keys
                print("dict data is:",data_dict)
                value_list=list(data_dict.values())
                comp=value_list[2]
                print("comp is",comp)
                print("value_list isaaaa:",value_list)

                dinfo=device_info.objects.filter(componant_name=value_list[2],unit_type=value_list[1],company_name=value_list[0])
                print(dinfo)
                for x in dinfo:
                    print("did id:",x.Device_id)
                    did=x.Device_id
                    cmpname=x.componant_name
                    print("ddddid is",did)
                for key in unwanted_keys:
                    if key in data_dict:
                        del data_dict[key]
                mqtt_client.publish(f'wd/{did}/updset/{cmpname}',str(data_dict))
                print(did,cmpname,data_dict)
            except:
                print("Error")
            return super().dispatch(request)
class tap3settingViewset(viewsets.ModelViewSet):
	# define queryset
        queryset = tap3_setting.objects.all()

        # specify serializer to be used
        serializer_class = tap3settingSerializer
        def dispatch(self, request, *args, **kwargs):
        
            try:
                data_dict = json.loads(request.body)
                print("Request",request.body)
                unwanted_keys = ["unit_type","company_name","componant_name"]  # Example of unwanted keys
                print("dict data is:",data_dict)
                value_list=list(data_dict.values())
                comp=value_list[2]
                print("comp is",comp)
                print("value_list isaaaa:",value_list)

                dinfo=device_info.objects.filter(componant_name=value_list[2],unit_type=value_list[1],company_name=value_list[0])
                print(dinfo)
                for x in dinfo:
                    print("did id:",x.Device_id)
                    did=x.Device_id
                    cmpname=x.componant_name
                    print("ddddid is",did)
                for key in unwanted_keys:
                    if key in data_dict:
                        del data_dict[key]
                mqtt_client.publish(f'wd/{did}/updset/{cmpname}',str(data_dict))
                print(did,cmpname,data_dict)
            except:
                print("Error")
            return super().dispatch(request)
class tap4settingViewset(viewsets.ModelViewSet):
	# define queryset
        queryset = tap4_setting.objects.all()

        # specify serializer to be used
        serializer_class = tap4settingSerializer
        def dispatch(self, request, *args, **kwargs):
        
            try:
                data_dict = json.loads(request.body)
                print("Request",request.body)
                unwanted_keys = ["unit_type","company_name","componant_name"]  # Example of unwanted keys
                print("dict data is:",data_dict)
                value_list=list(data_dict.values())
                comp=value_list[2]
                print("comp is",comp)
                print("value_list isaaaa:",value_list)

                dinfo=device_info.objects.filter(componant_name=value_list[2],unit_type=value_list[1],company_name=value_list[0])
                print(dinfo)
                for x in dinfo:
                    print("did id:",x.Device_id)
                    did=x.Device_id
                    cmpname=x.componant_name
                    print("ddddid is",did)
                for key in unwanted_keys:
                    if key in data_dict:
                        del data_dict[key]
                mqtt_client.publish(f'wd/{did}/updset/{cmpname}',str(data_dict))
                print(did,cmpname,data_dict)
            except:
                print("Error")
            return super().dispatch(request)
        
        
class HourlyViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = repo_hourly.objects.all()

# 	# specify serializer to be used
# 	serializer_class = All_componentSerializer      
# class HourlyViewset(viewsets.ModelViewSet):
# 	# define queryset
# 	queryset = cnd_tds_repo_hourly.objects.all()

# 	# specify serializer to be used
# 	serializer_class = HourlySerializer
        
# class MonthlyViewset(viewsets.ModelViewSet):
# 	# define queryset
# 	queryset = cnd_tds_repo_monthly.objects.all()

# 	# specify serializer to be used
# 	serializer_class = MonthlySerializer
        
# class DailyViewset(viewsets.ModelViewSet):
# 	# define queryset
# 	queryset = cnd_tds_repo_daily.objects.all()

# 	# specify serializer to be used
# 	serializer_class = DailySerializer
        
class GraphViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = graph_info.objects.all()

	# specify serializer to be used
	serializer_class = GraphSerializer
class TopicViewSet(viewsets.ModelViewSet):
	# define queryset
	queryset = topics.objects.all()

	# specify serializer to be used
	serializer_class = TopicSerializer
# class YearlyViewset(viewsets.ModelViewSet):
# 	# define queryset
# 	queryset = repo_yearly.objects.all()

# 	# specify serializer to be used
# 	serializer_class = YearlySerializer

class DeviceViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = device_info.objects.all()

	# specify serializer to be used
	serializer_class = DeviceSerializer
        
class keyViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = key_info.objects.all()

	# specify serializer to be used
	serializer_class = KeySerializer
        
class RwpstateViewset(viewsets.ModelViewSet):
        # define queryset
        queryset = Rwp_state.objects.all()

        # specify serializer to be used
        serializer_class = RwpstateSerializer
        def dispatch(self, request, *args, **kwargs):
        
            try:
                data_dict = json.loads(request.body)
                unwanted_keys = ["unit_type", "water_treatment","company_name","componant_name"]  # Example of unwanted keys
                print("dict data is:",data_dict)
                value_list=list(data_dict.values())
                print("value_list:",value_list)
                dinfo=device_info.objects.filter(componant_name=value_list[2],unit_type=value_list[1],company_name=value_list[0])
                for x in dinfo:
                    print("did id:",x.Device_id)
                    did=x.Device_id
                    cmpname=x.componant_name
                    print("ddddid is",did)
                for key in unwanted_keys:
                    if key in data_dict:
                        del data_dict[key]
                mqtt_client.publish(f'wc/{did}/updset/{cmpname}',str(data_dict))
                print("data send to hivemq")

            except Exception as e:
                print("Error",e)
            return super().dispatch(request)    
        def perform_create(self, serializer):
            try:
                data_dict = serializer.validated_data
                # Get the device information based on the provided values
                dinfo = device_info.objects.filter(componant_name=data_dict['componant_name'],
                                                unit_type=data_dict['unit_type'],
                                                company_name=data_dict['company_name']).last()
                if dinfo:
                    did = dinfo.Device_id
                    cmpname = dinfo.componant_name
                    data_dict['device_id'] = did
                serializer.save()  # Save the data to the database
                
            except Exception as e:
                print("Error:", e)
        def desptroy(self, request):
            try:
                instance = self.get_object()
                self.perform_destroy(instance)
            except Http404:
                pass
# rwp=rwp_setting.objects.last()

# dinfo=device_info.objects.filter(componant_name=rwp.componant_name,unit_type=rwp.unit_type,company_name=rwp.company_name)
# for x in dinfo:
#     print("did id:",x.Device_id)
#     did=x.Device_id
#     cmpname=x.componant_name
#     print("ddddid is",did)

class rwpsettingViewset(viewsets.ModelViewSet):
	# define queryset
    print("hi ok ")
    # queryset = rwp_setting.objects.all()
    queryset = rwp_setting.objects.all()
    print("queryset is",queryset)    
	# specify serializer to be used
    serializer_class = rwpsettingSerializer
    def dispatch(self, request, *args, **kwargs):
        try:
            data_dict = json.loads(request.body)
            unwanted_keys = ["unit_type", "water_treatment","company_name","componant_name"]  # Example of unwanted keys
            print("dict data is:",data_dict)
            value_list=list(data_dict.values())
            print("value_list:",value_list)
            dinfo=device_info.objects.filter(componant_name=value_list[2],unit_type=value_list[1],company_name=value_list[0])
            for x in dinfo:
                print("did id:",x.Device_id)
                did=x.Device_id
                cmpname=x.componant_name
                print("ddddid is",did)
            for key in unwanted_keys:
                if key in data_dict:
                    del data_dict[key]
            mqtt_client.publish(f'wc/{did}/chgset/{cmpname}',str(data_dict))
            print("data send to hivemq")
        except Exception as e:
            print("Error",e)
        return super().dispatch(request)    
    def perform_create(self, serializer):
        try:
            data_dict = serializer.validated_data
            dinfo = device_info.objects.filter(componant_name=data_dict['componant_name'],
                                               unit_type=data_dict['unit_type'],
                                               company_name=data_dict['company_name']).last()
            if dinfo:
                did = dinfo.Device_id
                cmpname = dinfo.componant_name
                data_dict['device_id'] = did
            serializer.save()  # Save the data to the database
            
        except Exception as e:
            print("Error:", e)
    def desptroy(self, request):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
        except Http404:
            pass
class hppstateViewset(viewsets.ModelViewSet):
	# define queryset
        queryset = hpp_state.objects.all()

        # specify serializer to be used
        serializer_class = hppstateSerializer
        def dispatch(self, request, *args, **kwargs):
        
            try:
                data_dict = json.loads(request.body)
                unwanted_keys = ["unit_type", "water_treatment","company_name","componant_name"]  # Example of unwanted keys
                print("dict data is:",data_dict)
                value_list=list(data_dict.values())
                print("value_list:",value_list)
                dinfo=device_info.objects.filter(componant_name=value_list[2],unit_type=value_list[1],company_name=value_list[0])
                for x in dinfo:
                    print("did id:",x.Device_id)
                    did=x.Device_id
                    cmpname=x.componant_name
                    print("ddddid is",did)
                for key in unwanted_keys:
                    if key in data_dict:
                        del data_dict[key]
                mqtt_client.publish(f'wc/{did}/updset/{cmpname}',str(data_dict))
                print("data send to hivemq")

            except Exception as e:
                print("Error",e)
            return super().dispatch(request)    
        def perform_create(self, serializer):
            try:
                data_dict = serializer.validated_data
                # Get the device information based on the provided values
                dinfo = device_info.objects.filter(componant_name=data_dict['componant_name'],
                                                unit_type=data_dict['unit_type'],
                                                company_name=data_dict['company_name']).last()
                if dinfo:
                    did = dinfo.Device_id
                    cmpname = dinfo.componant_name
                    data_dict['device_id'] = did
                serializer.save()  # Save the data to the database
                
            except Exception as e:
                print("Error:", e)
        def desptroy(self, request):
            try:
                instance = self.get_object()
                self.perform_destroy(instance)
            except Http404:
                pass   
class hppsettingViewset(viewsets.ModelViewSet):
        # define queryset
        queryset = hpp_setting.objects.all()
        # specify serializer to be used
        serializer_class = hppsettingSerializer
        def dispatch(self, request, *args, **kwargs):
        
            try:
                data_dict = json.loads(request.body)
                unwanted_keys = ["unit_type", "water_treatment","company_name","componant_name"]  # Example of unwanted keys
                print("dict data is:",data_dict)
                value_list=list(data_dict.values())
                print("value_list:",value_list)
                dinfo=device_info.objects.filter(componant_name=value_list[2],unit_type=value_list[1],company_name=value_list[0])
                for x in dinfo:
                    print("did id:",x.Device_id)
                    did=x.Device_id
                    cmpname=x.componant_name
                    print("ddddid is",did)
                for key in unwanted_keys:
                    if key in data_dict:
                        del data_dict[key]
                mqtt_client.publish(f'wc/{did}/updset/{cmpname}',str(data_dict))
                print("data send to hivemq")

            except Exception as e:
                print("Error",e)
            return super().dispatch(request)    
        def perform_create(self, serializer):
            try:
                data_dict = serializer.validated_data
                # Get the device information based on the provided values
                dinfo = device_info.objects.filter(componant_name=data_dict['componant_name'],
                                                unit_type=data_dict['unit_type'],
                                                company_name=data_dict['company_name']).last()
                if dinfo:
                    did = dinfo.Device_id
                    cmpname = dinfo.componant_name
                    data_dict['device_id'] = did
                serializer.save()  # Save the data to the database
                
            except Exception as e:
                print("Error:", e)
        def desptroy(self, request):
            try:
                instance = self.get_object()
                self.perform_destroy(instance)
            except Http404:
                pass
                
class cndsettingViewset(viewsets.ModelViewSet):
	# define queryset
        queryset = cnd_setting.objects.all()
        serializer_class = cndsettingSerializer
        def dispatch(self, request, *args, **kwargs):
        
            try:
                data_dict = json.loads(request.body)
                unwanted_keys = ["unit_type", "water_treatment","company_name","componant_name"]  # Example of unwanted keys
                print("dict data is:",data_dict)
                value_list=list(data_dict.values())
                print("value_list:",value_list)
                dinfo=device_info.objects.filter(componant_name=value_list[2],unit_type=value_list[1],company_name=value_list[0])
                for x in dinfo:
                    print("did id:",x.Device_id)
                    did=x.Device_id
                    cmpname=x.componant_name
                    print("ddddid is",did)
                for key in unwanted_keys:
                    if key in data_dict:
                        del data_dict[key]
                mqtt_client.publish(f'wc/{did}/updset/{cmpname}',str(data_dict))
                print("data send to hivemq")

            except Exception as e:
                print("Error",e)
            return super().dispatch(request)    
        def perform_create(self, serializer):
            try:
                data_dict = serializer.validated_data
                # Get the device information based on the provided values
                dinfo = device_info.objects.filter(componant_name=data_dict['componant_name'],
                                                unit_type=data_dict['unit_type'],
                                                company_name=data_dict['company_name']).last()
                if dinfo:
                    did = dinfo.Device_id
                    cmpname = dinfo.componant_name
                    data_dict['device_id'] = did
                serializer.save()  # Save the data to the database
                
            except Exception as e:
                print("Error:", e)
        def desptroy(self, request):
            try:
                instance = self.get_object()
                self.perform_destroy(instance)
            except Http404:
                pass
        
class tdssettingViewset(viewsets.ModelViewSet):
        # define queryset
        queryset = tds_setting.objects.all()

        # specify serializer to be used
        serializer_class = tdssettingSerializer
        
        def dispatch(self, request, *args, **kwargs):
        
            try:
                data_dict = json.loads(request.body)
                unwanted_keys = ["unit_type", "water_treatment","company_name","componant_name"]  # Example of unwanted keys
                print("dict data is:",data_dict)
                value_list=list(data_dict.values())
                print("value_list:",value_list)
                dinfo=device_info.objects.filter(componant_name=value_list[2],unit_type=value_list[1],company_name=value_list[0])
                for x in dinfo:
                    print("did id:",x.Device_id)
                    did=x.Device_id
                    cmpname=x.componant_name
                    print("ddddid is",did)
                for key in unwanted_keys:
                    if key in data_dict:
                        del data_dict[key]
                mqtt_client.publish(f'wc/{did}/updset/{cmpname}',str(data_dict))
                print("data send to hivemq")

            except Exception as e:
                print("Error",e)
            return super().dispatch(request)    
        def perform_create(self, serializer):
            try:
                data_dict = serializer.validated_data
                # Get the device information based on the provided values
                dinfo = device_info.objects.filter(componant_name=data_dict['componant_name'],
                                                unit_type=data_dict['unit_type'],
                                                company_name=data_dict['company_name']).last()
                if dinfo:
                    did = dinfo.Device_id
                    cmpname = dinfo.componant_name
                    data_dict['device_id'] = did
                serializer.save()  # Save the data to the database
                
            except Exception as e:
                print("Error:", e)
        def desptroy(self, request):
            try:
                instance = self.get_object()
                self.perform_destroy(instance)
            except Http404:
                pass
    
class FflowsensettingViewset(viewsets.ModelViewSet):
        # define queryset
        queryset = F_flowsen_setting.objects.all()

        # specify serializer to be used
        serializer_class = FflowsensettingSerializer
        def dispatch(self, request, *args, **kwargs):
        
            try:
                data_dict = json.loads(request.body)
                unwanted_keys = ["unit_type", "water_treatment","company_name","componant_name"]  # Example of unwanted keys
                print("dict data is:",data_dict)
                value_list=list(data_dict.values())
                print("value_list:",value_list)
                dinfo=device_info.objects.filter(componant_name=value_list[2],unit_type=value_list[1],company_name=value_list[0])
                for x in dinfo:
                    print("did id:",x.Device_id)
                    did=x.Device_id
                    cmpname=x.componant_name
                    print("ddddid is",did)
                for key in unwanted_keys:
                    if key in data_dict:
                        del data_dict[key]
                mqtt_client.publish(f'wc/{did}/updset/{cmpname}',str(data_dict))
                print("data send to hivemq")

            except Exception as e:
                print("Error",e)
            return super().dispatch(request)    
        def perform_create(self, serializer):
            try:
                data_dict = serializer.validated_data
                # Get the device information based on the provided values
                dinfo = device_info.objects.filter(componant_name=data_dict['componant_name'],
                                                unit_type=data_dict['unit_type'],
                                                company_name=data_dict['company_name']).last()
                if dinfo:
                    did = dinfo.Device_id
                    cmpname = dinfo.componant_name
                    data_dict['device_id'] = did
                serializer.save()  # Save the data to the database
                
            except Exception as e:
                print("Error:", e)
        def desptroy(self, request):
            try:
                instance = self.get_object()
                self.perform_destroy(instance)
            except Http404:
                pass
        
class PflowsensettingViewset(viewsets.ModelViewSet):
	# define queryset
        queryset = P_flowsen_setting.objects.all()

        # specify serializer to be used
        serializer_class =PflowsensettingSerializer
        def dispatch(self, request, *args, **kwargs):
        
            try:
                data_dict = json.loads(request.body)
                unwanted_keys = ["unit_type", "water_treatment","company_name","componant_name"]  # Example of unwanted keys
                print("dict data is:",data_dict)
                value_list=list(data_dict.values())
                print("value_list:",value_list)
                dinfo=device_info.objects.filter(componant_name=value_list[2],unit_type=value_list[1],company_name=value_list[0])
                for x in dinfo:
                    print("did id:",x.Device_id)
                    did=x.Device_id
                    cmpname=x.componant_name
                    print("ddddid is",did)
                for key in unwanted_keys:
                    if key in data_dict:
                        del data_dict[key]
                mqtt_client.publish(f'wc/{did}/updset/{cmpname}',str(data_dict))
                print("data send to hivemq")

            except Exception as e:
                print("Error",e)
            return super().dispatch(request)    
        def perform_create(self, serializer):
            try:
                data_dict = serializer.validated_data
                # Get the device information based on the provided values
                dinfo = device_info.objects.filter(componant_name=data_dict['componant_name'],
                                                unit_type=data_dict['unit_type'],
                                                company_name=data_dict['company_name']).last()
                if dinfo:
                    did = dinfo.Device_id
                    cmpname = dinfo.componant_name
                    data_dict['device_id'] = did
                serializer.save()  # Save the data to the database
                
            except Exception as e:
                print("Error:", e)
        def desptroy(self, request):
            try:
                instance = self.get_object()
                self.perform_destroy(instance)
            except Http404:
                pass
class panelsettingViewset(viewsets.ModelViewSet):
	# define queryset
        queryset = panel_setting.objects.all()

        # specify serializer to be used
        serializer_class = panelsettingSerializer
        def dispatch(self, request, *args, **kwargs):
        
            try:
                data_dict = json.loads(request.body)
                unwanted_keys = ["unit_type", "water_treatment","company_name","componant_name"]  # Example of unwanted keys
                print("dict data is:",data_dict)
                value_list=list(data_dict.values())
                print("value_list:",value_list)
                dinfo=device_info.objects.filter(componant_name=value_list[2],unit_type=value_list[1],company_name=value_list[0])
                for x in dinfo:
                    print("did id:",x.Device_id)
                    did=x.Device_id
                    cmpname=x.componant_name
                    print("ddddid is",did)
                for key in unwanted_keys:
                    if key in data_dict:
                        del data_dict[key]
                mqtt_client.publish(f'wc/{did}/updset/{cmpname}',str(data_dict))
                print("data send to hivemq")

            except Exception as e:
                print("Error",e)
            return super().dispatch(request)    
        def perform_create(self, serializer):
            try:
                data_dict = serializer.validated_data
                # Get the device information based on the provided values
                dinfo = device_info.objects.filter(componant_name=data_dict['componant_name'],
                                                unit_type=data_dict['unit_type'],
                                                company_name=data_dict['company_name']).last()
                if dinfo:
                    did = dinfo.Device_id
                    cmpname = dinfo.componant_name
                    data_dict['device_id'] = did
                serializer.save()  # Save the data to the database
                
            except Exception as e:
                print("Error:", e)
        def desptroy(self, request):
            try:
                instance = self.get_object()
                self.perform_destroy(instance)
            except Http404:
                pass
class atmsettingViewset(viewsets.ModelViewSet):
	# define queryset
        queryset = atm_setting.objects.all()

        # specify serializer to be used
        serializer_class = atmsettingSerializer
        def dispatch(self, request, *args, **kwargs):
        
            try:
                data_dict = json.loads(request.body)
                unwanted_keys = ["unit_type", "water_treatment","company_name","componant_name"]  # Example of unwanted keys
                print("dict data is:",data_dict)
                value_list=list(data_dict.values())
                print("value_list:",value_list)
                dinfo=device_info.objects.filter(componant_name=value_list[2],unit_type=value_list[1],company_name=value_list[0])
                for x in dinfo:
                    print("did id:",x.Device_id)
                    did=x.Device_id
                    cmpname=x.componant_name
                    print("ddddid is",did)
                for key in unwanted_keys:
                    if key in data_dict:
                        del data_dict[key]
                mqtt_client.publish(f'wc/{did}/updset/{cmpname}',str(data_dict))
                print("data send to hivemq")

            except Exception as e:
                print("Error",e)
            return super().dispatch(request)    
        def perform_create(self, serializer):
            try:
                data_dict = serializer.validated_data
                # Get the device information based on the provided values
                dinfo = device_info.objects.filter(componant_name=data_dict['componant_name'],
                                                unit_type=data_dict['unit_type'],
                                                company_name=data_dict['company_name']).last()
                if dinfo:
                    did = dinfo.Device_id
                    cmpname = dinfo.componant_name
                    data_dict['device_id'] = did
                serializer.save()  # Save the data to the database
                
            except Exception as e:
                print("Error:", e)
        def desptroy(self, request):
            try:
                instance = self.get_object()
                self.perform_destroy(instance)
            except Http404:
                pass
        
class consensettingViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = consen_setting.objects.all()

	# specify serializer to be used
	serializer_class = consensettingSerializer
class ampv1stateViewset(viewsets.ModelViewSet):
        # define queryset
        queryset = ampv1_state.objects.all()

        # specify serializer to be used
        serializer_class = ampv1stateSerializer
        def dispatch(self, request, *args, **kwargs):
        
            try:
                data_dict = json.loads(request.body)
                unwanted_keys = ["unit_type", "water_treatment","company_name","componant_name"]  # Example of unwanted keys
                print("dict data is:",data_dict)
                value_list=list(data_dict.values())
                print("value_list:",value_list)
                dinfo=device_info.objects.filter(componant_name=value_list[2],unit_type=value_list[1],company_name=value_list[0])
                for x in dinfo:
                    print("did id:",x.Device_id)
                    did=x.Device_id
                    cmpname=x.componant_name
                    print("ddddid is",did)
                for key in unwanted_keys:
                    if key in data_dict:
                        del data_dict[key]
                mqtt_client.publish(f'wc/{did}/updset/{cmpname}',str(data_dict))
                print("data send to hivemq")

            except Exception as e:
                print("Error",e)
            return super().dispatch(request)    
        def perform_create(self, serializer):
            try:
                data_dict = serializer.validated_data
                # Get the device information based on the provided values
                dinfo = device_info.objects.filter(componant_name=data_dict['componant_name'],
                                                unit_type=data_dict['unit_type'],
                                                company_name=data_dict['company_name']).last()
                if dinfo:
                    did = dinfo.Device_id
                    cmpname = dinfo.componant_name
                    data_dict['device_id'] = did
                serializer.save()  # Save the data to the database
                
            except Exception as e:
                print("Error:", e)
        def desptroy(self, request):
            try:
                instance = self.get_object()
                self.perform_destroy(instance)
            except Http404:
                pass
        
class ampv1settingViewset(viewsets.ModelViewSet):
# 	# define queryset
        queryset = ampv1_setting.objects.all()

        # specify serializer to be used
        serializer_class = ampv1settingSerializer
        def dispatch(self, request, *args, **kwargs):
        
            try:
                data_dict = json.loads(request.body)
                unwanted_keys = ["unit_type", "water_treatment","company_name","componant_name"]  # Example of unwanted keys
                print("dict data is:",data_dict)
                value_list=list(data_dict.values())
                print("value_list:",value_list)
                dinfo=device_info.objects.filter(componant_name=value_list[2],unit_type=value_list[1],company_name=value_list[0])
                for x in dinfo:
                    print("did id:",x.Device_id)
                    did=x.Device_id
                    cmpname=x.componant_name
                    print("ddddid is",did)
                for key in unwanted_keys:
                    if key in data_dict:
                        del data_dict[key]
                mqtt_client.publish(f'wc/{did}/updset/{cmpname}',str(data_dict))
                print("data send to hivemq")

            except Exception as e:
                print("Error",e)
            return super().dispatch(request)    
        def perform_create(self, serializer):
            try:
                data_dict = serializer.validated_data
                # Get the device information based on the provided values
                dinfo = device_info.objects.filter(componant_name=data_dict['componant_name'],
                                                unit_type=data_dict['unit_type'],
                                                company_name=data_dict['company_name']).last()
                if dinfo:
                    did = dinfo.Device_id
                    cmpname = dinfo.componant_name
                    data_dict['device_id'] = did
                serializer.save()  # Save the data to the database
                
            except Exception as e:
                print("Error:", e)
        def desptroy(self, request):
            try:
                instance = self.get_object()
                self.perform_destroy(instance)
            except Http404:
                pass
class ampv2stateViewset(viewsets.ModelViewSet):
        # define queryset
        queryset = ampv2_state.objects.all()

        # specify serializer to be used
        serializer_class = ampv2stateSerializer
        def dispatch(self, request, *args, **kwargs):
        
            try:
                data_dict = json.loads(request.body)
                unwanted_keys = ["unit_type", "water_treatment","company_name","componant_name"]  # Example of unwanted keys
                print("dict data is:",data_dict)
                value_list=list(data_dict.values())
                print("value_list:",value_list)
                dinfo=device_info.objects.filter(componant_name=value_list[2],unit_type=value_list[1],company_name=value_list[0])
                for x in dinfo:
                    print("did id:",x.Device_id)
                    did=x.Device_id
                    cmpname=x.componant_name
                    print("ddddid is",did)
                for key in unwanted_keys:
                    if key in data_dict:
                        del data_dict[key]
                mqtt_client.publish(f'wc/{did}/updset/{cmpname}',str(data_dict))
                print("data send to hivemq")

            except Exception as e:
                print("Error",e)
            return super().dispatch(request)    
        def perform_create(self, serializer):
            try:
                data_dict = serializer.validated_data
                # Get the device information based on the provided values
                dinfo = device_info.objects.filter(componant_name=data_dict['componant_name'],
                                                unit_type=data_dict['unit_type'],
                                                company_name=data_dict['company_name']).last()
                if dinfo:
                    did = dinfo.Device_id
                    cmpname = dinfo.componant_name
                    data_dict['device_id'] = did
                serializer.save()  # Save the data to the database
                
            except Exception as e:
                print("Error:", e)
        def desptroy(self, request):
            try:
                instance = self.get_object()
                self.perform_destroy(instance)
            except Http404:
                pass
class ampv2settingViewset(viewsets.ModelViewSet):
	# define queryset
        queryset = ampv2_setting.objects.all()

        # specify serializer to be used
        serializer_class = ampv2settingSerializer
        def dispatch(self, request, *args, **kwargs):
        
            try:
                data_dict = json.loads(request.body)
                unwanted_keys = ["unit_type", "water_treatment","company_name","componant_name"]  # Example of unwanted keys
                print("dict data is:",data_dict)
                value_list=list(data_dict.values())
                print("value_list:",value_list)
                dinfo=device_info.objects.filter(componant_name=value_list[2],unit_type=value_list[1],company_name=value_list[0])
                for x in dinfo:
                    print("did id:",x.Device_id)
                    did=x.Device_id
                    cmpname=x.componant_name
                    print("ddddid is",did)
                for key in unwanted_keys:
                    if key in data_dict:
                        del data_dict[key]
                mqtt_client.publish(f'wc/{did}/updset/{cmpname}',str(data_dict))
                print("data send to hivemq")

            except Exception as e:
                print("Error",e)
            return super().dispatch(request)    
        def perform_create(self, serializer):
            try:
                data_dict = serializer.validated_data
                # Get the device information based on the provided values
                dinfo = device_info.objects.filter(componant_name=data_dict['componant_name'],
                                                unit_type=data_dict['unit_type'],
                                                company_name=data_dict['company_name']).last()
                if dinfo:
                    did = dinfo.Device_id
                    cmpname = dinfo.componant_name
                    data_dict['device_id'] = did
                serializer.save()  # Save the data to the database
                
            except Exception as e:
                print("Error:", e)
        def desptroy(self, request):
            try:
                instance = self.get_object()
                self.perform_destroy(instance)
            except Http404:
                pass

class tap1settingViewset(viewsets.ModelViewSet):
	# define queryset
        queryset = tap1_setting.objects.all()

        # specify serializer to be used
        serializer_class = tap1settingSerializer
        def dispatch(self, request, *args, **kwargs):
        
            try:
                data_dict = json.loads(request.body)
                unwanted_keys = ["unit_type", "water_treatment","company_name","componant_name"]  # Example of unwanted keys
                print("dict data is:",data_dict)
                value_list=list(data_dict.values())
                print("value_list:",value_list)
                dinfo=device_info.objects.filter(componant_name=value_list[2],unit_type=value_list[1],company_name=value_list[0])
                for x in dinfo:
                    print("did id:",x.Device_id)
                    did=x.Device_id
                    cmpname=x.componant_name
                    print("ddddid is",did)
                for key in unwanted_keys:
                    if key in data_dict:
                        del data_dict[key]
                mqtt_client.publish(f'wc/{did}/updset/{cmpname}',str(data_dict))
                print("data send to hivemq")

            except Exception as e:
                print("Error",e)
            return super().dispatch(request)    
        def perform_create(self, serializer):
            try:
                data_dict = serializer.validated_data
                # Get the device information based on the provided values
                dinfo = device_info.objects.filter(componant_name=data_dict['componant_name'],
                                                unit_type=data_dict['unit_type'],
                                                company_name=data_dict['company_name']).last()
                if dinfo:
                    did = dinfo.Device_id
                    cmpname = dinfo.componant_name
                    data_dict['device_id'] = did
                serializer.save()  # Save the data to the database
                
            except Exception as e:
                print("Error:", e)
        def desptroy(self, request):
            try:
                instance = self.get_object()
                self.perform_destroy(instance)
            except Http404:
                pass
class tap2settingViewset(viewsets.ModelViewSet):
	# define queryset
        queryset = tap2_setting.objects.all()

        # specify serializer to be used
        serializer_class = tap2settingSerializer
        def dispatch(self, request, *args, **kwargs):
        
            try:
                data_dict = json.loads(request.body)
                unwanted_keys = ["unit_type", "water_treatment","company_name","componant_name"]  # Example of unwanted keys
                print("dict data is:",data_dict)
                value_list=list(data_dict.values())
                print("value_list:",value_list)
                dinfo=device_info.objects.filter(componant_name=value_list[2],unit_type=value_list[1],company_name=value_list[0])
                for x in dinfo:
                    print("did id:",x.Device_id)
                    did=x.Device_id
                    cmpname=x.componant_name
                    print("ddddid is",did)
                for key in unwanted_keys:
                    if key in data_dict:
                        del data_dict[key]
                mqtt_client.publish(f'wc/{did}/updset/{cmpname}',str(data_dict))
                print("data send to hivemq")

            except Exception as e:
                print("Error",e)
            return super().dispatch(request)    
        def perform_create(self, serializer):
            try:
                data_dict = serializer.validated_data
                # Get the device information based on the provided values
                dinfo = device_info.objects.filter(componant_name=data_dict['componant_name'],
                                                unit_type=data_dict['unit_type'],
                                                company_name=data_dict['company_name']).last()
                if dinfo:
                    did = dinfo.Device_id
                    cmpname = dinfo.componant_name
                    data_dict['device_id'] = did
                serializer.save()  # Save the data to the database
                
            except Exception as e:
                print("Error:", e)
        def desptroy(self, request):
            try:
                instance = self.get_object()
                self.perform_destroy(instance)
            except Http404:
                pass
class tap3settingViewset(viewsets.ModelViewSet):
	# define queryset
        queryset = tap3_setting.objects.all()

        # specify serializer to be used
        serializer_class = tap3settingSerializer
        def dispatch(self, request, *args, **kwargs):
        
            try:
                data_dict = json.loads(request.body)
                unwanted_keys = ["unit_type", "water_treatment","company_name","componant_name"]  # Example of unwanted keys
                print("dict data is:",data_dict)
                value_list=list(data_dict.values())
                print("value_list:",value_list)
                dinfo=device_info.objects.filter(componant_name=value_list[2],unit_type=value_list[1],company_name=value_list[0])
                for x in dinfo:
                    print("did id:",x.Device_id)
                    did=x.Device_id
                    cmpname=x.componant_name
                    print("ddddid is",did)
                for key in unwanted_keys:
                    if key in data_dict:
                        del data_dict[key]
                mqtt_client.publish(f'wc/{did}/updset/{cmpname}',str(data_dict))
                print("data send to hivemq")

            except Exception as e:
                print("Error",e)
            return super().dispatch(request)    
        def perform_create(self, serializer):
            try:
                data_dict = serializer.validated_data
                # Get the device information based on the provided values
                dinfo = device_info.objects.filter(componant_name=data_dict['componant_name'],
                                                unit_type=data_dict['unit_type'],
                                                company_name=data_dict['company_name']).last()
                if dinfo:
                    did = dinfo.Device_id
                    cmpname = dinfo.componant_name
                    data_dict['device_id'] = did
                serializer.save()  # Save the data to the database
                
            except Exception as e:
                print("Error:", e)
        def desptroy(self, request):
            try:
                instance = self.get_object()
                self.perform_destroy(instance)
            except Http404:
                pass
class tap4settingViewset(viewsets.ModelViewSet):
	# define queryset
        queryset = tap4_setting.objects.all()

        # specify serializer to be used
        serializer_class = tap4settingSerializer
        def dispatch(self, request, *args, **kwargs):
        
            try:
                data_dict = json.loads(request.body)
                unwanted_keys = ["unit_type", "water_treatment","company_name","componant_name"]  # Example of unwanted keys
                print("dict data is:",data_dict)
                value_list=list(data_dict.values())
                print("value_list:",value_list)
                dinfo=device_info.objects.filter(componant_name=value_list[2],unit_type=value_list[1],company_name=value_list[0])
                for x in dinfo:
                    print("did id:",x.Device_id)
                    did=x.Device_id
                    cmpname=x.componant_name
                    print("ddddid is",did)
                for key in unwanted_keys:
                    if key in data_dict:
                        del data_dict[key]
                mqtt_client.publish(f'wc/{did}/updset/{cmpname}',str(data_dict))
                print("data send to hivemq")

            except Exception as e:
                print("Error",e)
            return super().dispatch(request)    
        def perform_create(self, serializer):
            try:
                data_dict = serializer.validated_data
                # Get the device information based on the provided values
                dinfo = device_info.objects.filter(componant_name=data_dict['componant_name'],
                                                unit_type=data_dict['unit_type'],
                                                company_name=data_dict['company_name']).last()
                if dinfo:
                    did = dinfo.Device_id
                    cmpname = dinfo.componant_name
                    data_dict['device_id'] = did
                serializer.save()  # Save the data to the database
                
            except Exception as e:
                print("Error:", e)
        def desptroy(self, request):
            try:
                instance = self.get_object()
                self.perform_destroy(instance)
            except Http404:
                pass
        

def Treat_cnd(request):
    print("hello")
    return render(request,'test.html')


# def publish_message(request):
# def publish_message():
    # request_data = json.loads(request.body)
    # testlist=['test/topic/1','test/topic/2']
    # msg=input("Enter message:")
    # testlist={'test/topic/1':input("Enter message:"),'test/topic/2':input("Enter message:")}

    # for k,v in testlist.items():
    #     rc, mid = mqtt_client.publish(k,v)
    #     # data=subscribers.objects.create(Topic=k,msg=v)
    #     # data.save()
    # return JsonResponse({'code': rc})

# cnd=0
# spn=0
# tsp=0
# asp=0
# sts=''
# crt=0
# olc=0
# drc=0
# rtl=''
# ttl=''
# lps=''
# hps=''
# dgp=''
# mod=''
# ipv=0
# unv=0
# ovv=0
# nmv=0
# stp=0
# srt=0
# bkt=0
# rst=0
# err=''
# fr1=0
# fr2=0
# ff1=0
# ff2=0
# pos=''
# rmt=0
# cct=0
# srt=0
# bkt=0
# mot=0
# stp=''
# op1=''
# op2=''
# op3=''
# ip1=''
# ip2=''
# ip3=''
# psi=''
# ndv=0
# ntt=''
# nta=0
# tmp=0
# ntp=0
# nov=0
# vl1=0
# vl2=0
# vl3=0
# vl4=0
# re1=0
# re2=0
# re3=0
# re4=0
# p1=0
# p2=0
# p3=0
# p4=0
# cnd=0
# spn=0
# asp=0

def testo(request):
    print("btesto")
    def on_connect(mqtt_client, userdata, flags, rc):
        # global rc
        if rc == 0:
            print('Connected successfully')

            
            mqtt_client.subscribe('wc/#')
            
        # response = requests.get('http://127.0.0.1:8000/topicapirwp_setting/')

        # if response.status_code == 200:
        #     print("HELLO",response.json()[-1])

            # print(response.J``)
            
            
            # topicdata=topics.objects.all()
            # for top in topicdata:
            #     print("topic is:",top)
            # print("Topic data is:",topicdata)
            # topicdata=dict(topicdata)
            # for k, v in topicdata.items():
            #     if k=='Topic_name':
            # mqtt_client.subscribe('django/mqtt')
        
        else:
            print('Bad connection. Code:', rc)

    
    def on_message(mqtt_client, userdata, msg):
        # global cnd,spn,tsp,asp,sts,crt,olc,drc,rtl,ttl,lps,hps,dgp,mod,ipv,unv,ovv,nmv,stp,srt,bkt,rst,err,fr1,fr2,ff1,ff2,pos,rmt,cct,srt,bkt,mot,stp,op1,op2,op3,ip1,ip2,ip3,psi,ndv,ntt,nta,tmp,ntp,nov,vl1,vl2,vl3,vl4,re1,re2,re3,re4,p1,p2,p3,p4,cnd,spn,asp
        global msgo
        print(f'Received message on topic: {msg.topic} with payload: {msg.payload}')
        jstring=msg.payload
        print("vikaso:",jstring)
        # mydata1=0
        dict_str = jstring.decode("UTF-8")
        print("decoded:",dict_str,type(dict_str))
        rep1=dict_str.replace("}",'')
        rep2=rep1.replace("{",'')
        print('********************************rep1',rep2)
        array_dat = rep2.split(',')
        mydata ={}

        cnd=0
        spn=0
        tsp=0
        asp=0
        sts=''
        crt=0
        olc=0
        drc=0
        rtl=''
        ttl=''
        lps=''
        hps=''
        dgp=''
        mod=''
        ipv=0
        unv=0
        ovv=0
        nmv=0
        stp=0
        srt=0
        bkt=0
        rst=0
        err=''
        fr1=0
        fr2=0
        ff1=0
        ff2=0
        pos=''
        rmt=0
        cct=0
        srt=0
        bkt=0
        mot=0
        stp=''
        op1=''
        op2=''
        op3=''
        ip1=''
        ip2=''
        ip3=''
        psi=''
        ndv=0
        ntt=''
        nta=0
        tmp=0
        ntp=0
        nov=0
        vl1=0
        vl2=0
        vl3=0
        vl4=0
        re1=0
        re2=0
        re3=0
        re4=0
        p1=0
        p2=0
        p3=0
        p4=0

        for loop_data in array_dat:
            print("array_dat",loop_data)
            removed_col = loop_data.split(':')
            print("removed_col",removed_col)
            mydata[removed_col[0]] =removed_col[1]

            
            if removed_col[0]=='cnd':
                cnd=removed_col[1]
            elif removed_col[0]=='spn':
                spn=removed_col[1]
            elif removed_col[0]=='tsp':
                tsp=removed_col[1]
            elif removed_col[0]=='asp':
                asp=removed_col[1]
            elif removed_col[0]=='sts':
                sts=removed_col[1]
            elif removed_col[0]=='crt':
                crt=removed_col[1]
            elif removed_col[0]=='olc':
                olc=removed_col[1]
            elif removed_col[0]=='drc':
                drc=removed_col[1]
            elif removed_col[0]=='rtl':
                rtl=removed_col[1]
            elif removed_col[0]=='ttl':
                ttl=removed_col[1]
            elif removed_col[0]=='lps':
                lps=removed_col[1]
            elif removed_col[0]=='hps':
                hps=removed_col[1]
            elif removed_col[0]=='dgp':
                dgp=removed_col[1]
            elif removed_col[0]=='mod':
                mod=removed_col[1]
            elif removed_col[0]=='ipv':
                ipv=removed_col[1]
            elif removed_col[0]=='unv':
                unv=removed_col[1]
            elif removed_col[0]=='ovv':
                ovv=removed_col[1]
            elif removed_col[0]=='nmv':
                nmv=removed_col[1]
            elif removed_col[0]=='stp':
                stp=removed_col[1]
            elif removed_col[0]=='srt':
                srt=removed_col[1]
            elif removed_col[0]=='bkt':
                bkt=removed_col[1]
            elif removed_col[0]=='rst':
                rst=removed_col[1]
            elif removed_col[0]=='err':
                err=removed_col[1]
            elif removed_col[0]=='fr1':
                fr1=removed_col[1]
            elif removed_col[0]=='fr2':
                fr2=removed_col[1]
            elif removed_col[0]=='ff1':
                ff1=removed_col[1]
            elif removed_col[0]=='ff2':
                ff2=removed_col[1]
            elif removed_col[0]=='pos':
                pos=removed_col[1]
            elif removed_col[0]=='rmt':
                rmt=removed_col[1]
            elif removed_col[0]=='cct':
                cct=removed_col[1]
            elif removed_col[0]=='srt':
                srt=removed_col[1]
            elif removed_col[0]=='bkt':
                bkt=removed_col[1]
            elif removed_col[0]=='mot':
                mot=removed_col[1]
            elif removed_col[0]=='stp':
                stp=removed_col[1]
            elif removed_col[0]=='op1':
                op1=removed_col[1]
            elif removed_col[0]=='op2':
                op2=removed_col[1]
            elif removed_col[0]=='op3':
                op3=removed_col[1]
            elif removed_col[0]=='ip1':
                ip1=removed_col[1]
            elif removed_col[0]=='ip2':
                ip2=removed_col[1]
            elif removed_col[0]=='ip3':
                ip3=removed_col[1]
            elif removed_col[0]=='psi':
                psi=removed_col[1]
            elif removed_col[0]=='ndv':
                ndv=removed_col[1]
            elif removed_col[0]=='ntt':
                ntt=removed_col[1]
            elif removed_col[0]=='nta':
                nta=removed_col[1]
            elif removed_col[0]=='tmp':
                tmp=removed_col[1]
            elif removed_col[0]=='ntp':
                ntp=removed_col[1]
            elif removed_col[0]=='nov':
                nov=removed_col[1]
            elif removed_col[0]=='vl1':
                vl1=removed_col[1]
            elif removed_col[0]=='vl2':
                vl2=removed_col[1]
            elif removed_col[0]=='vl3':
                vl3=removed_col[1]
            elif removed_col[0]=='vl4':
                vl4=removed_col[1]
            elif removed_col[0]=='re1':
                re1=removed_col[1]
            elif removed_col[0]=='re2':
                re2=removed_col[1]
            elif removed_col[0]=='re3':
                re3=removed_col[1]
            elif removed_col[0]=='re4':
                re4=removed_col[1]
            elif removed_col[0]=='p1':
                p1=removed_col[1]
            elif removed_col[0]=='p2':
                p2=removed_col[1]
            elif removed_col[0]=='p3':
                p3=removed_col[1]
            elif removed_col[0]=='p4':
                p4=removed_col[1]
          
           
           
           
        print("sts", sts)

        print("mydata before dump:",mydata,type(mydata))  
        mydata1=mydata      
        mydata = json.dumps(mydata, indent = 4) 
        # mydata = ast.literal_eval(mydata)
        # mydata = ast.literal_eval(dict_str)
        print("final data:",mydata,type(mydata))
        mydatadict=json.loads(mydata)
        print(mydatadict,type(mydatadict))
        hmq=msg.topic
        hmqm_split=hmq.split('/')
        print(hmqm_split)
        device_id=hmqm_split[1]
        msg_type=hmqm_split[2]
        components=hmqm_split[3]
        print("*"*10,mydata)
        od=mydata.strip()
        print("#"*10,od)
        repo_histobj=repo_history.objects.create(device_id=device_id,message_type=msg_type,component_name=components,msg_json=mydata1)
        repo_histobj.save()
        get_device_id=repo_latestdata.objects.all()
        # print(get_device_id.)
        device_idlist=[]
        tds1={}
        rwp={}
        hpp={}
        panel={}
        flowsen={}
        ampv1={}
        ampv2={}
        ampv3={}
        ampv4={}
        ampv5={}
        atm={}
        tap1={}
        tap2={}
        tap3={}
        tap4={}
        consen={}

        monthset=set()
        print("device id is:",device_id,type(device_id))
        for did in get_device_id:
             s=str(did.device_id)
             if device_id == s:
                print("latest data is:",did.device_id)
                print("latest data is:",did.message_type)
                tds=did.cnd_tds
                tds1=tds
                # tdsstr=(str(tds))
                print("tdso data is:",tds,type(tds))
                print("latest data is:",did.cnd_tds,type(did.cnd_tds))
                rwp=did.rwp
                print("latest data is:",did.rwp)
                hpp=did.hpp
                print("latest data is:",did.hpp)
                panel=did.panel
                print("latest data is:",did.panel)
                flowsen=did.flowsen
                print("latest data is:",did.flowsen)
                ampv1=did.ampv1
                print("latest data is:",did.ampv1)
                ampv2=did.ampv2
                print("latest data is:",did.ampv2)
                ampv3=did.ampv3
                print("latest data is:",did.ampv3)
                ampv4=did.ampv4
                print("latest data is:",did.ampv4)
                ampv5=did.ampv5
                print("latest data is:",did.ampv5)
                atm=did.atm
                print("latest data is:",did.atm)
                tap1=did.tap1
                print("latest data is:",did.tap1)
                tap2=did.tap2
                print("latest data is:",did.tap2)
                tap3=did.tap3
                print("latest data is:",did.tap3)
                tap4=did.tap4
                print("latest data is:",did.tap4)
                consen=did.consen
                print("latest data is:",did.consen)
             device_idlist.append(s)
             print(device_idlist)
        print("component is:",components)
        service_list=[]
        repoyearly=cnd_tds_repo_yearly.objects.all()
        for ry in repoyearly:
                ser=ry.service
                service_list.append(ser)
                print("service is:",ser)
        print("out of for loop")
        olddata={}
        hourset=set()
        dd=dateandtime() 
        print("$$$$$$$ddn is:",dd,type(dd)) 
        print(dd[0])
        response = requests.get('http://127.0.0.1:8000/topicapirwp_setting/')

        try:
            if response.status_code == 200:
                print("HELLO in if:",response.json()[-1])
                datas=response.json()[-1]

                rwp=rwp_setting.objects.last()
                print("RWP",rwp)
                comd.update({'olc':rwp.olc,'drc':rwp.drc,'spn':rwp.spn})
                print("comd",comd)
                print("rwp is:",rwp)
                print("olc is:",rwp.olc)
                print("drc is:",rwp.drc)
                print("spn is:",rwp.spn)
                print("unit_type is:",rwp.unit_type)
                print("company_name is:",rwp.company_name)
                print("componant_name:",rwp.componant_name)
                print("-x-"*25)
                dinfo=devices_info.objects.filter(componant_name=rwp.componant_name,unit_type=rwp.unit_type,company_name=rwp.company_name)
                # print("dinfo is:",dinfo.componant_name)
                cmpname=str()
                did=0
                for x in dinfo:
                    print("did id:",x.Device_id)
                    did=x.Device_id
                    cmpname=x.componant_name

                    urlo=f"wd/{did}/updset/{cmpname}"
                    print("url is ",urlo)
                    testlist={f'wd/{did}/updset/{cmpname}':str(datas)}#,'test/topic/2':comd
                    print("****",testlist)
                    for k,v in testlist.items():
                        rc, mid = mqtt_client.publish(k,v)
        except:
            pass 
        try:
            if 'cnd_tds'== components:
                # com=cl
                print("in cndtds")
                if device_id not in device_idlist:
                     repo_latestdata.objects.create(device_id=device_id,message_type=msg_type,cnd_tds=mydata1)
                else:
                    repo_latestobj = repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id, message_type=msg_type, cnd_tds=mydata1)

                    get_device_id=repo_latestdata.objects.all()
                    for did in get_device_id:
                        s=str(did.device_id)
                        if device_id == s:
                            print("latest data is:",did.device_id)
                            print("latest data is:",did.message_type)
                            tds=did.cnd_tds
                            tds1=tds
                            # tdsstr=(str(tds))
                            print("tdso data is:",tds,type(tds))
                            print("latest data is:",did.cnd_tds,type(did.cnd_tds))

                    klist = list(tds1.keys())
                    print("klist is:",klist)
                    mydatakey = list(mydata1.keys())
                    print("mydatakey:",mydatakey)
                    for k,v in tds1.items():
                         if k not in mydatakey:
                              olddata.update({k:v})
                              
                    mydata5=olddata.update(mydata1)    
                    print("old data is:",olddata) # add/update keys in mydata1 to olddata
                    repo_latestobj = repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id, message_type=msg_type, cnd_tds=olddata)
                
                dd=dateandtime()  
                print("$$$$$$$dd is:",dd,type(dd)) 
                print(dd[0])
                ds=treat_cnd_tds_sen.objects.create(device_id=device_id,message_type=msg_type,cnd=cnd,spn=spn,tsp=tsp,asp=asp,year=dd[0],month=dd[1],day=dd[2],hour=dd[3],minit=dd[4],second=dd[5])
                ds.save()
                # Hour
                yrdata=treat_cnd_tds_sen.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id)
                count=0
                zerocount=-1
                sumd={}
                sums_cnd=0
                sums_spn=0
                sums_tsp=0
                sums_asp=0
                avgs_cnd = 0
                avgs_spn = 0
                avgs_tsp = 0
                avgs_asp = 0
                if yrdata:
                    for yr in yrdata:
                        yr_d_id=yr.device_id
                        if yr_d_id == device_id:
                            cnds=yr.cnd
                            spns=yr.spn
                            tsps=yr.tsp
                            asps=yr.asp
                            print("cnds is:",cnds)
                            sums_cnd=sums_cnd+cnds
                            sums_spn=sums_spn+spns
                            sums_tsp=sums_tsp+tsps
                            sums_asp=sums_asp+asps
                            count=count+1
                            print("sums is:",sums_cnd)
                            print("count is:",count)
                            if cnds or spns or tsp or asp == 0:
                                zerocount=zerocount+1
                                print("countzone is:",zerocount)
                    count1=count-zerocount
                    avgs_cnd=sums_cnd/count
                    avgs_spn=sums_spn/count
                    avgs_tsp=sums_tsp/count
                    avgs_asp=sums_asp/count
                hr=cnd_tds_repo_hourly.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id)
                if hr:
                    yr_data=cnd_tds_repo_hourly.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id).update(device_id=device_id,service='cnd_tds',cnd={'sum':sums_cnd,'avg':avgs_cnd,'count':count},spn={'sum':sums_spn,'avg':avgs_spn,'count':count},tsp={'sum':sums_tsp,'avg':avgs_tsp,'count':count},asp={'sum':sums_asp,'avg':avgs_asp,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                else:
                    yr_data=cnd_tds_repo_hourly.objects.create(device_id=device_id,service='cnd_tds',cnd={'sum':sums_cnd,'avg':avgs_cnd,'count':count},spn={'sum':sums_spn,'avg':avgs_spn,'count':count},tsp={'sum':sums_tsp,'avg':avgs_tsp,'count':count},asp={'sum':sums_asp,'avg':avgs_asp,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                    yr_data.save()
                    # if cnds != 0:
                    #     yr_data=cnd_tds_repo_hourly.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id).update(device_id=device_id,service='cnd_tds',cnd={'sum':sums_cnd,'avg':avgs_cnd,'count':count},spn={'sum':sums_spn,'avg':avgs_spn,'count':count},tsp={'sum':sums_tsp,'avg':avgs_tsp,'count':count},asp={'sum':sums_asp,'avg':avgs_asp,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                    # else:
                    #     yr_data=cnd_tds_repo_hourly.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id).update(device_id=device_id,service='cnd_tds',cnd={'sum':sums_cnd,'avg':avgs_cnd,'count':count1},spn={'sum':sums_spn,'avg':avgs_spn,'count':count},tsp={'sum':sums_tsp,'avg':avgs_tsp,'count':count},asp={'sum':sums_asp,'avg':avgs_asp,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                    # if spns != 0:
                    #     yr_data=cnd_tds_repo_hourly.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id).update(device_id=device_id,service='cnd_tds',cnd={'sum':sums_cnd,'avg':avgs_cnd,'count':count},spn={'sum':sums_spn,'avg':avgs_spn,'count':count},tsp={'sum':sums_tsp,'avg':avgs_tsp,'count':count},asp={'sum':sums_asp,'avg':avgs_asp,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                    # else:
                    #     yr_data=cnd_tds_repo_hourly.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id).update(device_id=device_id,service='cnd_tds',cnd={'sum':sums_cnd,'avg':avgs_cnd,'count':count},spn={'sum':sums_spn,'avg':avgs_spn,'count':count1},tsp={'sum':sums_tsp,'avg':avgs_tsp,'count':count},asp={'sum':sums_asp,'avg':avgs_asp,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                #day   
                yrdata=treat_cnd_tds_sen.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id)
                count=0
                count_sum=0
                count_cnd=0
                count_spn=0
                count_tsp=0
                count_asp=0
                sums_cnd=0
                sums_spn=0
                sums_tsp=0
                sums_asp=0
                avgs_cnd = 0
                avgs_spn = 0
                avgs_tsp = 0
                avgs_asp = 0
                if yrdata:
                    for yr in yrdata:
                        print("day for loop")
                        yr_d_id=yr.device_id
                        if yr_d_id == device_id:
                            print("in if")
                            cnds_d=yr.cnd
                            spns_d=yr.spn
                            tsps_d=yr.tsp
                            asps_d=yr.asp
                            # sums_d=list(cnds_d.values())[0]
                            # sums_s=list(spns_d.values())[0]
                            # sums_t=list(tsps_d.values())[0]
                            # sums_a=list(asps_d.values())[0]
                            # # avgs_cnd=list(cnds.values())[1]
                            # count_cnd=list(cnds_d.values())[2]
                            # for k,v in cnds.items():
                            sums_cnd=sums_cnd+cnds_d
                            sums_spn=sums_spn+spns_d
                            sums_tsp=sums_tsp+tsps_d
                            sums_asp=sums_asp+asps_d
                            count_sum=count_sum+count_cnd


                            print("sum from dict:",sums_cnd,type(sums_cnd))
                            # spns=yr.spn[1]
                            # tsps=yr.tsp[2]
                            # asps=yr.asp[3]
                            print("cnds is:",cnds)
                            # sums_cnd=sums_cnd+cnds
                            # sums_spn=sums_spn+spns
                            # sums_tsp=sums_tsp+tsps
                            # sums_asp=sums_asp+asps
                            count=count+1
                            print("count is:",count)
                    print("sums is:",sums_cnd)
                    print("countsum is:",count_sum)
                    avgs_cnd=sums_cnd/count
                    print("average cnd is:",avgs_cnd)

                    avgs_spn=sums_spn/count
                    print("avg of spn:",avgs_spn)
                    avgs_tsp=sums_tsp/count
                    avgs_asp=sums_asp/count
                hr=cnd_tds_repo_daily.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id)
                if hr:
                    print("in if hr")
                    yr_data=cnd_tds_repo_daily.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id).update(device_id=device_id,service='cnd_tds',cnd={'sum':sums_cnd,'avg':avgs_cnd,'count':count},spn={'sum':sums_spn,'avg':avgs_spn,'count':count},tsp={'sum':sums_tsp,'avg':avgs_tsp,'count':count},asp={'sum':sums_asp,'avg':avgs_asp,'count':count},month=dd[1],year=dd[0],day=dd[2],hour=dd[3])
                    print("data insertedd")
                else:
                    yr_data=cnd_tds_repo_daily.objects.create(device_id=device_id,service='cnd_tds',cnd={'sum':sums_cnd,'avg':avgs_cnd,'count':count},spn={'sum':sums_spn,'avg':avgs_spn,'count':count},tsp={'sum':sums_tsp,'avg':avgs_tsp,'count':count},asp={'sum':sums_asp,'avg':avgs_asp,'count':count},month=dd[1],year=dd[0],day=dd[2],hour=dd[3])
                    yr_data.save()
                    print("success")
                 #month
                print("in month")
                yrdata=treat_cnd_tds_sen.objects.filter(year=dd[0],month=dd[1],device_id=device_id)
                count=0
                sums_cnd=0
                sums_spn=0
                sums_tsp=0
                sums_asp=0
                avgs_cnd = 0
                avgs_spn = 0
                avgs_tsp = 0
                avgs_asp = 0
                if yrdata:
                    for yr in yrdata:
                        yr_d_id=yr.device_id
                        if yr_d_id == device_id:
                            cnds=yr.cnd
                            spns=yr.spn
                            tsps=yr.tsp
                            asps=yr.asp
                            print("cnds is:",cnds)
                            sums_cnd=sums_cnd+cnds
                            sums_spn=sums_spn+spns
                            sums_tsp=sums_tsp+tsps
                            sums_asp=sums_asp+asps
                            count=count+1
                            print("sums is:",sums_cnd)
                            print("count is:",count)                            
                            if cnds or spns or tsp or asp == 0:
                                zerocount=zerocount+1
                    # count1=count-zerocount
                    # if cnds != 0:
                    #     avgs_cnd=sums_cnd/count
                    # else:
                    #     avgs_cnd=sums_cnd/count1
                    # if spns != 0:
                    #     avgs_spn=sums_spn/count
                    # else:
                    #     avgs_spn=sums_spn/count1
                    # if tsps !=0:
                    #     avgs_tsp=sums_tsp/count
                    # else:    
                    #     avgs_tsp=sums_tsp/count1
                    # if asp !=0:
                    #     avgs_asp=sums_asp/count
                    # else:
                    #     avgs_asp=sums_asp/count1
                    avgs_cnd=sums_cnd/count
                    avgs_spn=sums_spn/count
                    avgs_tsp=sums_tsp/count
                    avgs_asp=sums_asp/count
                hr=cnd_tds_repo_monthly.objects.filter(year=dd[0],month=dd[1],device_id=device_id)
                if hr:
                    yr_data=cnd_tds_repo_monthly.objects.filter(year=dd[0],month=dd[1],device_id=device_id).update(device_id=device_id,service='cnd_tds',cnd={'sum':sums_cnd,'avg':avgs_cnd,'count':count},spn={'sum':sums_spn,'avg':avgs_spn,'count':count},tsp={'sum':sums_tsp,'avg':avgs_tsp,'count':count},asp={'sum':sums_asp,'avg':avgs_asp,'count':count},month=dd[1],year=dd[0],day=dd[2],hour=dd[3])
                else:
                    yr_data=cnd_tds_repo_monthly.objects.create(device_id=device_id,service='cnd_tds',cnd={'sum':sums_cnd,'avg':avgs_cnd,'count':count},spn={'sum':sums_spn,'avg':avgs_spn,'count':count},tsp={'sum':sums_tsp,'avg':avgs_tsp,'count':count},asp={'sum':sums_asp,'avg':avgs_asp,'count':count},month=dd[1],year=dd[0],day=dd[2],hour=dd[3])
                    yr_data.save()
               
                # year
                yrdata=treat_cnd_tds_sen.objects.filter(year=dd[0],device_id=device_id)
                count=0
                sums_cnd=0
                sums_spn=0
                sums_tsp=0
                sums_asp=0
                avgs_cnd = 0
                avgs_spn = 0
                avgs_tsp = 0
                avgs_asp = 0
                if yrdata:
                    for yr in yrdata:
                        yr_d_id=yr.device_id
                        if yr_d_id == device_id:
                            cnds=yr.cnd
                            spns=yr.spn
                            tsps=yr.tsp
                            asps=yr.asp
                            print("cnds is:",cnds)
                            sums_cnd=sums_cnd+cnds
                            sums_spn=sums_spn+spns
                            sums_tsp=sums_tsp+tsps
                            sums_asp=sums_asp+asps
                            count=count+1
                            print("sums is:",sums_cnd)
                            print("count is:",count)
                            if cnds or spns or tsp or asp == 0:
                                zerocount=zerocount+1
                    # count1=count-zerocount
                    # if cnds != 0:
                    #     avgs_cnd=sums_cnd/count
                    # else:
                    #     avgs_cnd=sums_cnd/count1
                    # if spns != 0:
                    #     avgs_spn=sums_spn/count
                    # else:
                    #     avgs_spn=sums_spn/count1
                    # if tsps !=0:
                    #     avgs_tsp=sums_tsp/count
                    # else:    
                    #     avgs_tsp=sums_tsp/count1
                    # if asp !=0:
                    #     avgs_asp=sums_asp/count
                    # else:
                    #     avgs_asp=sums_asp/count1
                    avgs_cnd=sums_cnd/count
                    avgs_spn=sums_spn/count
                    avgs_tsp=sums_tsp/count
                    avgs_asp=sums_asp/count
                hr=cnd_tds_repo_yearly.objects.filter(year=dd[0],device_id=device_id)
                if hr:
                    yr_data=cnd_tds_repo_yearly.objects.filter(device_id=device_id).update(device_id=device_id,service='cnd_tds',cnd={'sum':sums_cnd,'avg':avgs_cnd,'count':count},spn={'sum':sums_spn,'avg':avgs_spn,'count':count},tsp={'sum':sums_tsp,'avg':avgs_tsp,'count':count},asp={'sum':sums_asp,'avg':avgs_asp,'count':count},month=dd[1],year=dd[0],day=dd[2],hour=dd[3])
                else:
                    yr_data=cnd_tds_repo_yearly.objects.create(device_id=device_id,service='cnd_tds',cnd={'sum':sums_cnd,'avg':avgs_cnd,'count':count},spn={'sum':sums_spn,'avg':avgs_spn,'count':count},tsp={'sum':sums_tsp,'avg':avgs_tsp,'count':count},asp={'sum':sums_asp,'avg':avgs_asp,'count':count},month=dd[1],year=dd[0],day=dd[2],hour=dd[3])
                    yr_data.save()
                               
                # #month
                # yrdata=treat_cnd_tds_sen.objects.filter(year=dd[0],month=dd[1],device_id=device_id)
                # count=0
                # sums=0
                # avgs = 0
                # if yrdata:
                #     for yr in yrdata:
                #         yr_d_id=yr.device_id
                #         if yr_d_id == device_id:
                #             cnds=yr.cnd
                #             print("cnds is:",cnds)
                #             sums=sums+cnds
                #             count=count+1
                #             print("sums is:",sums)
                #             print("count is:",count)
                #     avgs=sums/count
                # hr=repo_monthly.objects.filter(year=dd[0],month=dd[1],device_id=device_id)
                # if hr:
                #     yr_data=repo_monthly.objects.filter(year=dd[0],month=dd[1],device_id=device_id).update(device_id=device_id,service='cnd_tds_cnd',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
                # else:
                #     yr_data=repo_monthly.objects.create(device_id=device_id,service='cnd_tds_cnd',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
                #     yr_data.save()
                
                
                # day
                # yrdata=treat_cnd_tds_sen.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id)
                # count=0
                # sums=0
                # avgs = 0
                # if yrdata:
                #     for yr in yrdata:
                #         yr_d_id=yr.device_id
                #         if yr_d_id == device_id:
                #             cnds=yr.cnd
                #             print("cnds is:",cnds)
                #             sums=sums+cnds
                #             count=count+1
                #             print("sums is:",sums)
                #             print("count is:",count)
                #     avgs=sums/count
                # hr=repo_daily.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id)
                # if hr:
                #     yr_data=repo_daily.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id).update(device_id=device_id,service='cnd_tds_cnd',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0],day=dd[2])
                # else:
                #     yr_data=repo_daily.objects.create(device_id=device_id,service='cnd_tds_cnd',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0],day=dd[2])
                #     yr_data.save()
                
                # return result
                
        except Exception as e:
            print("error ==>", e)
            error_message = traceback.format_exc()
        
        # Send the error message to the WebSocket client
            send_error_message_to_websocket(error_message)
            error_message = e
            global eg
            eg = e
            # print("eg is:",eg)
            # print("Error massage:",e)
            # EchoConsumer.websocket_receive('event','event')
            
            # raise e
            # send_exception_message(error_message)
            # EchoCo.send({
            #         'type': 'websocket.send',
            #          # 'text': event.get('text')
            #         'text': str(e),
                    
            #     })
            # msgo=e
            # return e                 
        try:
            if 'rwp'==components:
                
                
                if device_id not in device_idlist:
                    repo_latestdata.objects.create(device_id=device_id,message_type=msg_type,rwp=mydata1)
                else:
                    repo_latestobj = repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id, message_type=msg_type, rwp=mydata1)

                    get_device_id=repo_latestdata.objects.all()
                    for did in get_device_id:
                        s=str(did.device_id)
                        if device_id == s:
                            rwp=did.rwp
                            # rwp=rwp
                    klist = list(rwp.keys())
                    print("klist is:",klist)
                    mydatakey = list(mydata1.keys())
                    print("mydatakey:",mydatakey)
                    for k,v in rwp.items():
                        if k not in mydatakey:
                            olddata.update({k:v})
                            
                    mydata5=olddata.update(mydata1)    
                    print("old data is:",olddata) # add/update keys in mydata1 to olddata
                    repo_latestobj = repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id, message_type=msg_type, rwp=olddata)
                dd=dateandtime()  
                print("$$$$$$$dd is:",dd,type(dd)) 
                print(dd[0])
                # repo_latestobj=repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id,message_type=msg_type,rwp=mydata1)
                ds=treat_rwp.objects.create(device_id=device_id,message_type=msg_type,sts=sts,crt=crt,olc=olc,drc=drc,spn=spn,year=dd[0],month=dd[1],day=dd[2],hour=dd[3],minit=dd[4],second=dd[5])
                ds.save()

                 # hour
                yrdata=treat_rwp.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id)
                count=0
                sumd={}
                sums_cnd=0
                sums_spn=0
                sums_tsp=0
                sums_asp=0
                avgs_cnd = 0
                avgs_spn = 0
                avgs_tsp = 0
                avgs_asp = 0
                if yrdata:
                    for yr in yrdata:
                        yr_d_id=yr.device_id
                        if yr_d_id == device_id:
                            cnds=yr.crt
                            spns=yr.olc
                            tsps=yr.drc
                            asps=yr.spn
                            print("cnds is:",cnds)
                            sums_cnd=sums_cnd+cnds
                            sums_spn=sums_spn+spns
                            sums_tsp=sums_tsp+tsps
                            sums_asp=sums_asp+asps
                            count=count+1
                            print("sums is:",sums_cnd)
                            print("count is:",count)
                    avgs_cnd=sums_cnd/count
                    avgs_spn=sums_spn/count
                    avgs_tsp=sums_tsp/count
                    avgs_asp=sums_asp/count
                    print("@@@")
               
                hr=rwp_repo_hourly.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id)
                if hr:
                    yr_data=rwp_repo_hourly.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id).update(device_id=device_id,service='rwp',crt={'sum':sums_cnd,'avg':avgs_cnd,'count':count},olc={'sum':sums_spn,'avg':avgs_spn,'count':count},drc={'sum':sums_tsp,'avg':avgs_tsp,'count':count},spn={'sum':sums_asp,'avg':avgs_asp,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                else:
                    yr_data=rwp_repo_hourly.objects.create(device_id=device_id,service='rwp',crt={'sum':sums_cnd,'avg':avgs_cnd,'count':count},olc={'sum':sums_spn,'avg':avgs_spn,'count':count},drc={'sum':sums_tsp,'avg':avgs_tsp,'count':count},spn={'sum':sums_asp,'avg':avgs_asp,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                    yr_data.save()
               
                 # day
                yrdata=treat_rwp.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id)
                count=0
                count_sum=0
                count_cnd=0
                count_spn=0
                count_tsp=0
                count_asp=0
                sums_cnd=0
                sums_spn=0
                sums_tsp=0
                sums_asp=0
                avgs_cnd = 0
                avgs_spn = 0
                avgs_tsp = 0
                avgs_asp = 0
                if yrdata:
                    for yr in yrdata:
                        print("day for loop")
                        yr_d_id=yr.device_id
                        if yr_d_id == device_id:
                            # print("in if")
                            # cnds_d=yr.crt
                            # spns_d=yr.olc
                            # tsps_d=yr.drc
                            # asps_d=yr.spn
                            # sums_d=list(cnds_d.values())[0]
                            # sums_s=list(spns_d.values())[0]
                            # sums_t=list(tsps_d.values())[0]
                            # sums_a=list(asps_d.values())[0]
                            # # avgs_cnd=list(cnds.values())[1]
                            # count_cnd=list(cnds_d.values())[2]
                            # # for k,v in cnds.items():
                            # sums_cnd=sums_cnd+sums_d
                            # sums_spn=sums_spn+sums_s
                            # sums_tsp=sums_tsp+sums_t
                            # sums_asp=sums_asp+sums_a
                            # sums_cnd=sums_cnd+cnds
                            # sums_spn=sums_spn+spns
                            # sums_tsp=sums_tsp+tsps
                            # sums_asp=sums_asp+asps
                            # count=count+1
                            # count_sum=count_sum+count_cnd
                            cnds=yr.crt
                            spns=yr.olc
                            tsps=yr.drc
                            asps=yr.spn
                            print("cnds is:",cnds)
                            sums_cnd=sums_cnd+cnds
                            sums_spn=sums_spn+spns
                            sums_tsp=sums_tsp+tsps
                            sums_asp=sums_asp+asps
                            count=count+1

                            print("sum from dict:",sums_cnd,type(sums_cnd))
                            # spns=yr.spn[1]
                            # tsps=yr.tsp[2]
                            # asps=yr.asp[3]
                            print("cnds is:",cnds)
                            # sums_cnd=sums_cnd+cnds
                            # sums_spn=sums_spn+spns
                            # sums_tsp=sums_tsp+tsps
                            # sums_asp=sums_asp+asps
                            # count=count+1
                            print("count is:",count)
                    print("sums is:",sums_cnd)
                    print("countsum is:",count_sum)
                    avgs_cnd=sums_cnd/count
                    print("average cnd is:",avgs_cnd)

                    avgs_spn=sums_spn/count
                    print("avg of spn00:",avgs_spn)
                    avgs_tsp=sums_tsp/count
                    avgs_asp=sums_asp/count
                hr=rwp_repo_daily.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id)
                if hr:
                    print("in if hr")
                    yr_data=rwp_repo_daily.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id).update(device_id=device_id,service='rwp',crt={'sum':sums_cnd,'avg':avgs_cnd,'count':count},olc={'sum':sums_spn,'avg':avgs_spn,'count':count},drc={'sum':sums_tsp,'avg':avgs_tsp,'count':count},spn={'sum':sums_asp,'avg':avgs_asp,'count':count},month=dd[1],year=dd[0],day=dd[2],hour=dd[3])
                    print("data insertedd")
                else:
                    yr_data=rwp_repo_daily.objects.create(device_id=device_id,service='rwp',crt={'sum':sums_cnd,'avg':avgs_cnd,'count':count},olc={'sum':sums_spn,'avg':avgs_spn,'count':count},drc={'sum':sums_tsp,'avg':avgs_tsp,'count':count},spn={'sum':sums_asp,'avg':avgs_asp,'count':count},month=dd[1],year=dd[0],day=dd[2],hour=dd[3])
                    yr_data.save()
                #monthly
                yrdata=treat_rwp.objects.filter(year=dd[0],month=dd[1],device_id=device_id)
                count=0
                sums_cnd=0
                sums_spn=0
                sums_tsp=0
                sums_asp=0
                avgs_cnd = 0
                avgs_spn = 0
                avgs_tsp = 0
                avgs_asp = 0
                if yrdata:
                    for yr in yrdata:
                        yr_d_id=yr.device_id
                        if yr_d_id == device_id:
                            # cnds_m=yr.crt
                            # spns_m=yr.olc
                            # tsps_m=yr.drc
                            # asps_m=yr.spn
                            # sums_d=list(cnds_m.values())[0]
                            # sums_s=list(spns_m.values())[0]
                            # sums_t=list(tsps_m.values())[0]
                            # sums_a=list(asps_m.values())[0]
                            # # avgs_cnd=list(cnds.values())[1]
                            # count_cnd=list(cnds_d.values())[2]
                            # # for k,v in cnds.items():
                            # sums_cnd=sums_cnd+sums_d
                            # sums_spn=sums_spn+sums_s
                            # sums_tsp=sums_tsp+sums_t
                            # sums_asp=sums_asp+sums_a
                            # sums_cnd=sums_cnd+cnds
                            # sums_spn=sums_spn+spns
                            # sums_tsp=sums_tsp+tsps
                            # sums_asp=sums_asp+asps
                            # count=count+1
                            cnds=yr.crt
                            spns=yr.olc
                            tsps=yr.drc
                            asps=yr.spn
                            print("cnds is:",cnds)
                            sums_cnd=sums_cnd+cnds
                            sums_spn=sums_spn+spns
                            sums_tsp=sums_tsp+tsps
                            sums_asp=sums_asp+asps
                            count=count+1
                            count_sum=count_sum+count_cnd


                            print("sum from dict:",sums_cnd,type(sums_cnd))
                            # spns=yr.spn[1]
                            # tsps=yr.tsp[2]
                            # asps=yr.asp[3]
                            print("cnds is:",cnds)
                            # sums_cnd=sums_cnd+cnds
                            # sums_spn=sums_spn+spns
                            # sums_tsp=sums_tsp+tsps
                            # sums_asp=sums_asp+asps
                            # count=count+1
                            print("count is:",count)
                    print("sums is:",sums_cnd)
                    print("countsum is:",count_sum)
                    avgs_cnd=sums_cnd/count
                    print("average cnd is:",avgs_cnd)

                    avgs_spn=sums_spn/count
                    print("avg of spn:",avgs_spn)
                    avgs_tsp=sums_tsp/count
                    avgs_asp=sums_asp/count
                hr=rwp_repo_monthly.objects.filter(year=dd[0],month=dd[1],device_id=device_id)
                if hr:
                    yr_data=rwp_repo_monthly.objects.filter(year=dd[0],month=dd[1],device_id=device_id).update(device_id=device_id,service='rwp',crt={'sum':sums_cnd,'avg':avgs_cnd,'count':count},olc={'sum':sums_spn,'avg':avgs_spn,'count':count},drc={'sum':sums_tsp,'avg':avgs_tsp,'count':count},spn={'sum':sums_asp,'avg':avgs_asp,'count':count},month=dd[1],year=dd[0],day=dd[2],hour=dd[3])
                else:
                    yr_data=rwp_repo_monthly.objects.create(device_id=device_id,service='rwp',crt={'sum':sums_cnd,'avg':avgs_cnd,'count':count},olc={'sum':sums_spn,'avg':avgs_spn,'count':count},drc={'sum':sums_tsp,'avg':avgs_tsp,'count':count},spn={'sum':sums_asp,'avg':avgs_asp,'count':count},month=dd[1],year=dd[0],day=dd[2],hour=dd[3])
                    yr_data.save()
               
                # year
                yrdata=treat_rwp.objects.filter(year=dd[0],device_id=device_id)
                count=0
                sums_cnd=0
                sums_spn=0
                sums_tsp=0
                sums_asp=0
                avgs_cnd = 0
                avgs_spn = 0
                avgs_tsp = 0
                avgs_asp = 0
                if yrdata:
                    for yr in yrdata:
                        yr_d_id=yr.device_id
                        if yr_d_id == device_id:
                            # cnds_m=yr.crt
                            # spns_m=yr.olc
                            # tsps_m=yr.drc
                            # asps_m=yr.spn
                            # sums_d=list(cnds_m.values())[0]
                            # sums_s=list(spns_m.values())[0]
                            # sums_t=list(tsps_m.values())[0]
                            # sums_a=list(asps_m.values())[0]
                            # # avgs_cnd=list(cnds.values())[1]
                            # count_cnd=list(cnds_d.values())[2]
                            # # for k,v in cnds.items():
                            # sums_cnd=sums_cnd+sums_d
                            # sums_spn=sums_spn+sums_s
                            # sums_tsp=sums_tsp+sums_t
                            # sums_asp=sums_asp+sums_a
                            # sums_cnd=sums_cnd+cnds
                            # sums_spn=sums_spn+spns
                            # sums_tsp=sums_tsp+tsps
                            # sums_asp=sums_asp+asps
                            # count=count+1
                            cnds=yr.crt
                            spns=yr.olc
                            tsps=yr.drc
                            asps=yr.spn
                            print("cnds is:",cnds)
                            sums_cnd=sums_cnd+cnds
                            sums_spn=sums_spn+spns
                            sums_tsp=sums_tsp+tsps
                            sums_asp=sums_asp+asps
                            count=count+1
                            count_sum=count_sum+count_cnd


                            print("sum from dict:",sums_cnd,type(sums_cnd))
                            # spns=yr.spn[1]
                            # tsps=yr.tsp[2]
                            # asps=yr.asp[3]
                            print("cnds is:",cnds)
                            # sums_cnd=sums_cnd+cnds
                            # sums_spn=sums_spn+spns
                            # sums_tsp=sums_tsp+tsps
                            # sums_asp=sums_asp+asps
                            # count=count+1
                            print("count is:",count)
                    print("sums is:",sums_cnd)
                    print("countsum is:",count_sum)
                    avgs_cnd=sums_cnd/count
                    print("average cnd is:",avgs_cnd)

                    avgs_spn=sums_spn/count
                    print("avg of spn11:",avgs_spn)
                    avgs_tsp=sums_tsp/count
                    avgs_asp=sums_asp/count
                hr=rwp_repo_yearly.objects.filter(year=dd[0],device_id=device_id)
                if hr:
                    yr_data=rwp_repo_yearly.objects.filter(device_id=device_id).update(device_id=device_id,service='rwp',crt={'sum':sums_cnd,'avg':avgs_cnd,'count':count},olc={'sum':sums_spn,'avg':avgs_spn,'count':count},drc={'sum':sums_tsp,'avg':avgs_tsp,'count':count},spn={'sum':sums_asp,'avg':avgs_asp,'count':count},month=dd[1],year=dd[0],day=dd[2],hour=dd[3])
                else:
                    yr_data=rwp_repo_yearly.objects.create(device_id=device_id,service='rwp',crt={'sum':sums_cnd,'avg':avgs_cnd,'count':count},olc={'sum':sums_spn,'avg':avgs_spn,'count':count},drc={'sum':sums_tsp,'avg':avgs_tsp,'count':count},spn={'sum':sums_asp,'avg':avgs_asp,'count':count},month=dd[1],year=dd[0],day=dd[2],hour=dd[3])
                    yr_data.save()
                    
                # yrdata=treat_rwp.objects.filter(year=dd[0],device_id=device_id)
                # count=0
                # sums=0
                # avgs = 0
                # if yrdata:
                #     for yr in yrdata:
                #         yr_d_id=yr.device_id
                #         if yr_d_id == device_id:
                #             crt=yr.crt
                #             print("crt is:",crt)
                #             sums=sums+crt
                #             count=count+1
                #             print("sums is:",sums)
                #             print("count is:",count)
                #     avgs=sums/count
                #     print('avg is:',avgs)
                # hr=repo_yearly.objects.filter(year=dd[0],device_id=device_id)
                # if hr:
                #     yr_data=repo_yearly.objects.filter(device_id=device_id).update(device_id=device_id,service='hpp',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
                # else:
                #     yr_data=repo_yearly.objects.create(device_id=device_id,service='hpp',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
                #     yr_data.save()
                
                # # month
                # yrdata=treat_rwp.objects.filter(year=dd[0],month=dd[1],device_id=device_id)
                # count=0
                # sums=0
                # avgs = 0
                # if yrdata:
                #     for yr in yrdata:
                #         yr_d_id=yr.device_id
                #         if yr_d_id == device_id:
                #             crt=yr.crt
                #             print("crt is:",crt)
                #             sums=sums+crt
                #             count=count+1
                #             print("sums is:",sums)
                #             print("count is:",count)
                #     avgs=sums/count
                # hr=repo_monthly.objects.filter(year=dd[0],month=dd[1],device_id=device_id)
                # if hr:
                #     yr_data=repo_monthly.objects.filter(year=dd[0],month=dd[1],device_id=device_id).update(device_id=device_id,service='hpp',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
                # else:
                #     yr_data=repo_monthly.objects.create(device_id=device_id,service='hpp',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
                #     yr_data.save()
                
                # # day
                # yrdata=treat_rwp.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id)
                # count=0
                # sums=0
                # avgs = 0
                # if yrdata:
                #     for yr in yrdata:
                #         yr_d_id=yr.device_id
                #         if yr_d_id == device_id:
                #             crt=yr.crt
                #             print("crt is:",crt)
                #             sums=sums+crt
                #             count=count+1
                #             print("sums is:",sums)
                #             print("count is:",count)
                #     avgs=sums/count
                # hr=repo_daily.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id)
                # if hr:
                #     yr_data=repo_daily.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id).update(device_id=device_id,service='hpp',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0],day=dd[2])
                # else:
                #     yr_data=repo_daily.objects.create(device_id=device_id,service='hpp',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0],day=dd[2])
                #     yr_data.save()
                
                # # hour
                # yrdata=treat_rwp.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id)
                # count=0
                # sums=0

                # avgs = 0
                # if yrdata:
                #     for yr in yrdata:
                #         yr_d_id=yr.device_id
                #         if yr_d_id == device_id:
                #             crt=yr.crt
                #             print("crt is:",crt)
                #             sums=sums+crt
                #             count=count+1
                #             print("sums is:",sums)
                #             print("count is:",count)
                #     avgs=sums/count
                
                # hr=repo_hourly.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id)
                # if hr:
                #     yr_data=repo_hourly.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id).update(device_id=device_id,service='hpp',sum=sums,count=count,avg=avgs,hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                # else:
                #     yr_data=repo_hourly.objects.create(device_id=device_id,service='hpp',sum=sums,count=count,avg=avgs,hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                #     yr_data.save()
                
        
        except Exception as e:
            print("error ==>", e)
            error_message = e
            # global eg
            eg = e
            print("eg is:",eg)
            print("Error massage:",e)
            EchoConsumer.websocket_receive('event','event')           
        try:
            if 'hpp'==components:
                # com=cl
                if device_id not in device_idlist:
                     repo_latestdata.objects.create(device_id=device_id,message_type=msg_type,hpp=mydata1)
                else:
                    repo_latestobj = repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id, message_type=msg_type, hpp=mydata1)

                    get_device_id=repo_latestdata.objects.all()
                    for did in get_device_id:
                        s=str(did.device_id)
                        if device_id == s:
                            hpp=did.hpp
                    klist = list(hpp.keys())
                    print("klist is:",klist)
                    mydatakey = list(mydata1.keys())
                    print("mydatakey:",mydatakey)
                    for k,v in hpp.items():
                         if k not in mydatakey:
                              olddata.update({k:v})
                              
                    mydata5=olddata.update(mydata1)    
                    print("old data is:",olddata) # add/update keys in mydata1 to olddata
                    repo_latestobj = repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id, message_type=msg_type, hpp=olddata)

                ds=treat_hpp.objects.create(device_id=device_id,message_type=msg_type,sts=sts,crt=crt,olc=olc,drc=drc,spn=spn,year=dd[0],month=dd[1],day=dd[2],hour=dd[3],minit=dd[4],second=dd[5])
                ds.save()
                 # hour
                yrdata=treat_hpp.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id)
                count=0
                sumd={}
                sums_cnd=0
                sums_spn=0
                sums_tsp=0
                sums_asp=0
                avgs_cnd = 0
                avgs_spn = 0
                avgs_tsp = 0
                avgs_asp = 0
                if yrdata:
                    for yr in yrdata:
                        yr_d_id=yr.device_id
                        if yr_d_id == device_id:
                            cnds=yr.crt
                            spns=yr.olc
                            tsps=yr.drc
                            asps=yr.spn
                            print("cnds is:",cnds)
                            sums_cnd=sums_cnd+cnds
                            sums_spn=sums_spn+spns
                            sums_tsp=sums_tsp+tsps
                            sums_asp=sums_asp+asps
                            count=count+1
                            print("sums is:",sums_cnd)
                            print("count is:",count)
                    avgs_cnd=sums_cnd/count
                    avgs_spn=sums_spn/count
                    avgs_tsp=sums_tsp/count
                    avgs_asp=sums_asp/count
                    print("@@@")
               
                hr=hpp_repo_hourly.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id)
                if hr:
                    yr_data=hpp_repo_hourly.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id).update(device_id=device_id,service='hpp',crt={'sum':sums_cnd,'avg':avgs_cnd,'count':count},olc={'sum':sums_spn,'avg':avgs_spn,'count':count},drc={'sum':sums_tsp,'avg':avgs_tsp,'count':count},spn={'sum':sums_asp,'avg':avgs_asp,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                else:
                    yr_data=hpp_repo_hourly.objects.create(device_id=device_id,service='hpp',crt={'sum':sums_cnd,'avg':avgs_cnd,'count':count},olc={'sum':sums_spn,'avg':avgs_spn,'count':count},drc={'sum':sums_tsp,'avg':avgs_tsp,'count':count},spn={'sum':sums_asp,'avg':avgs_asp,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                    yr_data.save()
               
                 # day
                yrdata=treat_hpp.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id)
                count=0
                count_sum=0
                count_cnd=0
                count_spn=0
                count_tsp=0
                count_asp=0
                sums_cnd=0
                sums_spn=0
                sums_tsp=0
                sums_asp=0
                avgs_cnd = 0
                avgs_spn = 0
                avgs_tsp = 0
                avgs_asp = 0
                if yrdata:
                    for yr in yrdata:
                        print("day for loop")
                        yr_d_id=yr.device_id
                        if yr_d_id == device_id:
                            print("in if")
                            cnds=yr.crt
                            spns=yr.olc
                            tsps=yr.drc
                            asps=yr.spn
                            # sums_d=list(cnds_d.values())[0]
                            # sums_s=list(spns_d.values())[0]
                            # sums_t=list(tsps_d.values())[0]
                            # sums_a=list(asps_d.values())[0]
                            # # avgs_cnd=list(cnds.values())[1]
                            # count_cnd=list(cnds_d.values())[2]
                            # # for k,v in cnds.items():
                            # sums_cnd=sums_cnd+sums_d
                            # sums_spn=sums_spn+sums_s
                            # sums_tsp=sums_tsp+sums_t
                            # sums_asp=sums_asp+sums_a
                            sums_cnd=sums_cnd+cnds
                            sums_spn=sums_spn+spns
                            sums_tsp=sums_tsp+tsps
                            sums_asp=sums_asp+asps
                            count=count+1
                            count_sum=count_sum+count_cnd


                            print("sum from dict:",sums_cnd,type(sums_cnd))
                            # spns=yr.spn[1]
                            # tsps=yr.tsp[2]
                            # asps=yr.asp[3]
                            print("cnds is:",cnds)
                            # sums_cnd=sums_cnd+cnds
                            # sums_spn=sums_spn+spns
                            # sums_tsp=sums_tsp+tsps
                            # sums_asp=sums_asp+asps
                            # count=count+1
                            print("count is:",count)
                    print("sums is:",sums_cnd)
                    print("countsum is:",count_sum)
                    avgs_cnd=sums_cnd/count
                    print("average cnd is:",avgs_cnd)

                    avgs_spn=sums_spn/count
                    print("avg of spn:",avgs_spn)
                    avgs_tsp=sums_tsp/count
                    avgs_asp=sums_asp/count
                hr=hpp_repo_daily.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id)
                if hr:
                    print("in if hr")
                    yr_data=hpp_repo_daily.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id).update(device_id=device_id,service='hpp',crt={'sum':sums_cnd,'avg':avgs_cnd,'count':count},olc={'sum':sums_spn,'avg':avgs_spn,'count':count},drc={'sum':sums_tsp,'avg':avgs_tsp,'count':count},spn={'sum':sums_asp,'avg':avgs_asp,'count':count},month=dd[1],year=dd[0],day=dd[2],hour=dd[3])
                    print("data insertedd")
                else:
                    yr_data=hpp_repo_daily.objects.create(device_id=device_id,service='hpp',crt={'sum':sums_cnd,'avg':avgs_cnd,'count':count},olc={'sum':sums_spn,'avg':avgs_spn,'count':count},drc={'sum':sums_tsp,'avg':avgs_tsp,'count':count},spn={'sum':sums_asp,'avg':avgs_asp,'count':count},month=dd[1],year=dd[0],day=dd[2],hour=dd[3])
                    yr_data.save()
                #monthly
                yrdata=treat_hpp.objects.filter(year=dd[0],month=dd[1],device_id=device_id)
                count=0
                sums_cnd=0
                sums_spn=0
                sums_tsp=0
                sums_asp=0
                avgs_cnd = 0
                avgs_spn = 0
                avgs_tsp = 0
                avgs_asp = 0
                if yrdata:
                    for yr in yrdata:
                        yr_d_id=yr.device_id
                        if yr_d_id == device_id:
                            cnds=yr.crt
                            spns=yr.olc
                            tsps=yr.drc
                            asps=yr.spn
                            # sums_d=list(cnds_m.values())[0]
                            # sums_s=list(spns_m.values())[0]
                            # sums_t=list(tsps_m.values())[0]
                            # sums_a=list(asps_m.values())[0]
                            # # avgs_cnd=list(cnds.values())[1]
                            # count_cnd=list(cnds_d.values())[2]
                            # # for k,v in cnds.items():
                            # sums_cnd=sums_cnd+sums_d
                            # sums_spn=sums_spn+sums_s
                            # sums_tsp=sums_tsp+sums_t
                            # sums_asp=sums_asp+sums_a
                            sums_cnd=sums_cnd+cnds
                            sums_spn=sums_spn+spns
                            sums_tsp=sums_tsp+tsps
                            sums_asp=sums_asp+asps
                            # count=count+1
                            count_sum=count_sum+count_cnd


                            print("sum from dict:",sums_cnd,type(sums_cnd))
                            # spns=yr.spn[1]
                            # tsps=yr.tsp[2]
                            # asps=yr.asp[3]
                            print("cnds is:",cnds)
                            # sums_cnd=sums_cnd+cnds
                            # sums_spn=sums_spn+spns
                            # sums_tsp=sums_tsp+tsps
                            # sums_asp=sums_asp+asps
                            count=count+1
                            print("count is:",count)
                    print("sums is:",sums_cnd)
                    print("countsum is:",count_sum)
                    avgs_cnd=sums_cnd/count
                    print("average cnd is:",avgs_cnd)

                    avgs_spn=sums_spn/count
                    print("avg of spn:",avgs_spn)
                    avgs_tsp=sums_tsp/count
                    avgs_asp=sums_asp/count
                hr=hpp_repo_monthly.objects.filter(year=dd[0],month=dd[1],device_id=device_id)
                if hr:
                    yr_data=hpp_repo_monthly.objects.filter(year=dd[0],month=dd[1],device_id=device_id).update(device_id=device_id,service='rwp',crt={'sum':sums_cnd,'avg':avgs_cnd,'count':count},olc={'sum':sums_spn,'avg':avgs_spn,'count':count},drc={'sum':sums_tsp,'avg':avgs_tsp,'count':count},spn={'sum':sums_asp,'avg':avgs_asp,'count':count},month=dd[1],year=dd[0],day=dd[2],hour=dd[3])
                else:
                    yr_data=hpp_repo_monthly.objects.create(device_id=device_id,service='rwp',crt={'sum':sums_cnd,'avg':avgs_cnd,'count':count},olc={'sum':sums_spn,'avg':avgs_spn,'count':count},drc={'sum':sums_tsp,'avg':avgs_tsp,'count':count},spn={'sum':sums_asp,'avg':avgs_asp,'count':count},month=dd[1],year=dd[0],day=dd[2],hour=dd[3])
                    yr_data.save()
               
                # year
                yrdata=treat_hpp.objects.filter(year=dd[0],device_id=device_id)
                count=0
                sums_cnd=0
                sums_spn=0
                sums_tsp=0
                sums_asp=0
                avgs_cnd = 0
                avgs_spn = 0
                avgs_tsp = 0
                avgs_asp = 0
                if yrdata:
                    for yr in yrdata:
                        yr_d_id=yr.device_id
                        if yr_d_id == device_id:
                            cnds=yr.crt
                            spns=yr.olc
                            tsps=yr.drc
                            asps=yr.spn
                            sums_cnd=sums_cnd+cnds
                            sums_spn=sums_spn+spns
                            sums_tsp=sums_tsp+tsps
                            sums_asp=sums_asp+asps
                            # count=count+1
                            count_sum=count_sum+count_cnd


                            print("sum from dict:",sums_cnd,type(sums_cnd))
                            # spns=yr.spn[1]
                            # tsps=yr.tsp[2]
                            # asps=yr.asp[3]
                            print("cnds is:",cnds)
                            # sums_cnd=sums_cnd+cnds
                            # sums_spn=sums_spn+spns
                            # sums_tsp=sums_tsp+tsps
                            # sums_asp=sums_asp+asps
                            count=count+1
                            print("count is:",count)
                    print("sums is:",sums_cnd)
                    print("countsum is:",count_sum)
                    avgs_cnd=sums_cnd/count
                    print("average cnd is:",avgs_cnd)

                    avgs_spn=sums_spn/count
                    print("avg of spn:",avgs_spn)
                    avgs_tsp=sums_tsp/count
                    avgs_asp=sums_asp/count
                hr=hpp_repo_yearly.objects.filter(year=dd[0],device_id=device_id)
                if hr:
                    yr_data=hpp_repo_yearly.objects.filter(device_id=device_id).update(device_id=device_id,service='rwp',crt={'sum':sums_cnd,'avg':avgs_cnd,'count':count},olc={'sum':sums_spn,'avg':avgs_spn,'count':count},drc={'sum':sums_tsp,'avg':avgs_tsp,'count':count},spn={'sum':sums_asp,'avg':avgs_asp,'count':count},month=dd[1],year=dd[0],day=dd[2],hour=dd[3])
                else:
                    yr_data=hpp_repo_yearly.objects.create(device_id=device_id,service='rwp',crt={'sum':sums_cnd,'avg':avgs_cnd,'count':count},olc={'sum':sums_spn,'avg':avgs_spn,'count':count},drc={'sum':sums_tsp,'avg':avgs_tsp,'count':count},spn={'sum':sums_asp,'avg':avgs_asp,'count':count},month=dd[1],year=dd[0],day=dd[2],hour=dd[3])
                    yr_data.save()
                
                # count=0
                # sums=0
                # avgs = 0
                # if yrdata:
                #     for yr in yrdata:
                #         yr_d_id=yr.device_id
                #         if yr_d_id == device_id:
                #             crt=yr.crt
                #             print("crt is:",crt)
                #             sums=sums+crt
                #             count=count+1
                #             print("sums is:",sums)
                #             print("count is:",count)
                #     avgs=sums/count
                #     print('avg is:',avgs)
                # hr=repo_yearly.objects.filter(year=dd[0],device_id=device_id)
                # if hr:
                #     yr_data=repo_yearly.objects.filter(device_id=device_id).update(device_id=device_id,service='hpp_crt',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
                # else:
                #     yr_data=repo_yearly.objects.create(device_id=device_id,service='hpp_crt',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
                #     yr_data.save()
                # # month
                # yrdata=treat_hpp.objects.filter(year=dd[0],month=dd[1],device_id=device_id)
                # count=0
                # sums=0
                # avgs = 0
                # if yrdata:
                #     for yr in yrdata:
                #         yr_d_id=yr.device_id
                #         if yr_d_id == device_id:
                #             crt=yr.crt
                #             print("crt is:",crt)
                #             sums=sums+crt
                #             count=count+1
                #             print("sums is:",sums)
                #             print("count is:",count)
                #     avgs=sums/count
                # hr=repo_monthly.objects.filter(year=dd[0],month=dd[1],device_id=device_id)
                # if hr:
                #     yr_data=repo_monthly.objects.filter(year=dd[0],month=dd[1],device_id=device_id).update(device_id=device_id,service='hpp_crt',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
                # else:
                #     yr_data=repo_monthly.objects.create(device_id=device_id,service='hpp_crt',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
                #     yr_data.save()
                # # day
                # yrdata=treat_hpp.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id)
                # count=0
                # sums=0
                # avgs = 0
                # if yrdata:
                #     for yr in yrdata:
                #         yr_d_id=yr.device_id
                #         if yr_d_id == device_id:
                #             crt=yr.crt
                #             print("crt is:",crt)
                #             sums=sums+crt
                #             count=count+1
                #             print("sums is:",sums)
                #             print("count is:",count)
                #     avgs=sums/count
                # hr=repo_daily.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id)
                # if hr:
                #     yr_data=repo_daily.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id).update(device_id=device_id,service='hpp_crt',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0],day=dd[2])
                # else:
                #     yr_data=repo_daily.objects.create(device_id=device_id,service='hpp_crt',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0],day=dd[2])
                #     yr_data.save()
                # # hour
                # yrdata=treat_hpp.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id)
                # count=0
                # sums=0
                # avgs = 0
                # if yrdata:
                #     for yr in yrdata:
                #         yr_d_id=yr.device_id
                #         if yr_d_id == device_id:
                #             crt=yr.crt
                #             print("crt is:",crt)
                #             sums=sums+crt
                #             count=count+1
                #             print("sums is:",sums)
                #             print("count is:",count)
                #     avgs=sums/count
                # hr=repo_hourly.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id)
                # if hr:
                #     yr_data=repo_hourly.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id).update(device_id=device_id,service='hpp_crt',sum=sums,count=count,avg=avgs,hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                # else:
                #     yr_data=repo_hourly.objects.create(device_id=device_id,service='hpp_crt',sum=sums,count=count,avg=avgs,hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                #     yr_data.save()
                
                # end_date = local_tz.localize(datetime.datetime.now())
                # print("first end date is:",end_date)
                # end_date = end_date.replace(tzinfo=local_tz)
                # print("replaced date :",end_date)
                # # start_date = end_date + relativedelta(hours=-8760)
                # start_date = end_date + relativedelta(hours=-1)
                # print("staredate is:",start_date)
                # yrdata=treat_hpp.objects.filter(created_at__range=(start_date, end_date))
                # count=0
                # sums=0
                # for yr in yrdata:
                #     yr_d_id=yr.device_id
                #     if yr_d_id == device_id:
                #         crt=yr.crt
                #         print("crt is:",crt)
                #         sums=sums+crt
                #         count=count+1
                #         print("sums is:",sums)
                #         print("count is:",count)
                # avgs=sums/count
                # print('avg is:',avgs)
                # if device_id not in device_idlist:
                #     yr_data=repo_hourly.objects.create(device_id=device_id,service='hpp_crt',sum=sums,count=count,avg=avgs)
                #     yr_data.save()
                # else:
                #     yr_data=repo_hourly.objects.filter(device_id=device_id).update(device_id=device_id,service='hpp_crt',sum=sums,count=count,avg=avgs)
        except Exception as e:
            print("error ==>", e)
            error_message = e
            # global eg
            eg = e
            print("eg is:",eg)
            print("Error massage:",e)
            EchoConsumer.websocket_receive('event','event')  
        try:
            if 'panel'==components:
                # com=cl
                if device_id not in device_idlist:
                     repo_latestdata.objects.create(device_id=device_id,message_type=msg_type,panel=mydata1)
                else:
                    repo_latestobj = repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id, message_type=msg_type, panel=mydata1)

                    get_device_id=repo_latestdata.objects.all()
                    for did in get_device_id:
                        s=str(did.device_id)
                        if device_id == s:
                            panel=did.panel
                    klist = list(panel.keys())
                    print("klist is:",klist)
                    mydatakey = list(mydata1.keys())
                    print("mydatakey:",mydatakey)
                    for k,v in panel.items():
                         if k not in mydatakey:
                              olddata.update({k:v})
                              
                    mydata5=olddata.update(mydata1)    
                    print("old data is:",olddata) # add/update keys in mydata1 to olddata
                    repo_latestobj = repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id, message_type=msg_type, panel=olddata)

                ds=treat_panel.objects.create(device_id=device_id,message_type=msg_type,sts=sts,rtl=rtl,ttl=ttl,lps=lps,hps=hps,dgp=dgp,mod=mod,ipv=ipv,unv=unv,ovv=ovv,spn=spn,nmv=nmv,stp=stp,srt=srt,bkt=bkt,rst=rst,err=err,year=dd[0],month=dd[1],day=dd[2],hour=dd[3],minit=dd[4],second=dd[5])
                ds.save()
                #hour
                yrdata=treat_panel.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id)
                count=0
                sums_ipv=0
                sums_unv=0
                sums_ovv=0
                sums_spn=0
                sums_nmv=0
                sums_srt=0
                sums_bkt=0
                sums_rst=0
                avgs_ipv = 0
                avgs_unv = 0
                avgs_ovv = 0
                avgs_spn = 0
                avgs_nmv = 0
                avgs_srt = 0
                avgs_bkt = 0
                avgs_rst = 0
                if yrdata:
                    for yr in yrdata:
                        yr_d_id=yr.device_id
                        if yr_d_id == device_id:
                            ipv=yr.ipv
                            unv=yr.unv
                            ovv=yr.ovv
                            spn=yr.spn
                            nmv=yr.nmv
                            srt=yr.srt
                            bkt=yr.bkt
                            rst=yr.rst
                            sums_ipv=sums_ipv+ipv
                            sums_unv=sums_unv+unv
                            sums_ovv=sums_ovv+ovv
                            sums_spn=sums_spn+spn
                            sums_nmv=sums_nmv+nmv
                            sums_srt=sums_srt+srt
                            sums_bkt=sums_bkt+bkt
                            sums_rst=sums_rst+rst
                            count=count+1
                            print("count is:",count)
                    avgs_ipv=sums_ipv/count
                    print("average cnd is:",avgs_ipv)
                    avgs_unv=sums_unv/count
                    print("avg of spn:",avgs_unv)
                    avgs_ovv=sums_ovv/count
                    avgs_spn=sums_spn/count
                    avgs_nmv=sums_nmv/count
                    avgs_srt=sums_srt/count
                    avgs_bkt=sums_bkt/count
                    avgs_rst=sums_rst/count
                hr=panel_repo_hourly.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id)
                if hr:
                    yr_data=panel_repo_hourly.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id).update(device_id=device_id,service='panel',ipv={'sum':sums_ipv,'avg':avgs_ipv,'count':count},unv={'sum':sums_unv,'avg':avgs_unv,'count':count},ovv={'sum':sums_ovv,'avg':avgs_ovv,'count':count},spn={'sum':sums_spn,'avg':avgs_spn,'count':count},nmv={'sum':sums_nmv,'avg':avgs_nmv,'count':count},srt={'sum':sums_srt,'avg':avgs_srt,'count':count},bkt={'sum':sums_bkt,'avg':avgs_bkt,'count':count},rst={'sum':sums_rst,'avg':avgs_rst,'count':count},month=dd[1],year=dd[0],day=dd[2],hour=dd[3])
                else:
                    yr_data=panel_repo_hourly.objects.create(device_id=device_id,service='panel',ipv={'sum':sums_ipv,'avg':avgs_ipv,'count':count},unv={'sum':sums_unv,'avg':avgs_unv,'count':count},ovv={'sum':sums_ovv,'avg':avgs_ovv,'count':count},spn={'sum':sums_spn,'avg':avgs_spn,'count':count},nmv={'sum':sums_nmv,'avg':avgs_nmv,'count':count},srt={'sum':sums_srt,'avg':avgs_srt,'count':count},bkt={'sum':sums_bkt,'avg':avgs_bkt,'count':count},rst={'sum':sums_rst,'avg':avgs_rst,'count':count},month=dd[1],year=dd[0],day=dd[2],hour=dd[3])
                    yr_data.save()
                # month
                yrdata=treat_panel.objects.filter(year=dd[0],month=dd[1],device_id=device_id)
                count=0
                sums_ipv=0
                sums_unv=0
                sums_ovv=0
                sums_spn=0
                sums_nmv=0
                sums_srt=0
                sums_bkt=0
                sums_rst=0
                avgs_ipv = 0
                avgs_unv = 0
                avgs_ovv = 0
                avgs_spn = 0
                avgs_nmv = 0
                avgs_srt = 0
                avgs_bkt = 0
                avgs_rst = 0
                if yrdata:
                    for yr in yrdata:
                        yr_d_id=yr.device_id
                        if yr_d_id == device_id:
                            ipv=yr.ipv
                            unv=yr.unv
                            ovv=yr.ovv
                            spn=yr.spn
                            nmv=yr.nmv
                            srt=yr.srt
                            bkt=yr.bkt
                            rst=yr.rst
                            sums_ipv=sums_ipv+ipv
                            sums_unv=sums_unv+unv
                            sums_ovv=sums_ovv+ovv
                            sums_spn=sums_spn+spn
                            sums_nmv=sums_nmv+nmv
                            sums_srt=sums_srt+srt
                            sums_bkt=sums_bkt+bkt
                            sums_rst=sums_rst+rst
                            count=count+1
                            print("count is:",count)
                    avgs_ipv=sums_ipv/count
                    print("average cnd is:",avgs_ipv)
                    avgs_unv=sums_unv/count
                    print("avg of spn:",avgs_unv)
                    avgs_ovv=sums_ovv/count
                    avgs_spn=sums_spn/count
                    avgs_nmv=sums_nmv/count
                    avgs_srt=sums_srt/count
                    avgs_bkt=sums_bkt/count
                    avgs_rst=sums_rst/count
                hr=panel_repo_monthly.objects.filter(year=dd[0],month=dd[1],device_id=device_id)
                if hr:
                    yr_data=panel_repo_monthly.objects.filter(year=dd[0],month=dd[1],device_id=device_id).update(device_id=device_id,service='panel',ipv={'sum':sums_ipv,'avg':avgs_ipv,'count':count},unv={'sum':sums_unv,'avg':avgs_unv,'count':count},ovv={'sum':sums_ovv,'avg':avgs_ovv,'count':count},spn={'sum':sums_spn,'avg':avgs_spn,'count':count},nmv={'sum':sums_nmv,'avg':avgs_nmv,'count':count},srt={'sum':sums_srt,'avg':avgs_srt,'count':count},bkt={'sum':sums_bkt,'avg':avgs_bkt,'count':count},rst={'sum':sums_rst,'avg':avgs_rst,'count':count},month=dd[1],year=dd[0],day=dd[2],hour=dd[3])
                else:
                    yr_data=panel_repo_monthly.objects.create(device_id=device_id,service='panel',ipv={'sum':sums_ipv,'avg':avgs_ipv,'count':count},unv={'sum':sums_unv,'avg':avgs_unv,'count':count},ovv={'sum':sums_ovv,'avg':avgs_ovv,'count':count},spn={'sum':sums_spn,'avg':avgs_spn,'count':count},nmv={'sum':sums_nmv,'avg':avgs_nmv,'count':count},srt={'sum':sums_srt,'avg':avgs_srt,'count':count},bkt={'sum':sums_bkt,'avg':avgs_bkt,'count':count},rst={'sum':sums_rst,'avg':avgs_rst,'count':count},month=dd[1],year=dd[0],day=dd[2],hour=dd[3])
                    yr_data.save()
              # day
                yrdata=treat_panel.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id)
                count=0
                sums_ipv=0
                sums_unv=0
                sums_ovv=0
                sums_spn=0
                sums_nmv=0
                sums_srt=0
                sums_bkt=0
                sums_rst=0
                avgs_ipv = 0
                avgs_unv = 0
                avgs_ovv = 0
                avgs_spn = 0
                avgs_nmv = 0
                avgs_srt = 0
                avgs_bkt = 0
                avgs_rst = 0
                if yrdata:
                    for yr in yrdata:
                        yr_d_id=yr.device_id
                        if yr_d_id == device_id:
                            ipv=yr.ipv
                            unv=yr.unv
                            ovv=yr.ovv
                            spn=yr.spn
                            nmv=yr.nmv
                            srt=yr.srt
                            bkt=yr.bkt
                            rst=yr.rst
                            sums_ipv=sums_ipv+ipv
                            sums_unv=sums_unv+unv
                            sums_ovv=sums_ovv+ovv
                            sums_spn=sums_spn+spn
                            sums_nmv=sums_nmv+nmv
                            sums_srt=sums_srt+srt
                            sums_bkt=sums_bkt+bkt
                            sums_rst=sums_rst+rst
                            count=count+1
                            print("count is:",count)
                    avgs_ipv=sums_ipv/count
                    print("average cnd is:",avgs_ipv)
                    avgs_unv=sums_unv/count
                    print("avg of spn:",avgs_unv)
                    avgs_ovv=sums_ovv/count
                    avgs_spn=sums_spn/count
                    avgs_nmv=sums_nmv/count
                    avgs_srt=sums_srt/count
                    avgs_bkt=sums_bkt/count
                    avgs_rst=sums_rst/count
                hr=panel_repo_daily.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id)
                if hr:
                    yr_data=panel_repo_daily.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id).update(device_id=device_id,service='panel',ipv={'sum':sums_ipv,'avg':avgs_ipv,'count':count},unv={'sum':sums_unv,'avg':avgs_unv,'count':count},ovv={'sum':sums_ovv,'avg':avgs_ovv,'count':count},spn={'sum':sums_spn,'avg':avgs_spn,'count':count},nmv={'sum':sums_nmv,'avg':avgs_nmv,'count':count},srt={'sum':sums_srt,'avg':avgs_srt,'count':count},bkt={'sum':sums_bkt,'avg':avgs_bkt,'count':count},rst={'sum':sums_rst,'avg':avgs_rst,'count':count},month=dd[1],year=dd[0],day=dd[2],hour=dd[3])
                else:
                    yr_data=panel_repo_daily.objects.create(device_id=device_id,service='panel',ipv={'sum':sums_ipv,'avg':avgs_ipv,'count':count},unv={'sum':sums_unv,'avg':avgs_unv,'count':count},ovv={'sum':sums_ovv,'avg':avgs_ovv,'count':count},spn={'sum':sums_spn,'avg':avgs_spn,'count':count},nmv={'sum':sums_nmv,'avg':avgs_nmv,'count':count},srt={'sum':sums_srt,'avg':avgs_srt,'count':count},bkt={'sum':sums_bkt,'avg':avgs_bkt,'count':count},rst={'sum':sums_rst,'avg':avgs_rst,'count':count},month=dd[1],year=dd[0],day=dd[2],hour=dd[3])
                    yr_data.save()
               #year
                yrdata=treat_panel.objects.filter(year=dd[0],device_id=device_id)
                count=0
                sums_ipv=0
                sums_unv=0
                sums_ovv=0
                sums_spn=0
                sums_nmv=0
                sums_srt=0
                sums_bkt=0
                sums_rst=0
                avgs_ipv = 0
                avgs_unv = 0
                avgs_ovv = 0
                avgs_spn = 0
                avgs_nmv = 0
                avgs_srt = 0
                avgs_bkt = 0
                avgs_rst = 0
                if yrdata:
                    for yr in yrdata:
                        yr_d_id=yr.device_id
                        if yr_d_id == device_id:
                            ipv=yr.ipv
                            unv=yr.unv
                            ovv=yr.ovv
                            spn=yr.spn
                            nmv=yr.nmv
                            srt=yr.srt
                            bkt=yr.bkt
                            rst=yr.rst
                            sums_ipv=sums_ipv+ipv
                            sums_unv=sums_unv+unv
                            sums_ovv=sums_ovv+ovv
                            sums_spn=sums_spn+spn
                            sums_nmv=sums_nmv+nmv
                            sums_srt=sums_srt+srt
                            sums_bkt=sums_bkt+bkt
                            sums_rst=sums_rst+rst
                            count=count+1
                            print("count is:",count)
                    avgs_ipv=sums_ipv/count
                    print("average cnd is:",avgs_ipv)
                    avgs_unv=sums_unv/count
                    print("avg of spn:",avgs_unv)
                    avgs_ovv=sums_ovv/count
                    avgs_spn=sums_spn/count
                    avgs_nmv=sums_nmv/count
                    avgs_srt=sums_srt/count
                    avgs_bkt=sums_bkt/count
                    avgs_rst=sums_rst/count
                hr=panel_repo_yearly.objects.filter(year=dd[0],device_id=device_id)
                if hr:
                    yr_data=panel_repo_yearly.objects.filter(year=dd[0],device_id=device_id).update(device_id=device_id,service='panel',ipv={'sum':sums_ipv,'avg':avgs_ipv,'count':count},unv={'sum':sums_unv,'avg':avgs_unv,'count':count},ovv={'sum':sums_ovv,'avg':avgs_ovv,'count':count},spn={'sum':sums_spn,'avg':avgs_spn,'count':count},nmv={'sum':sums_nmv,'avg':avgs_nmv,'count':count},srt={'sum':sums_srt,'avg':avgs_srt,'count':count},bkt={'sum':sums_bkt,'avg':avgs_bkt,'count':count},rst={'sum':sums_rst,'avg':avgs_rst,'count':count},month=dd[1],year=dd[0],day=dd[2],hour=dd[3])
                else:
                    yr_data=panel_repo_yearly.objects.create(device_id=device_id,service='panel',ipv={'sum':sums_ipv,'avg':avgs_ipv,'count':count},unv={'sum':sums_unv,'avg':avgs_unv,'count':count},ovv={'sum':sums_ovv,'avg':avgs_ovv,'count':count},spn={'sum':sums_spn,'avg':avgs_spn,'count':count},nmv={'sum':sums_nmv,'avg':avgs_nmv,'count':count},srt={'sum':sums_srt,'avg':avgs_srt,'count':count},bkt={'sum':sums_bkt,'avg':avgs_bkt,'count':count},rst={'sum':sums_rst,'avg':avgs_rst,'count':count},month=dd[1],year=dd[0],day=dd[2],hour=dd[3])
                    yr_data.save()
        except Exception as e:
            print("error ==>", e)
            error_message = e
            # global eg
            eg = e
            print("eg is:",eg)
            print("Error massage:",e)
            EchoConsumer.websocket_receive('event','event') 
        try:
            if 'flowsen'==components:
                # com=cl
                if device_id not in device_idlist:
                     repo_latestdata.objects.create(device_id=device_id,message_type=msg_type,flowsen=mydata1)
                else:
                    repo_latestobj = repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id, message_type=msg_type, flowsen=mydata1)

                    get_device_id=repo_latestdata.objects.all()
                    for did in get_device_id:
                        s=str(did.device_id)
                        if device_id == s:
                            flowsen=did.flowsen

                    klist = list(flowsen.keys())
                    print("klist is:",klist)
                    mydatakey = list(mydata1.keys())
                    print("mydatakey:",mydatakey)
                    for k,v in flowsen.items():
                         if k not in mydatakey:
                              olddata.update({k:v})
                              
                    mydata5=olddata.update(mydata1)    
                    print("old data is111:",olddata) # add/update keys in mydata1 to olddata
                    repo_latestobj = repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id, message_type=msg_type, flowsen=olddata)

                # repo_latestobj=repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id,message_type=msg_type,flowsen=mydata1)
                # repo_latestobj.save() 
                ds=treat_flowsen.objects.create(device_id=device_id,message_type=msg_type,fr1=fr1,fr2=fr2,ff1=ff1,ff2=ff2,year=dd[0],month=dd[1],day=dd[2],hour=dd[3],minit=dd[4],second=dd[5])
                ds.save()
                #hour
                yrdata=treat_flowsen.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id)
                count=0
                zerocount=-1
                sumd={}
                sums_fr1=0
                sums_fr2=0
                sums_ff1=0
                sums_ff2=0
                avgs_fr1 = 0
                avgs_fr2 = 0
                avgs_ff1 = 0
                avgs_ff2 = 0
                if yrdata:
                    for yr in yrdata:
                        yr_d_id=yr.device_id
                        if yr_d_id == device_id:
                            fr1=yr.fr1
                            fr2=yr.fr2
                            ff1=yr.ff1
                            ff2=yr.ff2
                            sums_fr1=sums_fr1+fr1
                            sums_fr2=sums_fr2+fr2
                            sums_ff1=sums_ff1+ff1
                            sums_ff2=sums_ff2+ff2
                            count=count+1
                    avgs_fr1=sums_fr1/count
                    avgs_fr2=sums_fr2/count
                    avgs_ff1=sums_ff1/count
                    avgs_ff2=sums_ff2/count
                hr=flowsen_repo_hourly.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id)
                if hr:
                    yr_data=flowsen_repo_hourly.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id).update(device_id=device_id,service='cnd_tds_cnd',fr1={'sum':sums_fr1,'avg':avgs_fr1,'count':count},fr2={'sum':sums_fr2,'avg':avgs_fr2,'count':count},ff1={'sum':sums_ff1,'avg':avgs_ff1,'count':count},ff2={'sum':sums_ff2,'avg':avgs_ff2,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                else:
                    yr_data=flowsen_repo_hourly.objects.create(device_id=device_id,service='flowsen',fr1={'sum':sums_fr1,'avg':avgs_fr1,'count':count},fr2={'sum':sums_fr2,'avg':avgs_fr2,'count':count},ff1={'sum':sums_ff1,'avg':avgs_ff1,'count':count},ff2={'sum':sums_ff2,'avg':avgs_ff2,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                    yr_data.save()

                #day
                yrdata=treat_flowsen.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id)
                count=0
                zerocount=-1
                sumd={}
                sums_fr1=0
                sums_fr2=0
                sums_ff1=0
                sums_ff2=0
                avgs_fr1 = 0
                avgs_fr2 = 0
                avgs_ff1 = 0
                avgs_ff2 = 0
                if yrdata:
                    for yr in yrdata:
                        yr_d_id=yr.device_id
                        if yr_d_id == device_id:
                            fr1=yr.fr1
                            fr2=yr.fr2
                            ff1=yr.ff1
                            ff2=yr.ff2
                            sums_fr1=sums_fr1+fr1
                            sums_fr2=sums_fr2+fr2
                            sums_ff1=sums_ff1+ff1
                            sums_ff2=sums_ff2+ff2
                            count=count+1
                    avgs_fr1=sums_fr1/count
                    avgs_fr2=sums_fr2/count
                    avgs_ff1=sums_ff1/count
                    avgs_ff2=sums_ff2/count
                hr=flowsen_repo_daily.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id)
                if hr:
                    yr_data=flowsen_repo_daily.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id).update(device_id=device_id,service='flowsen',fr1={'sum':sums_fr1,'avg':avgs_fr1,'count':count},fr2={'sum':sums_fr2,'avg':avgs_fr2,'count':count},ff1={'sum':sums_ff1,'avg':avgs_ff1,'count':count},ff2={'sum':sums_ff2,'avg':avgs_ff2,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                else:
                    yr_data=flowsen_repo_daily.objects.create(device_id=device_id,service='flowsen',fr1={'sum':sums_fr1,'avg':avgs_fr1,'count':count},fr2={'sum':sums_fr2,'avg':avgs_fr2,'count':count},ff1={'sum':sums_ff1,'avg':avgs_ff1,'count':count},ff2={'sum':sums_ff2,'avg':avgs_ff2,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                    yr_data.save()
                #month
                yrdata=treat_flowsen.objects.filter(year=dd[0],month=dd[1],device_id=device_id)
                count=0
                zerocount=-1
                sumd={}
                sums_fr1=0
                sums_fr2=0
                sums_ff1=0
                sums_ff2=0
                avgs_fr1 = 0
                avgs_fr2 = 0
                avgs_ff1 = 0
                avgs_ff2 = 0
                if yrdata:
                    for yr in yrdata:
                        yr_d_id=yr.device_id
                        if yr_d_id == device_id:
                            fr1=yr.fr1
                            fr2=yr.fr2
                            ff1=yr.ff1
                            ff2=yr.ff2
                            sums_fr1=sums_fr1+fr1
                            sums_fr2=sums_fr2+fr2
                            sums_ff1=sums_ff1+ff1
                            sums_ff2=sums_ff2+ff2
                            count=count+1
                    avgs_fr1=sums_fr1/count
                    avgs_fr2=sums_fr2/count
                    avgs_ff1=sums_ff1/count
                    avgs_ff2=sums_ff2/count
                hr=flowsen_repo_monthly.objects.filter(year=dd[0],month=dd[1],device_id=device_id)
                if hr:
                    yr_data=flowsen_repo_monthly.objects.filter(year=dd[0],month=dd[1],device_id=device_id).update(device_id=device_id,service='cnd_tds_cnd',fr1={'sum':sums_fr1,'avg':avgs_fr1,'count':count},fr2={'sum':sums_fr2,'avg':avgs_fr2,'count':count},ff1={'sum':sums_ff1,'avg':avgs_ff1,'count':count},ff2={'sum':sums_ff2,'avg':avgs_ff2,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                else:
                    yr_data=flowsen_repo_monthly.objects.create(device_id=device_id,service='flowsen',fr1={'sum':sums_fr1,'avg':avgs_fr1,'count':count},fr2={'sum':sums_fr2,'avg':avgs_fr2,'count':count},ff1={'sum':sums_ff1,'avg':avgs_ff1,'count':count},ff2={'sum':sums_ff2,'avg':avgs_ff2,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                    yr_data.save()

                #year
                yrdata=treat_flowsen.objects.filter(year=dd[0],device_id=device_id)
                count=0
                zerocount=-1
                sumd={}
                sums_fr1=0
                sums_fr2=0
                sums_ff1=0
                sums_ff2=0
                avgs_fr1 = 0
                avgs_fr2 = 0
                avgs_ff1 = 0
                avgs_ff2 = 0
                if yrdata:
                    for yr in yrdata:
                        yr_d_id=yr.device_id
                        if yr_d_id == device_id:
                            fr1=yr.fr1
                            fr2=yr.fr2
                            ff1=yr.ff1
                            ff2=yr.ff2
                            sums_fr1=sums_fr1+fr1
                            sums_fr2=sums_fr2+fr2
                            sums_ff1=sums_ff1+ff1
                            sums_ff2=sums_ff2+ff2
                            count=count+1
                    avgs_fr1=sums_fr1/count
                    avgs_fr2=sums_fr2/count
                    avgs_ff1=sums_ff1/count
                    avgs_ff2=sums_ff2/count
                hr=flowsen_repo_yearly.objects.filter(year=dd[0],device_id=device_id)
                if hr:
                    yr_data=flowsen_repo_yearly.objects.filter(year=dd[0],device_id=device_id).update(device_id=device_id,service='flowsen',fr1={'sum':sums_fr1,'avg':avgs_fr1,'count':count},fr2={'sum':sums_fr2,'avg':avgs_fr2,'count':count},ff1={'sum':sums_ff1,'avg':avgs_ff1,'count':count},ff2={'sum':sums_ff2,'avg':avgs_ff2,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                else:
                    yr_data=flowsen_repo_yearly.objects.create(device_id=device_id,service='flowsen',fr1={'sum':sums_fr1,'avg':avgs_fr1,'count':count},fr2={'sum':sums_fr2,'avg':avgs_fr2,'count':count},ff1={'sum':sums_ff1,'avg':avgs_ff1,'count':count},ff2={'sum':sums_ff2,'avg':avgs_ff2,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                    yr_data.save()

                # yrdata=treat_flowsen.objects.filter(year=dd[0],device_id=device_id)
                # count=0
                # sums=0
                # avgs = 0
                # if yrdata:
                #     for yr in yrdata:
                #         yr_d_id=yr.device_id
                #         if yr_d_id == device_id:
                #             fr1=yr.fr1
                #             print("fr1 is:",fr1)
                #             sums=sums+fr1
                #             count=count+1
                #             print("sums is:",sums)
                #             print("count is:",count)
                #     avgs=sums/count
                # hr=repo_yearly.objects.filter(service='flowsen_fr1',year=dd[0],device_id=device_id)
                # if hr:
                #     yr_data=repo_yearly.objects.filter(device_id=device_id).update(device_id=device_id,service='flowsen_fr1',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
                # else:
                #     yr_data=repo_yearly.objects.create(device_id=device_id,service='flowsen_fr1',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
                #     yr_data.save()
                # ds=treat_flowsen.objects.create(device_id=device_id,message_type=msg_type,fr1=fr1,fr2=fr2,ff1=ff1,ff2=ff2,year=dd[0],month=dd[1],day=dd[2],hour=dd[3],minit=dd[4],second=dd[5])
                # ds.save()  
                # ds=treat_flowsen.objects.create(device_id=device_id,message_type=msg_type,fr1=fr1,fr2=fr2,ff1=ff1,ff2=ff2)
                # ds.save()
                # yrdata=treat_flowsen.objects.filter(year=dd[0],device_id=device_id)
                # count=0
                # sums=0
                # avgs = 0
                # if yrdata:
                #     for yr in yrdata:
                #         yr_d_id=yr.device_id
                #         if yr_d_id == device_id:
                #             fr2=yr.fr2
                #             print("fr2 is:",fr2)
                #             sums=sums+fr2
                #             count=count+1
                #             print("sums is:",sums)
                #             print("count is:",count)
                #     avgs=sums/count
                # hr=repo_yearly.objects.filter(service='flowsen_fr2',year=dd[0],device_id=device_id)
                # if hr:
                #     yr_data=repo_yearly.objects.filter(device_id=device_id).update(device_id=device_id,service='flowsen_fr2',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
                # else:
                #     yr_data=repo_yearly.objects.create(device_id=device_id,service='flowsen_fr2',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
                #     yr_data.save()
           
            #     # month
            #     yrdata=treat_flowsen.objects.filter(year=dd[0],month=dd[1],device_id=device_id)
            #     count=0
            #     sums=0
            #     avgs = 0
            #     if yrdata:
            #         for yr in yrdata:
            #             yr_d_id=yr.device_id
            #             if yr_d_id == device_id:
            #                 fr1=yr.fr1
            #                 print("fr1 is:",fr1)
            #                 sums=sums+fr1
            #                 count=count+1
            #                 print("sums is:",sums)
            #                 print("count is:",count)
            #         avgs=sums/count
            #     hr=repo_monthly.objects.filter(service='flowsen_fr1',year=dd[0],month=dd[1],device_id=device_id)
            #     if hr:
            #         yr_data=repo_monthly.objects.filter(year=dd[0],month=dd[1],device_id=device_id).update(device_id=device_id,service='flowsen_fr1',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
            #     else:
            #         yr_data=repo_monthly.objects.create(device_id=device_id,service='flowsen_fr1',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
            #         yr_data.save()
            #     yrdata=treat_flowsen.objects.filter(year=dd[0],month=dd[1],device_id=device_id)
            #     count=0
            #     sums=0
            #     avgs = 0
            #     if yrdata:
            #         for yr in yrdata:
            #             yr_d_id=yr.device_id
            #             if yr_d_id == device_id:
            #                 fr2=yr.fr2
            #                 print("fr2 is:",fr2)
            #                 sums=sums+fr2
            #                 count=count+1
            #                 print("sums is:",sums)
            #                 print("count is:",count)
            #         avgs=sums/count
            #     hr=repo_monthly.objects.filter(service='flowsen_fr2',year=dd[0],month=dd[1],device_id=device_id)
            #     if hr:
            #         yr_data=repo_monthly.objects.filter(year=dd[0],month=dd[1],device_id=device_id).update(device_id=device_id,service='flowsen_fr2',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
            #     else:
            #         yr_data=repo_monthly.objects.create(device_id=device_id,service='flowsen_fr2',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
            #         yr_data.save()
                
            #   # day
            #     yrdata=treat_flowsen.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id)
            #     count=0
            #     sums=0
            #     avgs = 0
            #     if yrdata:
            #         for yr in yrdata:
            #             yr_d_id=yr.device_id
            #             if yr_d_id == device_id:
            #                 fr1=yr.fr1
            #                 print("fr1 is:",fr1)
            #                 sums=sums+fr1
            #                 count=count+1
            #                 print("sums is:",sums)
            #                 print("count is:",count)
            #         avgs=sums/count
            #     hr=repo_daily.objects.filter(service='flowsen_fr1',year=dd[0],month=dd[1],day=dd[2],device_id=device_id)
            #     if hr:
            #         yr_data=repo_daily.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id).update(device_id=device_id,service='flowsen_fr1',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0],day=dd[2])
            #     else:
            #         yr_data=repo_daily.objects.create(device_id=device_id,service='flowsen_fr1',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0],day=dd[2])
            #         yr_data.save()
            #     yrdata=treat_flowsen.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id)
            #     count=0
            #     sums=0
            #     avgs = 0
            #     if yrdata:
            #         for yr in yrdata:
            #             yr_d_id=yr.device_id
            #             if yr_d_id == device_id:
            #                 fr2=yr.fr2
            #                 print("fr2 is:",fr2)
            #                 sums=sums+fr2
            #                 count=count+1
            #                 print("sums is:",sums)
            #                 print("count is:",count)
            #         avgs=sums/count
            #     hr=repo_daily.objects.filter(service='flowsen_fr2',year=dd[0],month=dd[1],day=dd[2],device_id=device_id)
            #     if hr:
            #         yr_data=repo_daily.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id).update(device_id=device_id,service='flowsen_fr2',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0],day=dd[2])
            #     else:
            #         yr_data=repo_daily.objects.create(device_id=device_id,service='flowsen_fr2',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0],day=dd[2])
            #         yr_data.save()
            #     # hour
            #     yrdata=treat_flowsen.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id)
            #     count=0
            #     sums=0
            #     avgs = 0
            #     if yrdata:
            #         for yr in yrdata:
            #             yr_d_id=yr.device_id
            #             if yr_d_id == device_id:
            #                 fr1=yr.fr1
            #                 print("fr1 is:",fr1)
            #                 sums=sums+fr1
            #                 count=count+1
            #                 print("sums is:",sums)
            #                 print("count is:",count)
            #         avgs=sums/count
            #     hr=repo_hourly.objects.filter(service='flowsen_fr1',year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id)
            #     if hr:
            #         yr_data=repo_hourly.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id).update(device_id=device_id,service='flowsen_fr1',sum=sums,count=count,avg=avgs,hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
            #     else:
            #         yr_data=repo_hourly.objects.create(device_id=device_id,service='flowsen_fr1',sum=sums,count=count,avg=avgs,hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
            #         yr_data.save()

            #     yrdata=treat_flowsen.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id)
            #     count=0
            #     sums=0
            #     avgs = 0
            #     if yrdata:
            #         for yr in yrdata:
            #             yr_d_id=yr.device_id
            #             if yr_d_id == device_id:
            #                 fr2=yr.fr2
            #                 print("fr2 is:",fr2)
            #                 sums=sums+fr2
            #                 count=count+1
            #                 print("sums is:",sums)
            #                 print("count is:",count)
            #         avgs=sums/count
            #     hr=repo_hourly.objects.filter(service='flowsen_fr2',year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id)
            #     if hr:
            #         yr_data=repo_hourly.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id).update(device_id=device_id,service='flowsen_fr2',sum=sums,count=count,avg=avgs,hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
            #     else:
            #         yr_data=repo_hourly.objects.create(device_id=device_id,service='flowsen_fr2',sum=sums,count=count,avg=avgs,hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
            #         yr_data.save()
        except Exception as e:
            print("error ==>", e)
            error_message = e
            # global eg
            eg = e
            print("eg is:",eg)
            print("Error massage:",e)
            EchoConsumer.websocket_receive('event','event')     
        try:
            if 'ampv1'==components:
                # com=cl
                if device_id not in device_idlist:
                     repo_latestdata.objects.create(device_id=device_id,message_type=msg_type,ampv1=mydata1)
                else:
                    repo_latestobj = repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id, message_type=msg_type, ampv1=mydata1)

                    get_device_id=repo_latestdata.objects.all()
                    for did in get_device_id:
                        s=str(did.device_id)
                        if device_id == s:
                            ampv1=did.ampv1
                    klist = list(ampv1.keys())
                    print("klist is:",klist)
                    mydatakey = list(mydata1.keys())
                    print("mydatakey:",mydatakey)
                    for k,v in ampv1.items():
                         if k not in mydatakey:
                              olddata.update({k:v})
                              
                    mydata5=olddata.update(mydata1)    
                    print("old data is:",olddata) # add/update keys in mydata1 to olddata
                    repo_latestobj = repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id, message_type=msg_type, ampv1=olddata)

                ds=treat_ampv1.objects.create(device_id=device_id,message_type=msg_type,pos=pos,rmt=rmt,cct=cct,srt=srt,bkt=bkt,rst=rst,mot=mot,stp=stp,op1=op1,op2=op2,op3=op3,ip1=ip1,ip2=ip2,ip3=ip3,psi=psi,year=dd[0],month=dd[1],day=dd[2],hour=dd[3],minit=dd[4],second=dd[5])
                ds.save()
                #hour
                yrdata=treat_ampv1.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id)
                count=0
                zerocount=-1
                sumd={}
                sums_rmt=0
                sums_cct=0
                sums_srt=0
                sums_bkt=0
                sums_rst=0
                sums_mot=0
                avgs_rmt = 0
                avgs_cct = 0
                avgs_srt = 0
                avgs_bkt = 0
                avgs_rst = 0
                avgs_mot = 0
                # avgs_bktsums_bkt = 0
                if yrdata:
                    for yr in yrdata:
                        yr_d_id=yr.device_id
                        if yr_d_id == device_id:
                            rmt=yr.rmt
                            cct=yr.cct
                            srt=yr.srt
                            bkt=yr.bkt
                            rst=yr.rst
                            mot=yr.mot
                            sums_rmt=sums_rmt+rmt
                            sums_cct=sums_cct+cct
                            sums_srt=sums_srt+srt
                            sums_bkt=sums_bkt+bkt
                            sums_rst=sums_rst+rst
                            sums_mot=sums_mot+mot
                            count=count+1
                    avgs_rmt=sums_rmt/count
                    avgs_cct=sums_cct/count
                    avgs_srt=sums_srt/count
                    avgs_bkt=sums_bkt/count
                    avgs_rst=sums_rst/count
                    avgs_mot=sums_mot/count
                hr=ampv1_repo_hourly.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id)
                if hr:
                    yr_data=ampv1_repo_hourly.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id).update(device_id=device_id,service='ampv1',rmt={'sum':sums_rmt,'avg':avgs_rmt,'count':count},cct={'sum':sums_cct,'avg':avgs_cct,'count':count},srt={'sum':sums_srt,'avg':avgs_srt,'count':count},bkt={'sum':sums_bkt,'avg':avgs_bkt,'count':count},rst={'sum':sums_rst,'avg':avgs_rst,'count':count},mot={'sum':sums_mot,'avg':avgs_mot,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                else:
                    yr_data=ampv1_repo_hourly.objects.create(device_id=device_id,service='ampv1',rmt={'sum':sums_rmt,'avg':avgs_rmt,'count':count},cct={'sum':sums_cct,'avg':avgs_cct,'count':count},srt={'sum':sums_srt,'avg':avgs_srt,'count':count},bkt={'sum':sums_bkt,'avg':avgs_bkt,'count':count},rst={'sum':sums_rst,'avg':avgs_rst,'count':count},mot={'sum':sums_mot,'avg':avgs_mot,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                    yr_data.save()
                #daily
                yrdata=treat_ampv1.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id)
                count=0
                zerocount=-1
                sumd={}
                sums_rmt=0
                sums_cct=0
                sums_srt=0
                sums_bkt=0
                sums_rst=0
                sums_mot=0
                avgs_rmt = 0
                avgs_cct = 0
                avgs_srt = 0
                avgs_bkt = 0
                avgs_rst = 0
                avgs_mot = 0
                # avgs_bktsums_bkt = 0
                if yrdata:
                    for yr in yrdata:
                        yr_d_id=yr.device_id
                        if yr_d_id == device_id:
                            rmt=yr.rmt
                            cct=yr.cct
                            srt=yr.srt
                            bkt=yr.bkt
                            rst=yr.rst
                            mot=yr.mot
                            sums_rmt=sums_rmt+rmt
                            sums_cct=sums_cct+cct
                            sums_srt=sums_srt+srt
                            sums_bkt=sums_bkt+bkt
                            sums_rst=sums_rst+rst
                            sums_mot=sums_mot+mot
                            count=count+1
                    avgs_rmt=sums_rmt/count
                    avgs_cct=sums_cct/count
                    avgs_srt=sums_srt/count
                    avgs_bkt=sums_bkt/count
                    avgs_rst=sums_rst/count
                    avgs_mot=sums_mot/count
                hr=ampv1_repo_daily.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id)
                if hr:
                    yr_data=ampv1_repo_daily.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id).update(device_id=device_id,service='ampv1',rmt={'sum':sums_rmt,'avg':avgs_rmt,'count':count},cct={'sum':sums_cct,'avg':avgs_cct,'count':count},srt={'sum':sums_srt,'avg':avgs_srt,'count':count},bkt={'sum':sums_bkt,'avg':avgs_bkt,'count':count},rst={'sum':sums_rst,'avg':avgs_rst,'count':count},mot={'sum':sums_mot,'avg':avgs_mot,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                else:
                    yr_data=ampv1_repo_daily.objects.create(device_id=device_id,service='ampv1',rmt={'sum':sums_rmt,'avg':avgs_rmt,'count':count},cct={'sum':sums_cct,'avg':avgs_cct,'count':count},srt={'sum':sums_srt,'avg':avgs_srt,'count':count},bkt={'sum':sums_bkt,'avg':avgs_bkt,'count':count},rst={'sum':sums_rst,'avg':avgs_rst,'count':count},mot={'sum':sums_mot,'avg':avgs_mot,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                    yr_data.save()
                #month
                yrdata=treat_ampv1.objects.filter(year=dd[0],month=dd[1],device_id=device_id)
                count=0
                zerocount=-1
                sumd={}
                sums_rmt=0
                sums_cct=0
                sums_srt=0
                sums_bkt=0
                sums_rst=0
                sums_mot=0
                avgs_rmt = 0
                avgs_cct = 0
                avgs_srt = 0
                avgs_bkt = 0
                avgs_rst = 0
                avgs_mot = 0
                # avgs_bktsums_bkt = 0
                if yrdata:
                    for yr in yrdata:
                        yr_d_id=yr.device_id
                        if yr_d_id == device_id:
                            rmt=yr.rmt
                            cct=yr.cct
                            srt=yr.srt
                            bkt=yr.bkt
                            rst=yr.rst
                            mot=yr.mot
                            sums_rmt=sums_rmt+rmt
                            sums_cct=sums_cct+cct
                            sums_srt=sums_srt+srt
                            sums_bkt=sums_bkt+bkt
                            sums_rst=sums_rst+rst
                            sums_mot=sums_mot+mot
                            count=count+1
                    avgs_rmt=sums_rmt/count
                    avgs_cct=sums_cct/count
                    avgs_srt=sums_srt/count
                    avgs_bkt=sums_bkt/count
                    avgs_rst=sums_rst/count
                    avgs_mot=sums_mot/count
                hr=ampv1_repo_monthly.objects.filter(year=dd[0],month=dd[1],device_id=device_id)
                if hr:
                    yr_data=ampv1_repo_monthly.objects.filter(year=dd[0],month=dd[1],device_id=device_id).update(device_id=device_id,service='ampv1',rmt={'sum':sums_rmt,'avg':avgs_rmt,'count':count},cct={'sum':sums_cct,'avg':avgs_cct,'count':count},srt={'sum':sums_srt,'avg':avgs_srt,'count':count},bkt={'sum':sums_bkt,'avg':avgs_bkt,'count':count},rst={'sum':sums_rst,'avg':avgs_rst,'count':count},mot={'sum':sums_mot,'avg':avgs_mot,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                else:
                    yr_data=ampv1_repo_monthly.objects.create(device_id=device_id,service='ampv1',rmt={'sum':sums_rmt,'avg':avgs_rmt,'count':count},cct={'sum':sums_cct,'avg':avgs_cct,'count':count},srt={'sum':sums_srt,'avg':avgs_srt,'count':count},bkt={'sum':sums_bkt,'avg':avgs_bkt,'count':count},rst={'sum':sums_rst,'avg':avgs_rst,'count':count},mot={'sum':sums_mot,'avg':avgs_mot,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                    yr_data.save()
                #year
                yrdata=treat_ampv1.objects.filter(year=dd[0],device_id=device_id)
                count=0
                zerocount=-1
                sumd={}
                sums_rmt=0
                sums_cct=0
                sums_srt=0
                sums_bkt=0
                sums_rst=0
                sums_mot=0
                avgs_rmt = 0
                avgs_cct = 0
                avgs_srt = 0
                avgs_bkt = 0
                avgs_rst = 0
                avgs_mot = 0
                # avgs_bktsums_bkt = 0
                if yrdata:
                    for yr in yrdata:
                        yr_d_id=yr.device_id
                        if yr_d_id == device_id:
                            rmt=yr.rmt
                            cct=yr.cct
                            srt=yr.srt
                            bkt=yr.bkt
                            rst=yr.rst
                            mot=yr.mot
                            sums_rmt=sums_rmt+rmt
                            sums_cct=sums_cct+cct
                            sums_srt=sums_srt+srt
                            sums_bkt=sums_bkt+bkt
                            sums_rst=sums_rst+rst
                            sums_mot=sums_mot+mot
                            count=count+1
                    avgs_rmt=sums_rmt/count
                    avgs_cct=sums_cct/count
                    avgs_srt=sums_srt/count
                    avgs_bkt=sums_bkt/count
                    avgs_rst=sums_rst/count
                    avgs_mot=sums_mot/count
                hr=ampv1_repo_yearly.objects.filter(year=dd[0],device_id=device_id)
                if hr:
                    yr_data=ampv1_repo_yearly.objects.filter(year=dd[0],device_id=device_id).update(device_id=device_id,service='ampv1',rmt={'sum':sums_rmt,'avg':avgs_rmt,'count':count},cct={'sum':sums_cct,'avg':avgs_cct,'count':count},srt={'sum':sums_srt,'avg':avgs_srt,'count':count},bkt={'sum':sums_bkt,'avg':avgs_bkt,'count':count},rst={'sum':sums_rst,'avg':avgs_rst,'count':count},mot={'sum':sums_mot,'avg':avgs_mot,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                else:
                    yr_data=ampv1_repo_yearly.objects.create(device_id=device_id,service='ampv1',rmt={'sum':sums_rmt,'avg':avgs_rmt,'count':count},cct={'sum':sums_cct,'avg':avgs_cct,'count':count},srt={'sum':sums_srt,'avg':avgs_srt,'count':count},bkt={'sum':sums_bkt,'avg':avgs_bkt,'count':count},rst={'sum':sums_rst,'avg':avgs_rst,'count':count},mot={'sum':sums_mot,'avg':avgs_mot,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                    yr_data.save()

            #     yrdata=treat_ampv1.objects.filter(year=dd[0],device_id=device_id)
            #     count=0
            #     sums=0
            #     avgs = 0
            #     if yrdata:
            #         for yr in yrdata:
            #             yr_d_id=yr.device_id
            #             if yr_d_id == device_id:
            #                 rmt=yr.rmt
            #                 print("rmt is:",rmt)
            #                 sums=sums+rmt
            #                 count=count+1
            #                 print("sums is:",sums)
            #                 print("count is:",count)
            #         avgs=sums/count
            #     hr=repo_yearly.objects.filter(service='ampv1_rmt',year=dd[0],device_id=device_id)
            #     if hr:
            #         yr_data=repo_yearly.objects.filter(device_id=device_id).update(device_id=device_id,service='ampv1_rmt',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
            #     else:
            #         yr_data=repo_yearly.objects.create(device_id=device_id,service='ampv1_rmt',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
            #         yr_data.save()
            #     yrdata=treat_ampv1.objects.filter(year=dd[0],device_id=device_id)    
            #     count=0
            #     sums=0
            #     avgs = 0
            #     if yrdata:
            #         for yr in yrdata:
            #             yr_d_id=yr.device_id
            #             if yr_d_id == device_id:
            #                 cct=yr.cct
            #                 print("cct is:",cct)
            #                 sums=sums+cct
            #                 count=count+1
            #                 print("sums is:",sums)
            #                 print("count is:",count)
            #         avgs=sums/count
            #     hr=repo_yearly.objects.filter(service='ampv1_cct',year=dd[0],device_id=device_id)
            #     if hr:
            #         yr_data=repo_yearly.objects.filter(device_id=device_id).update(device_id=device_id,service='ampv1_cct',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
            #     else:
            #         yr_data=repo_yearly.objects.create(device_id=device_id,service='ampv1_cct',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
            #         yr_data.save()
            #     yrdata=treat_ampv1.objects.filter(year=dd[0],month=dd[1],device_id=device_id)
            #     count=0
            #     sums=0
            #     avgs = 0
            #     if yrdata:
            #         for yr in yrdata:
            #             yr_d_id=yr.device_id
            #             if yr_d_id == device_id:
            #                 rmt=yr.rmt
            #                 print("rmt is:",rmt)
            #                 sums=sums+rmt
            #                 count=count+1
            #                 print("sums is:",sums)
            #                 print("count is:",count)
            #         avgs=sums/count
            #     hr=repo_monthly.objects.filter(service='ampv1_rmt',year=dd[0],month=dd[1],device_id=device_id)
            #     if hr:
            #         yr_data=repo_monthly.objects.filter(year=dd[0],month=dd[1],device_id=device_id).update(device_id=device_id,service='ampv1_rmt',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
            #     else:
            #         yr_data=repo_monthly.objects.create(device_id=device_id,service='ampv1_rmt',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
            #         yr_data.save()
            #     yrdata=treat_ampv1.objects.filter(year=dd[0],month=dd[1],device_id=device_id)        
            #     count=0
            #     sums=0
            #     avgs = 0
            #     if yrdata:
            #         for yr in yrdata:
            #             yr_d_id=yr.device_id
            #             if yr_d_id == device_id:
            #                 cct=yr.cct
            #                 print("cct is:",cct)
            #                 sums=sums+cct
            #                 count=count+1
            #                 print("sums is:",sums)
            #                 print("count is:",count)
            #         avgs=sums/count
            #     hr=repo_monthly.objects.filter(service='ampv1_cct',year=dd[0],month=dd[1],device_id=device_id)
            #     if hr:
            #         yr_data=repo_monthly.objects.filter(year=dd[0],month=dd[1],device_id=device_id).update(device_id=device_id,service='ampv1_cct',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
            #     else:
            #         yr_data=repo_monthly.objects.create(device_id=device_id,service='ampv1_cct',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
            #         yr_data.save()
            #   # day
            #     yrdata=treat_ampv1.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id)
            #     count=0
            #     sums=0
            #     avgs = 0
            #     if yrdata:
            #         for yr in yrdata:
            #             yr_d_id=yr.device_id
            #             if yr_d_id == device_id:
            #                 rmt=yr.rmt
            #                 print("rmt is:",rmt)
            #                 sums=sums+rmt
            #                 count=count+1
            #                 print("sums is:",sums)
            #                 print("count is:",count)
            #         avgs=sums/count
            #     hr=repo_daily.objects.filter(service='ampv1_rmt',year=dd[0],month=dd[1],day=dd[2],device_id=device_id)
            #     if hr:
            #         yr_data=repo_daily.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id).update(device_id=device_id,service='ampv1_rmt',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0],day=dd[2])
            #     else:
            #         yr_data=repo_daily.objects.create(device_id=device_id,service='ampv1_rmt',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0],day=dd[2])
            #         yr_data.save()
            #     yrdata=treat_ampv1.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id)        
            #     count=0
            #     sums=0
            #     avgs = 0
            #     if yrdata:
            #         for yr in yrdata:
            #             yr_d_id=yr.device_id
            #             if yr_d_id == device_id:
            #                 cct=yr.cct
            #                 print("cct is:",cct)
            #                 sums=sums+cct
            #                 count=count+1
            #                 print("sums is:",sums)
            #                 print("count is:",count)
            #         avgs=sums/count
            #     hr=repo_daily.objects.filter(service='ampv1_cct',year=dd[0],month=dd[1],day=dd[2],device_id=device_id)
            #     if hr:
            #         yr_data=repo_daily.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id).update(device_id=device_id,service='ampv1_cct',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0],day=dd[2])
            #     else:
            #         yr_data=repo_daily.objects.create(device_id=device_id,service='ampv1_cct',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0],day=dd[2])
            #         yr_data.save()
            #  # hour
            #     yrdata=treat_ampv1.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id)
            #     count=0
            #     sums=0
            #     avgs = 0
            #     if yrdata:
            #         for yr in yrdata:
            #             yr_d_id=yr.device_id
            #             if yr_d_id == device_id:
            #                 rmt=yr.rmt
            #                 print("rmt is:",rmt)
            #                 sums=sums+rmt
            #                 count=count+1
            #                 print("sums is:",sums)
            #                 print("count is:",count)
            #         avgs=sums/count
            #     hr=repo_hourly.objects.filter(service='ampv1_rmt',year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id)
            #     if hr:
            #         yr_data=repo_hourly.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id).update(device_id=device_id,service='ampv1_rmt',sum=sums,count=count,avg=avgs,hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
            #     else:
            #         yr_data=repo_hourly.objects.create(device_id=device_id,service='ampv1_rmt',sum=sums,count=count,avg=avgs,hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
            #         yr_data.save()
            #     yrdata=treat_ampv1.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id)        
            #     count=0
            #     sums=0
            #     avgs = 0
            #     if yrdata:
            #         for yr in yrdata:
            #             yr_d_id=yr.device_id
            #             if yr_d_id == device_id:
            #                 cct=yr.cct
            #                 print("cct is:",cct)
            #                 sums=sums+cct
            #                 count=count+1
            #                 print("sums is:",sums)
            #                 print("count is:",count)
            #         avgs=sums/count
            #     hr=repo_hourly.objects.filter(service='ampv1_cct',year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id)
            #     if hr:
            #         yr_data=repo_hourly.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id).update(device_id=device_id,service='ampv1_cct',sum=sums,count=count,avg=avgs,hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
            #     else:
            #         yr_data=repo_hourly.objects.create(device_id=device_id,service='ampv1_cct',sum=sums,count=count,avg=avgs,hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
            #         yr_data.save()
        except Exception as e:
            print("error ==>", e)
            error_message = e
            # global eg
            eg = e
            print("eg is:",eg)
            print("Error massage:",e)
            EchoConsumer.websocket_receive('event','event') 
        try:
            if 'ampv2'==components:
                # com=cl

                if device_id not in device_idlist:
                     repo_latestdata.objects.create(device_id=device_id,message_type=msg_type,ampv2=mydata1)
                else:
                    repo_latestobj = repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id, message_type=msg_type, ampv2=mydata1)

                    get_device_id=repo_latestdata.objects.all()
                    for did in get_device_id:
                        s=str(did.device_id)
                        if device_id == s:
                            ampv2=did.ampv2
                    klist = list(ampv2.keys())
                    print("klist is:",klist)
                    mydatakey = list(mydata1.keys())
                    print("mydatakey:",mydatakey)
                    for k,v in ampv2.items():
                         if k not in mydatakey:
                              olddata.update({k:v})
                              
                    mydata5=olddata.update(mydata1)    
                    print("old data is:",olddata) # add/update keys in mydata1 to olddata
                    repo_latestobj = repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id, message_type=msg_type, ampv2=olddata)

                # repo_latestobj=repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id,message_type=msg_type,ampv2=mydata1)
                # repo_latestobj.save()
                ds=treat_ampv2.objects.create(device_id=device_id,message_type=msg_type,pos=pos,rmt=rmt,cct=cct,srt=srt,bkt=bkt,rst=rst,mot=mot,stp=stp,op1=op1,op2=op2,op3=op3,ip1=ip1,ip2=ip2,ip3=ip3,psi=psi,year=dd[0],month=dd[1],day=dd[2],hour=dd[3],minit=dd[4],second=dd[5])
                ds.save()
                #hour
                yrdata=treat_ampv2.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id)
                count=0
                zerocount=-1
                sumd={}
                sums_rmt=0
                sums_cct=0
                sums_srt=0
                sums_bkt=0
                sums_rst=0
                sums_mot=0
                avgs_rmt = 0
                avgs_cct = 0
                avgs_srt = 0
                avgs_bkt = 0
                avgs_rst = 0
                avgs_mot = 0
                # avgs_bktsums_bkt = 0
                if yrdata:
                    for yr in yrdata:
                        yr_d_id=yr.device_id
                        if yr_d_id == device_id:
                            rmt=yr.rmt
                            cct=yr.cct
                            srt=yr.srt
                            bkt=yr.bkt
                            rst=yr.rst
                            mot=yr.mot
                            sums_rmt=sums_rmt+rmt
                            sums_cct=sums_cct+cct
                            sums_srt=sums_srt+srt
                            sums_bkt=sums_bkt+bkt
                            sums_rst=sums_rst+rst
                            sums_mot=sums_mot+mot
                            count=count+1
                    avgs_rmt=sums_rmt/count
                    avgs_cct=sums_cct/count
                    avgs_srt=sums_srt/count
                    avgs_bkt=sums_bkt/count
                    avgs_rst=sums_rst/count
                    avgs_mot=sums_mot/count
                hr=ampv2_repo_hourly.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id)
                if hr:
                    yr_data=ampv2_repo_hourly.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id).update(device_id=device_id,service='ampv2',rmt={'sum':sums_rmt,'avg':avgs_rmt,'count':count},cct={'sum':sums_cct,'avg':avgs_cct,'count':count},srt={'sum':sums_srt,'avg':avgs_srt,'count':count},bkt={'sum':sums_bkt,'avg':avgs_bkt,'count':count},rst={'sum':sums_rst,'avg':avgs_rst,'count':count},mot={'sum':sums_mot,'avg':avgs_mot,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                else:
                    yr_data=ampv2_repo_hourly.objects.create(device_id=device_id,service='ampv2',rmt={'sum':sums_rmt,'avg':avgs_rmt,'count':count},cct={'sum':sums_cct,'avg':avgs_cct,'count':count},srt={'sum':sums_srt,'avg':avgs_srt,'count':count},bkt={'sum':sums_bkt,'avg':avgs_bkt,'count':count},rst={'sum':sums_rst,'avg':avgs_rst,'count':count},mot={'sum':sums_mot,'avg':avgs_mot,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                    yr_data.save()
                #daily
                yrdata=treat_ampv2.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id)
                count=0
                zerocount=-1
                sumd={}
                sums_rmt=0
                sums_cct=0
                sums_srt=0
                sums_bkt=0
                sums_rst=0
                sums_mot=0
                avgs_rmt = 0
                avgs_cct = 0
                avgs_srt = 0
                avgs_bkt = 0
                avgs_rst = 0
                avgs_mot = 0
                # avgs_bktsums_bkt = 0
                if yrdata:
                    for yr in yrdata:
                        yr_d_id=yr.device_id
                        if yr_d_id == device_id:
                            rmt=yr.rmt
                            cct=yr.cct
                            srt=yr.srt
                            bkt=yr.bkt
                            rst=yr.rst
                            mot=yr.mot
                            sums_rmt=sums_rmt+rmt
                            sums_cct=sums_cct+cct
                            sums_srt=sums_srt+srt
                            sums_bkt=sums_bkt+bkt
                            sums_rst=sums_rst+rst
                            sums_mot=sums_mot+mot
                            count=count+1
                    avgs_rmt=sums_rmt/count
                    avgs_cct=sums_cct/count
                    avgs_srt=sums_srt/count
                    avgs_bkt=sums_bkt/count
                    avgs_rst=sums_rst/count
                    avgs_mot=sums_mot/count
                hr=ampv2_repo_daily.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id)
                if hr:
                    yr_data=ampv2_repo_daily.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id).update(device_id=device_id,service='ampv2',rmt={'sum':sums_rmt,'avg':avgs_rmt,'count':count},cct={'sum':sums_cct,'avg':avgs_cct,'count':count},srt={'sum':sums_srt,'avg':avgs_srt,'count':count},bkt={'sum':sums_bkt,'avg':avgs_bkt,'count':count},rst={'sum':sums_rst,'avg':avgs_rst,'count':count},mot={'sum':sums_mot,'avg':avgs_mot,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                else:
                    yr_data=ampv2_repo_daily.objects.create(device_id=device_id,service='ampv2',rmt={'sum':sums_rmt,'avg':avgs_rmt,'count':count},cct={'sum':sums_cct,'avg':avgs_cct,'count':count},srt={'sum':sums_srt,'avg':avgs_srt,'count':count},bkt={'sum':sums_bkt,'avg':avgs_bkt,'count':count},rst={'sum':sums_rst,'avg':avgs_rst,'count':count},mot={'sum':sums_mot,'avg':avgs_mot,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                    yr_data.save()
                #month
                yrdata=treat_ampv2.objects.filter(year=dd[0],month=dd[1],device_id=device_id)
                count=0
                zerocount=-1
                sumd={}
                sums_rmt=0
                sums_cct=0
                sums_srt=0
                sums_bkt=0
                sums_rst=0
                sums_mot=0
                avgs_rmt = 0
                avgs_cct = 0
                avgs_srt = 0
                avgs_bkt = 0
                avgs_rst = 0
                avgs_mot = 0
                # avgs_bktsums_bkt = 0
                if yrdata:
                    for yr in yrdata:
                        yr_d_id=yr.device_id
                        if yr_d_id == device_id:
                            rmt=yr.rmt
                            cct=yr.cct
                            srt=yr.srt
                            bkt=yr.bkt
                            rst=yr.rst
                            mot=yr.mot
                            sums_rmt=sums_rmt+rmt
                            sums_cct=sums_cct+cct
                            sums_srt=sums_srt+srt
                            sums_bkt=sums_bkt+bkt
                            sums_rst=sums_rst+rst
                            sums_mot=sums_mot+mot
                            count=count+1
                    avgs_rmt=sums_rmt/count
                    avgs_cct=sums_cct/count
                    avgs_srt=sums_srt/count
                    avgs_bkt=sums_bkt/count
                    avgs_rst=sums_rst/count
                    avgs_mot=sums_mot/count
                hr=ampv2_repo_monthly.objects.filter(year=dd[0],month=dd[1],device_id=device_id)
                if hr:
                    yr_data=ampv2_repo_monthly.objects.filter(year=dd[0],month=dd[1],device_id=device_id).update(device_id=device_id,service='ampv2',rmt={'sum':sums_rmt,'avg':avgs_rmt,'count':count},cct={'sum':sums_cct,'avg':avgs_cct,'count':count},srt={'sum':sums_srt,'avg':avgs_srt,'count':count},bkt={'sum':sums_bkt,'avg':avgs_bkt,'count':count},rst={'sum':sums_rst,'avg':avgs_rst,'count':count},mot={'sum':sums_mot,'avg':avgs_mot,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                else:
                    yr_data=ampv2_repo_monthly.objects.create(device_id=device_id,service='ampv2',rmt={'sum':sums_rmt,'avg':avgs_rmt,'count':count},cct={'sum':sums_cct,'avg':avgs_cct,'count':count},srt={'sum':sums_srt,'avg':avgs_srt,'count':count},bkt={'sum':sums_bkt,'avg':avgs_bkt,'count':count},rst={'sum':sums_rst,'avg':avgs_rst,'count':count},mot={'sum':sums_mot,'avg':avgs_mot,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                    yr_data.save()
                #year
                yrdata=treat_ampv2.objects.filter(year=dd[0],device_id=device_id)
                count=0
                zerocount=-1
                sumd={}
                sums_rmt=0
                sums_cct=0
                sums_srt=0
                sums_bkt=0
                sums_rst=0
                sums_mot=0
                avgs_rmt = 0
                avgs_cct = 0
                avgs_srt = 0
                avgs_bkt = 0
                avgs_rst = 0
                avgs_mot = 0
                # avgs_bktsums_bkt = 0
                if yrdata:
                    for yr in yrdata:
                        yr_d_id=yr.device_id
                        if yr_d_id == device_id:
                            rmt=yr.rmt
                            cct=yr.cct
                            srt=yr.srt
                            bkt=yr.bkt
                            rst=yr.rst
                            mot=yr.mot
                            sums_rmt=sums_rmt+rmt
                            sums_cct=sums_cct+cct
                            sums_srt=sums_srt+srt
                            sums_bkt=sums_bkt+bkt
                            sums_rst=sums_rst+rst
                            sums_mot=sums_mot+mot
                            count=count+1
                    avgs_rmt=sums_rmt/count
                    avgs_cct=sums_cct/count
                    avgs_srt=sums_srt/count
                    avgs_bkt=sums_bkt/count
                    avgs_rst=sums_rst/count
                    avgs_mot=sums_mot/count
                hr=ampv2_repo_yearly.objects.filter(year=dd[0],device_id=device_id)
                if hr:
                    yr_data=ampv2_repo_yearly.objects.filter(year=dd[0],device_id=device_id).update(device_id=device_id,service='ampv2',rmt={'sum':sums_rmt,'avg':avgs_rmt,'count':count},cct={'sum':sums_cct,'avg':avgs_cct,'count':count},srt={'sum':sums_srt,'avg':avgs_srt,'count':count},bkt={'sum':sums_bkt,'avg':avgs_bkt,'count':count},rst={'sum':sums_rst,'avg':avgs_rst,'count':count},mot={'sum':sums_mot,'avg':avgs_mot,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                else:
                    yr_data=ampv2_repo_yearly.objects.create(device_id=device_id,service='ampv2',rmt={'sum':sums_rmt,'avg':avgs_rmt,'count':count},cct={'sum':sums_cct,'avg':avgs_cct,'count':count},srt={'sum':sums_srt,'avg':avgs_srt,'count':count},bkt={'sum':sums_bkt,'avg':avgs_bkt,'count':count},rst={'sum':sums_rst,'avg':avgs_rst,'count':count},mot={'sum':sums_mot,'avg':avgs_mot,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                    yr_data.save()


            #     yrdata=treat_ampv2.objects.filter(year=dd[0],device_id=device_id)
            #     count=0
            #     sums=0
            #     avgs = 0
            #     if yrdata:
            #         for yr in yrdata:
            #             yr_d_id=yr.device_id
            #             if yr_d_id == device_id:
            #                 rmt=yr.rmt
            #                 print("rmt is:",rmt)
            #                 sums=sums+rmt
            #                 count=count+1
            #                 print("sums is:",sums)
            #                 print("count is:",count)
            #         avgs=sums/count
            #     hr=repo_yearly.objects.filter(service='ampv2_rmt',year=dd[0],device_id=device_id)
            #     if hr:
            #         yr_data=repo_yearly.objects.filter(device_id=device_id).update(device_id=device_id,service='ampv2_rmt',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
            #     else:
            #         yr_data=repo_yearly.objects.create(device_id=device_id,service='ampv2_rmt',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
            #         yr_data.save()
            #     yrdata=treat_ampv2.objects.filter(year=dd[0],device_id=device_id)
            #     count=0
            #     sums=0
            #     avgs = 0
            #     if yrdata:
            #         for yr in yrdata:
            #             yr_d_id=yr.device_id
            #             if yr_d_id == device_id:
            #                 cct=yr.cct
            #                 print("cct is:",cct)
            #                 sums=sums+cct
            #                 count=count+1
            #                 print("sums is:",sums)
            #                 print("count is:",count)
            #         avgs=sums/count
            #     hr=repo_yearly.objects.filter(service='ampv2_cct',year=dd[0],device_id=device_id)
            #     if hr:
            #         yr_data=repo_yearly.objects.filter(device_id=device_id).update(device_id=device_id,service='ampv2_cct',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
            #     else:
            #         yr_data=repo_yearly.objects.create(device_id=device_id,service='ampv2_cct',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
            #         yr_data.save()
                
            # # month
            #     yrdata=treat_ampv2.objects.filter(year=dd[0],month=dd[1],device_id=device_id)
            #     count=0
            #     sums=0
            #     avgs = 0
            #     if yrdata:
            #         for yr in yrdata:
            #             yr_d_id=yr.device_id
            #             if yr_d_id == device_id:
            #                 rmt=yr.rmt
            #                 print("rmt is:",rmt)
            #                 sums=sums+rmt
            #                 count=count+1
            #                 print("sums is:",sums)
            #                 print("count is:",count)
            #         avgs=sums/count
            #     hr=repo_monthly.objects.filter(service='ampv2_rmt',year=dd[0],month=dd[1],device_id=device_id)
            #     if hr:
            #         yr_data=repo_monthly.objects.filter(year=dd[0],month=dd[1],device_id=device_id).update(device_id=device_id,service='ampv2_rmt',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
            #     else:
            #         yr_data=repo_monthly.objects.create(device_id=device_id,service='ampv2_rmt',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
            #         yr_data.save()
            #     yrdata=treat_ampv2.objects.filter(year=dd[0],month=dd[1],device_id=device_id)
            #     count=0
            #     sums=0
            #     avgs = 0
            #     if yrdata:
            #         for yr in yrdata:
            #             yr_d_id=yr.device_id
            #             if yr_d_id == device_id:
            #                 cct=yr.cct
            #                 print("cct is:",cct)
            #                 sums=sums+cct
            #                 count=count+1
            #                 print("sums is:",sums)
            #                 print("count is:",count)
            #         avgs=sums/count
            #     hr=repo_monthly.objects.filter(service='ampv2_cct',year=dd[0],month=dd[1],device_id=device_id)
            #     if hr:
            #         yr_data=repo_monthly.objects.filter(year=dd[0],month=dd[1],device_id=device_id).update(device_id=device_id,service='ampv2_cct',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
            #     else:
            #         yr_data=repo_monthly.objects.create(device_id=device_id,service='ampv2_cct',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
            #         yr_data.save()
            # # day
            #     yrdata=treat_ampv2.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id)
            #     count=0
            #     sums=0
            #     avgs = 0
            #     if yrdata:
            #         for yr in yrdata:
            #             yr_d_id=yr.device_id
            #             if yr_d_id == device_id:
            #                 rmt=yr.rmt
            #                 print("rmt is:",rmt)
            #                 sums=sums+rmt
            #                 count=count+1
            #                 print("sums is:",sums)
            #                 print("count is:",count)
            #         avgs=sums/count
            #     hr=repo_daily.objects.filter(service='ampv2_rmt',year=dd[0],month=dd[1],day=dd[2],device_id=device_id)
            #     if hr:
            #         yr_data=repo_daily.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id).update(device_id=device_id,service='ampv2_rmt',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0],day=dd[2])
            #     else:
            #         yr_data=repo_daily.objects.create(device_id=device_id,service='ampv2_rmt',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0],day=dd[2])
            #         yr_data.save()
            #     yrdata=treat_ampv2.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id)
            #     count=0
            #     sums=0
            #     avgs = 0
            #     if yrdata:
            #         for yr in yrdata:
            #             yr_d_id=yr.device_id
            #             if yr_d_id == device_id:
            #                 cct=yr.cct
            #                 print("cct is:",cct)
            #                 sums=sums+cct
            #                 count=count+1
            #                 print("sums is:",sums)
            #                 print("count is:",count)
            #         avgs=sums/count
            #     hr=repo_daily.objects.filter(service='ampv2_cct',year=dd[0],month=dd[1],day=dd[2],device_id=device_id)
            #     if hr:
            #         yr_data=repo_daily.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id).update(device_id=device_id,service='ampv2_cct',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0],day=dd[2])
            #     else:
            #         yr_data=repo_daily.objects.create(device_id=device_id,service='ampv2_cct',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0],day=dd[2])
            #         yr_data.save()
            #     # hour
            #     yrdata=treat_ampv2.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id)
            #     count=0
            #     sums=0
            #     avgs = 0
            #     if yrdata:
            #         for yr in yrdata:
            #             yr_d_id=yr.device_id
            #             if yr_d_id == device_id:
            #                 rmt=yr.rmt
            #                 print("rmt is:",rmt)
            #                 sums=sums+rmt
            #                 count=count+1
            #                 print("sums is:",sums)
            #                 print("count is:",count)
            #         avgs=sums/count
            #     hr=repo_hourly.objects.filter(service='ampv2_rmt',year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id)
            #     if hr:
            #         yr_data=repo_hourly.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id).update(device_id=device_id,service='ampv2_rmt',sum=sums,count=count,avg=avgs,hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
            #     else:
            #         yr_data=repo_hourly.objects.create(device_id=device_id,service='ampv2_rmt',sum=sums,count=count,avg=avgs,hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
            #         yr_data.save()
            #     yrdata=treat_ampv2.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id)
            #     count=0
            #     sums=0
            #     avgs = 0
            #     if yrdata:
            #         for yr in yrdata:
            #             yr_d_id=yr.device_id
            #             if yr_d_id == device_id:
            #                 cct=yr.cct
            #                 print("cct is:",cct)
            #                 sums=sums+cct
            #                 count=count+1
            #                 print("sums is:",sums)
            #                 print("count is:",count)
            #         avgs=sums/count
            #     hr=repo_hourly.objects.filter(service='ampv2_cct',year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id)
            #     if hr:
            #         yr_data=repo_hourly.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id).update(device_id=device_id,service='ampv2_cct',sum=sums,count=count,avg=avgs,hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
            #     else:
            #         yr_data=repo_hourly.objects.create(device_id=device_id,service='ampv2_cct',sum=sums,count=count,avg=avgs,hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
            #         yr_data.save()
        except Exception as e:
            print("error ==>", e)
            error_message = e
            # global eg
            eg = e
            print("eg is:",eg)
            print("Error massage:",e)
            EchoConsumer.websocket_receive('event','event') 
        try:
            if 'ampv3'==components:
                # com=cl
                if device_id not in device_idlist:
                     repo_latestdata.objects.create(device_id=device_id,message_type=msg_type,ampv3=mydata1)
                else:
                    repo_latestobj = repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id, message_type=msg_type, ampv3=mydata1)

                    get_device_id=repo_latestdata.objects.all()
                    for did in get_device_id:
                        s=str(did.device_id)
                        if device_id == s:
                            ampv3=did.ampv3
                    klist = list(ampv3.keys())
                    print("klist is:",klist)
                    mydatakey = list(mydata1.keys())
                    print("mydatakey:",mydatakey)
                    for k,v in ampv3.items():
                         if k not in mydatakey:
                              olddata.update({k:v})
                              
                    mydata5=olddata.update(mydata1)    
                    print("old data is:",olddata) # add/update keys in mydata1 to olddata
                    repo_latestobj = repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id, message_type=msg_type, ampv3=olddata)

                ds=treat_ampv3.objects.create(device_id=device_id,message_type=msg_type,pos=pos,rmt=rmt,cct=cct,srt=srt,bkt=bkt,rst=rst,mot=mot,stp=stp,op1=op1,op2=op2,op3=op3,ip1=ip1,ip2=ip2,ip3=ip3,psi=psi,year=dd[0],month=dd[1],day=dd[2],hour=dd[3],minit=dd[4],second=dd[5])
                ds.save()
                #hour
                yrdata=treat_ampv3.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id)
                count=0
                zerocount=-1
                sumd={}
                sums_rmt=0
                sums_cct=0
                sums_srt=0
                sums_bkt=0
                sums_rst=0
                sums_mot=0
                avgs_rmt = 0
                avgs_cct = 0
                avgs_srt = 0
                avgs_bkt = 0
                avgs_rst = 0
                avgs_mot = 0
                # avgs_bktsums_bkt = 0
                if yrdata:
                    for yr in yrdata:
                        yr_d_id=yr.device_id
                        if yr_d_id == device_id:
                            rmt=yr.rmt
                            cct=yr.cct
                            srt=yr.srt
                            bkt=yr.bkt
                            rst=yr.rst
                            mot=yr.mot
                            sums_rmt=sums_rmt+rmt
                            sums_cct=sums_cct+cct
                            sums_srt=sums_srt+srt
                            sums_bkt=sums_bkt+bkt
                            sums_rst=sums_rst+rst
                            sums_mot=sums_mot+mot
                            count=count+1
                    avgs_rmt=sums_rmt/count
                    avgs_cct=sums_cct/count
                    avgs_srt=sums_srt/count
                    avgs_bkt=sums_bkt/count
                    avgs_rst=sums_rst/count
                    avgs_mot=sums_mot/count
                hr=ampv3_repo_hourly.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id)
                if hr:
                    yr_data=ampv3_repo_hourly.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id).update(device_id=device_id,service='ampv3',rmt={'sum':sums_rmt,'avg':avgs_rmt,'count':count},cct={'sum':sums_cct,'avg':avgs_cct,'count':count},srt={'sum':sums_srt,'avg':avgs_srt,'count':count},bkt={'sum':sums_bkt,'avg':avgs_bkt,'count':count},rst={'sum':sums_rst,'avg':avgs_rst,'count':count},mot={'sum':sums_mot,'avg':avgs_mot,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                else:
                    yr_data=ampv3_repo_hourly.objects.create(device_id=device_id,service='ampv3',rmt={'sum':sums_rmt,'avg':avgs_rmt,'count':count},cct={'sum':sums_cct,'avg':avgs_cct,'count':count},srt={'sum':sums_srt,'avg':avgs_srt,'count':count},bkt={'sum':sums_bkt,'avg':avgs_bkt,'count':count},rst={'sum':sums_rst,'avg':avgs_rst,'count':count},mot={'sum':sums_mot,'avg':avgs_mot,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                    yr_data.save()
                #daily
                yrdata=treat_ampv3.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id)
                count=0
                zerocount=-1
                sumd={}
                sums_rmt=0
                sums_cct=0
                sums_srt=0
                sums_bkt=0
                sums_rst=0
                sums_mot=0
                avgs_rmt = 0
                avgs_cct = 0
                avgs_srt = 0
                avgs_bkt = 0
                avgs_rst = 0
                avgs_mot = 0
                # avgs_bktsums_bkt = 0
                if yrdata:
                    for yr in yrdata:
                        yr_d_id=yr.device_id
                        if yr_d_id == device_id:
                            rmt=yr.rmt
                            cct=yr.cct
                            srt=yr.srt
                            bkt=yr.bkt
                            rst=yr.rst
                            mot=yr.mot
                            sums_rmt=sums_rmt+rmt
                            sums_cct=sums_cct+cct
                            sums_srt=sums_srt+srt
                            sums_bkt=sums_bkt+bkt
                            sums_rst=sums_rst+rst
                            sums_mot=sums_mot+mot
                            count=count+1
                    avgs_rmt=sums_rmt/count
                    avgs_cct=sums_cct/count
                    avgs_srt=sums_srt/count
                    avgs_bkt=sums_bkt/count
                    avgs_rst=sums_rst/count
                    avgs_mot=sums_mot/count
                hr=ampv3_repo_daily.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id)
                if hr:
                    yr_data=ampv3_repo_daily.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id).update(device_id=device_id,service='ampv3',rmt={'sum':sums_rmt,'avg':avgs_rmt,'count':count},cct={'sum':sums_cct,'avg':avgs_cct,'count':count},srt={'sum':sums_srt,'avg':avgs_srt,'count':count},bkt={'sum':sums_bkt,'avg':avgs_bkt,'count':count},rst={'sum':sums_rst,'avg':avgs_rst,'count':count},mot={'sum':sums_mot,'avg':avgs_mot,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                else:
                    yr_data=ampv3_repo_daily.objects.create(device_id=device_id,service='ampv3',rmt={'sum':sums_rmt,'avg':avgs_rmt,'count':count},cct={'sum':sums_cct,'avg':avgs_cct,'count':count},srt={'sum':sums_srt,'avg':avgs_srt,'count':count},bkt={'sum':sums_bkt,'avg':avgs_bkt,'count':count},rst={'sum':sums_rst,'avg':avgs_rst,'count':count},mot={'sum':sums_mot,'avg':avgs_mot,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                    yr_data.save()
                #month
                yrdata=treat_ampv3.objects.filter(year=dd[0],month=dd[1],device_id=device_id)
                count=0
                zerocount=-1
                sumd={}
                sums_rmt=0
                sums_cct=0
                sums_srt=0
                sums_bkt=0
                sums_rst=0
                sums_mot=0
                avgs_rmt = 0
                avgs_cct = 0
                avgs_srt = 0
                avgs_bkt = 0
                avgs_rst = 0
                avgs_mot = 0
                # avgs_bktsums_bkt = 0
                if yrdata:
                    for yr in yrdata:
                        yr_d_id=yr.device_id
                        if yr_d_id == device_id:
                            rmt=yr.rmt
                            cct=yr.cct
                            srt=yr.srt
                            bkt=yr.bkt
                            rst=yr.rst
                            mot=yr.mot
                            sums_rmt=sums_rmt+rmt
                            sums_cct=sums_cct+cct
                            sums_srt=sums_srt+srt
                            sums_bkt=sums_bkt+bkt
                            sums_rst=sums_rst+rst
                            sums_mot=sums_mot+mot
                            count=count+1
                    avgs_rmt=sums_rmt/count
                    avgs_cct=sums_cct/count
                    avgs_srt=sums_srt/count
                    avgs_bkt=sums_bkt/count
                    avgs_rst=sums_rst/count
                    avgs_mot=sums_mot/count
                hr=ampv3_repo_monthly.objects.filter(year=dd[0],month=dd[1],device_id=device_id)
                if hr:
                    yr_data=ampv3_repo_monthly.objects.filter(year=dd[0],month=dd[1],device_id=device_id).update(device_id=device_id,service='ampv3',rmt={'sum':sums_rmt,'avg':avgs_rmt,'count':count},cct={'sum':sums_cct,'avg':avgs_cct,'count':count},srt={'sum':sums_srt,'avg':avgs_srt,'count':count},bkt={'sum':sums_bkt,'avg':avgs_bkt,'count':count},rst={'sum':sums_rst,'avg':avgs_rst,'count':count},mot={'sum':sums_mot,'avg':avgs_mot,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                else:
                    yr_data=ampv3_repo_monthly.objects.create(device_id=device_id,service='ampv3',rmt={'sum':sums_rmt,'avg':avgs_rmt,'count':count},cct={'sum':sums_cct,'avg':avgs_cct,'count':count},srt={'sum':sums_srt,'avg':avgs_srt,'count':count},bkt={'sum':sums_bkt,'avg':avgs_bkt,'count':count},rst={'sum':sums_rst,'avg':avgs_rst,'count':count},mot={'sum':sums_mot,'avg':avgs_mot,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                    yr_data.save()
                #year
                yrdata=treat_ampv3.objects.filter(year=dd[0],device_id=device_id)
                count=0
                zerocount=-1
                sumd={}
                sums_rmt=0
                sums_cct=0
                sums_srt=0
                sums_bkt=0
                sums_rst=0
                sums_mot=0
                avgs_rmt = 0
                avgs_cct = 0
                avgs_srt = 0
                avgs_bkt = 0
                avgs_rst = 0
                avgs_mot = 0
                # avgs_bktsums_bkt = 0
                if yrdata:
                    for yr in yrdata:
                        yr_d_id=yr.device_id
                        if yr_d_id == device_id:
                            rmt=yr.rmt
                            cct=yr.cct
                            srt=yr.srt
                            bkt=yr.bkt
                            rst=yr.rst
                            mot=yr.mot
                            sums_rmt=sums_rmt+rmt
                            sums_cct=sums_cct+cct
                            sums_srt=sums_srt+srt
                            sums_bkt=sums_bkt+bkt
                            sums_rst=sums_rst+rst
                            sums_mot=sums_mot+mot
                            count=count+1
                    avgs_rmt=sums_rmt/count
                    avgs_cct=sums_cct/count
                    avgs_srt=sums_srt/count
                    avgs_bkt=sums_bkt/count
                    avgs_rst=sums_rst/count
                    avgs_mot=sums_mot/count
                hr=ampv3_repo_yearly.objects.filter(year=dd[0],device_id=device_id)
                if hr:
                    yr_data=ampv3_repo_yearly.objects.filter(year=dd[0],device_id=device_id).update(device_id=device_id,service='ampv3',rmt={'sum':sums_rmt,'avg':avgs_rmt,'count':count},cct={'sum':sums_cct,'avg':avgs_cct,'count':count},srt={'sum':sums_srt,'avg':avgs_srt,'count':count},bkt={'sum':sums_bkt,'avg':avgs_bkt,'count':count},rst={'sum':sums_rst,'avg':avgs_rst,'count':count},mot={'sum':sums_mot,'avg':avgs_mot,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                else:
                    yr_data=ampv3_repo_yearly.objects.create(device_id=device_id,service='ampv3',rmt={'sum':sums_rmt,'avg':avgs_rmt,'count':count},cct={'sum':sums_cct,'avg':avgs_cct,'count':count},srt={'sum':sums_srt,'avg':avgs_srt,'count':count},bkt={'sum':sums_bkt,'avg':avgs_bkt,'count':count},rst={'sum':sums_rst,'avg':avgs_rst,'count':count},mot={'sum':sums_mot,'avg':avgs_mot,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                    yr_data.save()

                # yrdata=treat_ampv3.objects.filter(year=dd[0],device_id=device_id)
                # count=0
                # sums=0
                # avgs = 0
                # if yrdata:
                #     for yr in yrdata:
                #         yr_d_id=yr.device_id
                #         if yr_d_id == device_id:
                #             rmt=yr.rmt
                #             print("rmt is:",rmt)
                #             sums=sums+rmt
                #             count=count+1
                #             print("sums is:",sums)
                #             print("count is:",count)
                #     avgs=sums/count
                # hr=repo_yearly.objects.filter(service='ampv3_rmt',year=dd[0],device_id=device_id)
                # if hr:
                #     yr_data=repo_yearly.objects.filter(device_id=device_id).update(device_id=device_id,service='ampv3_rmt',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
                # else:
                #     yr_data=repo_yearly.objects.create(device_id=device_id,service='ampv3_rmt',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
                #     yr_data.save()
                # yrdata=treat_ampv3.objects.filter(year=dd[0],device_id=device_id)
                # count=0
                # sums=0
                # avgs = 0
                # if yrdata:
                #     for yr in yrdata:
                #         yr_d_id=yr.device_id
                #         if yr_d_id == device_id:
                #             cct=yr.cct
                #             print("cct is:",cct)
                #             sums=sums+cct
                #             count=count+1
                #             print("sums is:",sums)
                #             print("count is:",count)
                #     avgs=sums/count
                # hr=repo_yearly.objects.filter(service='ampv3_cct',year=dd[0],device_id=device_id)
                # if hr:
                #     yr_data=repo_yearly.objects.filter(device_id=device_id).update(device_id=device_id,service='ampv3_cct',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
                # else:
                #     yr_data=repo_yearly.objects.create(device_id=device_id,service='ampv3_cct',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
                #     yr_data.save()
                #   # month
                # yrdata=treat_ampv3.objects.filter(year=dd[0],month=dd[1],device_id=device_id)
                # count=0
                # sums=0
                # avgs = 0
                # if yrdata:
                #     for yr in yrdata:
                #         yr_d_id=yr.device_id
                #         if yr_d_id == device_id:
                #             rmt=yr.rmt
                #             print("rmt is:",rmt)
                #             sums=sums+rmt
                #             count=count+1
                #             print("sums is:",sums)
                #             print("count is:",count)
                #     avgs=sums/count
                # hr=repo_monthly.objects.filter(service='ampv3_rmt',year=dd[0],month=dd[1],device_id=device_id)
                # if hr:
                #     yr_data=repo_monthly.objects.filter(year=dd[0],month=dd[1],device_id=device_id).update(device_id=device_id,service='ampv3_rmt',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
                # else:
                #     yr_data=repo_monthly.objects.create(device_id=device_id,service='ampv3_rmt',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
                #     yr_data.save()
                # yrdata=treat_ampv3.objects.filter(year=dd[0],month=dd[1],device_id=device_id)
                # count=0
                # sums=0
                # avgs = 0
                # if yrdata:
                #     for yr in yrdata:
                #         yr_d_id=yr.device_id
                #         if yr_d_id == device_id:
                #             cct=yr.cct
                #             print("cct is:",cct)
                #             sums=sums+cct
                #             count=count+1
                #             print("sums is:",sums)
                #             print("count is:",count)
                #     avgs=sums/count
                # hr=repo_monthly.objects.filter(service='ampv3_cct',year=dd[0],month=dd[1],device_id=device_id)
                # if hr:
                #     yr_data=repo_monthly.objects.filter(year=dd[0],month=dd[1],device_id=device_id).update(device_id=device_id,service='ampv3_cct',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
                # else:
                #     yr_data=repo_monthly.objects.create(device_id=device_id,service='ampv3_cct',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
                #     yr_data.save()
               
                # # day
                # yrdata=treat_ampv3.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id)
                # count=0
                # sums=0
                # avgs = 0
                # if yrdata:
                #     for yr in yrdata:
                #         yr_d_id=yr.device_id
                #         if yr_d_id == device_id:
                #             rmt=yr.rmt
                #             print("rmt is:",rmt)
                #             sums=sums+rmt
                #             count=count+1
                #             print("sums is:",sums)
                #             print("count is:",count)
                #     avgs=sums/count
                # hr=repo_daily.objects.filter(service='ampv3_rmt',year=dd[0],month=dd[1],day=dd[2],device_id=device_id)
                # if hr:
                #     yr_data=repo_daily.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id).update(device_id=device_id,service='ampv3_rmt',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0],day=dd[2])
                # else:
                #     yr_data=repo_daily.objects.create(device_id=device_id,service='ampv3_rmt',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0],day=dd[2])
                #     yr_data.save()
                # yrdata=treat_ampv3.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id)
                # count=0
                # sums=0
                # avgs = 0
                # if yrdata:
                #     for yr in yrdata:
                #         yr_d_id=yr.device_id
                #         if yr_d_id == device_id:
                #             cct=yr.cct
                #             print("cct is:",cct)
                #             sums=sums+cct
                #             count=count+1
                #             print("sums is:",sums)
                #             print("count is:",count)
                #     avgs=sums/count
                # hr=repo_daily.objects.filter(service='ampv3_cct',year=dd[0],month=dd[1],day=dd[2],device_id=device_id)
                # if hr:
                #     yr_data=repo_daily.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id).update(device_id=device_id,service='ampv3_cct',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0],day=dd[2])
                # else:
                #     yr_data=repo_daily.objects.create(device_id=device_id,service='ampv3_cct',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0],day=dd[2])
                #     yr_data.save()
                
                # # hour

                # yrdata=treat_ampv3.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id)
                # count=0
                # sums=0
                # avgs = 0
                # if yrdata:
                #     for yr in yrdata:
                #         yr_d_id=yr.device_id
                #         if yr_d_id == device_id:
                #             rmt=yr.rmt
                #             print("rmt is:",rmt)
                #             sums=sums+rmt
                #             count=count+1
                #             print("sums is:",sums)
                #             print("count is:",count)
                #     avgs=sums/count
                # hr=repo_hourly.objects.filter(service='ampv3_rmt',year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id)
                # if hr:
                #     yr_data=repo_hourly.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id).update(device_id=device_id,service='ampv3_rmt',sum=sums,count=count,avg=avgs,hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                # else:
                #     yr_data=repo_hourly.objects.create(device_id=device_id,service='ampv3_rmt',sum=sums,count=count,avg=avgs,hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                #     yr_data.save()
                # yrdata=treat_ampv3.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id)
                # count=0
                # sums=0
                # avgs = 0
                # if yrdata:
                #     for yr in yrdata:
                #         yr_d_id=yr.device_id
                #         if yr_d_id == device_id:
                #             cct=yr.cct
                #             print("cct is:",cct)
                #             sums=sums+cct
                #             count=count+1
                #             print("sums is:",sums)
                #             print("count is:",count)
                #     avgs=sums/count
                # hr=repo_hourly.objects.filter(service='ampv3_cct',year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id)
                # if hr:
                #     yr_data=repo_hourly.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id).update(device_id=device_id,service='ampv3_cct',sum=sums,count=count,avg=avgs,hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                # else:
                #     yr_data=repo_hourly.objects.create(device_id=device_id,service='ampv3_cct',sum=sums,count=count,avg=avgs,hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                #     yr_data.save()
        except Exception as e:
            print("error ==>", e)
            error_message = e
            # global eg
            eg = e
            print("eg is:",eg)
            print("Error massage:",e)
            EchoConsumer.websocket_receive('event','event') 
        try:        
            if 'ampv4'==components:
                # com=cl
                if device_id not in device_idlist:
                     repo_latestdata.objects.create(device_id=device_id,message_type=msg_type,ampv4=mydata1)
                else:
                    repo_latestobj = repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id, message_type=msg_type, ampv4=mydata1)

                    get_device_id=repo_latestdata.objects.all()
                    for did in get_device_id:
                        s=str(did.device_id)
                        if device_id == s:
                            ampv4=did.ampv4
                    klist = list(ampv4.keys())
                    print("klist is:",klist)
                    mydatakey = list(mydata1.keys())
                    print("mydatakey:",mydatakey)
                    for k,v in ampv4.items():
                         if k not in mydatakey:
                              olddata.update({k:v})
                              
                    mydata5=olddata.update(mydata1)    
                    print("old data is:",olddata) # add/update keys in mydata1 to olddata
                    repo_latestobj = repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id, message_type=msg_type, ampv4=olddata)

                ds=treat_ampv4.objects.create(device_id=device_id,message_type=msg_type,pos=pos,rmt=rmt,cct=cct,srt=srt,bkt=bkt,rst=rst,mot=mot,stp=stp,op1=op1,op2=op2,op3=op3,ip1=ip1,ip2=ip2,ip3=ip3,psi=psi,year=dd[0],month=dd[1],day=dd[2],hour=dd[3],minit=dd[4],second=dd[5])
                ds.save()
                #hour
                yrdata=treat_ampv4.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id)
                count=0
                zerocount=-1
                sumd={}
                sums_rmt=0
                sums_cct=0
                sums_srt=0
                sums_bkt=0
                sums_rst=0
                sums_mot=0
                avgs_rmt = 0
                avgs_cct = 0
                avgs_srt = 0
                avgs_bkt = 0
                avgs_rst = 0
                avgs_mot = 0
                # avgs_bktsums_bkt = 0
                if yrdata:
                    for yr in yrdata:
                        yr_d_id=yr.device_id
                        if yr_d_id == device_id:
                            rmt=yr.rmt
                            cct=yr.cct
                            srt=yr.srt
                            bkt=yr.bkt
                            rst=yr.rst
                            mot=yr.mot
                            sums_rmt=sums_rmt+rmt
                            sums_cct=sums_cct+cct
                            sums_srt=sums_srt+srt
                            sums_bkt=sums_bkt+bkt
                            sums_rst=sums_rst+rst
                            sums_mot=sums_mot+mot
                            count=count+1
                    avgs_rmt=sums_rmt/count
                    avgs_cct=sums_cct/count
                    avgs_srt=sums_srt/count
                    avgs_bkt=sums_bkt/count
                    avgs_rst=sums_rst/count
                    avgs_mot=sums_mot/count
                hr=ampv4_repo_hourly.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id)
                if hr:
                    yr_data=ampv4_repo_hourly.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id).update(device_id=device_id,service='ampv4',rmt={'sum':sums_rmt,'avg':avgs_rmt,'count':count},cct={'sum':sums_cct,'avg':avgs_cct,'count':count},srt={'sum':sums_srt,'avg':avgs_srt,'count':count},bkt={'sum':sums_bkt,'avg':avgs_bkt,'count':count},rst={'sum':sums_rst,'avg':avgs_rst,'count':count},mot={'sum':sums_mot,'avg':avgs_mot,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                else:
                    yr_data=ampv4_repo_hourly.objects.create(device_id=device_id,service='ampv4',rmt={'sum':sums_rmt,'avg':avgs_rmt,'count':count},cct={'sum':sums_cct,'avg':avgs_cct,'count':count},srt={'sum':sums_srt,'avg':avgs_srt,'count':count},bkt={'sum':sums_bkt,'avg':avgs_bkt,'count':count},rst={'sum':sums_rst,'avg':avgs_rst,'count':count},mot={'sum':sums_mot,'avg':avgs_mot,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                    yr_data.save()
                #daily
                yrdata=treat_ampv4.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id)
                count=0
                zerocount=-1
                sumd={}
                sums_rmt=0
                sums_cct=0
                sums_srt=0
                sums_bkt=0
                sums_rst=0
                sums_mot=0
                avgs_rmt = 0
                avgs_cct = 0
                avgs_srt = 0
                avgs_bkt = 0
                avgs_rst = 0
                avgs_mot = 0
                # avgs_bktsums_bkt = 0
                if yrdata:
                    for yr in yrdata:
                        yr_d_id=yr.device_id
                        if yr_d_id == device_id:
                            rmt=yr.rmt
                            cct=yr.cct
                            srt=yr.srt
                            bkt=yr.bkt
                            rst=yr.rst
                            mot=yr.mot
                            sums_rmt=sums_rmt+rmt
                            sums_cct=sums_cct+cct
                            sums_srt=sums_srt+srt
                            sums_bkt=sums_bkt+bkt
                            sums_rst=sums_rst+rst
                            sums_mot=sums_mot+mot
                            count=count+1
                    avgs_rmt=sums_rmt/count
                    avgs_cct=sums_cct/count
                    avgs_srt=sums_srt/count
                    avgs_bkt=sums_bkt/count
                    avgs_rst=sums_rst/count
                    avgs_mot=sums_mot/count
                hr=ampv4_repo_daily.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id)
                if hr:
                    yr_data=ampv4_repo_daily.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id).update(device_id=device_id,service='ampv4',rmt={'sum':sums_rmt,'avg':avgs_rmt,'count':count},cct={'sum':sums_cct,'avg':avgs_cct,'count':count},srt={'sum':sums_srt,'avg':avgs_srt,'count':count},bkt={'sum':sums_bkt,'avg':avgs_bkt,'count':count},rst={'sum':sums_rst,'avg':avgs_rst,'count':count},mot={'sum':sums_mot,'avg':avgs_mot,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                else:
                    yr_data=ampv4_repo_daily.objects.create(device_id=device_id,service='ampv4',rmt={'sum':sums_rmt,'avg':avgs_rmt,'count':count},cct={'sum':sums_cct,'avg':avgs_cct,'count':count},srt={'sum':sums_srt,'avg':avgs_srt,'count':count},bkt={'sum':sums_bkt,'avg':avgs_bkt,'count':count},rst={'sum':sums_rst,'avg':avgs_rst,'count':count},mot={'sum':sums_mot,'avg':avgs_mot,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                    yr_data.save()
                #month
                yrdata=treat_ampv4.objects.filter(year=dd[0],month=dd[1],device_id=device_id)
                count=0
                zerocount=-1
                sumd={}
                sums_rmt=0
                sums_cct=0
                sums_srt=0
                sums_bkt=0
                sums_rst=0
                sums_mot=0
                avgs_rmt = 0
                avgs_cct = 0
                avgs_srt = 0
                avgs_bkt = 0
                avgs_rst = 0
                avgs_mot = 0
                # avgs_bktsums_bkt = 0
                if yrdata:
                    for yr in yrdata:
                        yr_d_id=yr.device_id
                        if yr_d_id == device_id:
                            rmt=yr.rmt
                            cct=yr.cct
                            srt=yr.srt
                            bkt=yr.bkt
                            rst=yr.rst
                            mot=yr.mot
                            sums_rmt=sums_rmt+rmt
                            sums_cct=sums_cct+cct
                            sums_srt=sums_srt+srt
                            sums_bkt=sums_bkt+bkt
                            sums_rst=sums_rst+rst
                            sums_mot=sums_mot+mot
                            count=count+1
                    avgs_rmt=sums_rmt/count
                    avgs_cct=sums_cct/count
                    avgs_srt=sums_srt/count
                    avgs_bkt=sums_bkt/count
                    avgs_rst=sums_rst/count
                    avgs_mot=sums_mot/count
                hr=ampv4_repo_monthly.objects.filter(year=dd[0],month=dd[1],device_id=device_id)
                if hr:
                    yr_data=ampv4_repo_monthly.objects.filter(year=dd[0],month=dd[1],device_id=device_id).update(device_id=device_id,service='ampv4',rmt={'sum':sums_rmt,'avg':avgs_rmt,'count':count},cct={'sum':sums_cct,'avg':avgs_cct,'count':count},srt={'sum':sums_srt,'avg':avgs_srt,'count':count},bkt={'sum':sums_bkt,'avg':avgs_bkt,'count':count},rst={'sum':sums_rst,'avg':avgs_rst,'count':count},mot={'sum':sums_mot,'avg':avgs_mot,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                else:
                    yr_data=ampv4_repo_monthly.objects.create(device_id=device_id,service='ampv4',rmt={'sum':sums_rmt,'avg':avgs_rmt,'count':count},cct={'sum':sums_cct,'avg':avgs_cct,'count':count},srt={'sum':sums_srt,'avg':avgs_srt,'count':count},bkt={'sum':sums_bkt,'avg':avgs_bkt,'count':count},rst={'sum':sums_rst,'avg':avgs_rst,'count':count},mot={'sum':sums_mot,'avg':avgs_mot,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                    yr_data.save()
                #year
                yrdata=treat_ampv4.objects.filter(year=dd[0],device_id=device_id)
                count=0
                zerocount=-1
                sumd={}
                sums_rmt=0
                sums_cct=0
                sums_srt=0
                sums_bkt=0
                sums_rst=0
                sums_mot=0
                avgs_rmt = 0
                avgs_cct = 0
                avgs_srt = 0
                avgs_bkt = 0
                avgs_rst = 0
                avgs_mot = 0
                # avgs_bktsums_bkt = 0
                if yrdata:
                    for yr in yrdata:
                        yr_d_id=yr.device_id
                        if yr_d_id == device_id:
                            rmt=yr.rmt
                            cct=yr.cct
                            srt=yr.srt
                            bkt=yr.bkt
                            rst=yr.rst
                            mot=yr.mot
                            sums_rmt=sums_rmt+rmt
                            sums_cct=sums_cct+cct
                            sums_srt=sums_srt+srt
                            sums_bkt=sums_bkt+bkt
                            sums_rst=sums_rst+rst
                            sums_mot=sums_mot+mot
                            count=count+1
                    avgs_rmt=sums_rmt/count
                    avgs_cct=sums_cct/count
                    avgs_srt=sums_srt/count
                    avgs_bkt=sums_bkt/count
                    avgs_rst=sums_rst/count
                    avgs_mot=sums_mot/count
                hr=ampv4_repo_yearly.objects.filter(year=dd[0],device_id=device_id)
                if hr:
                    yr_data=ampv4_repo_yearly.objects.filter(year=dd[0],device_id=device_id).update(device_id=device_id,service='ampv4',rmt={'sum':sums_rmt,'avg':avgs_rmt,'count':count},cct={'sum':sums_cct,'avg':avgs_cct,'count':count},srt={'sum':sums_srt,'avg':avgs_srt,'count':count},bkt={'sum':sums_bkt,'avg':avgs_bkt,'count':count},rst={'sum':sums_rst,'avg':avgs_rst,'count':count},mot={'sum':sums_mot,'avg':avgs_mot,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                else:
                    yr_data=ampv4_repo_yearly.objects.create(device_id=device_id,service='ampv4',rmt={'sum':sums_rmt,'avg':avgs_rmt,'count':count},cct={'sum':sums_cct,'avg':avgs_cct,'count':count},srt={'sum':sums_srt,'avg':avgs_srt,'count':count},bkt={'sum':sums_bkt,'avg':avgs_bkt,'count':count},rst={'sum':sums_rst,'avg':avgs_rst,'count':count},mot={'sum':sums_mot,'avg':avgs_mot,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                    yr_data.save()


            #     yrdata=treat_ampv4.objects.filter(year=dd[0],device_id=device_id)
            #     count=0
            #     sums=0
            #     avgs = 0
            #     if yrdata:
            #         for yr in yrdata:
            #             yr_d_id=yr.device_id
            #             if yr_d_id == device_id:
            #                 rmt=yr.rmt
            #                 print("rmt is:",rmt)
            #                 sums=sums+rmt
            #                 count=count+1
            #                 print("sums is:",sums)
            #                 print("count is:",count)
            #         avgs=sums/count
            #     hr=repo_yearly.objects.filter(service='ampv4_rmt',year=dd[0],device_id=device_id)
            #     if hr:
            #         yr_data=repo_yearly.objects.filter(device_id=device_id).update(device_id=device_id,service='ampv4_rmt',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
            #     else:
            #         yr_data=repo_yearly.objects.create(device_id=device_id,service='ampv4_rmt',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
            #         yr_data.save()
            #     yrdata=treat_ampv2.objects.filter(year=dd[0],device_id=device_id)
            #     count=0
            #     sums=0
            #     avgs = 0
            #     if yrdata:
            #         for yr in yrdata:
            #             yr_d_id=yr.device_id
            #             if yr_d_id == device_id:
            #                 cct=yr.cct
            #                 print("cct is:",cct)
            #                 sums=sums+cct
            #                 count=count+1
            #                 print("sums is:",sums)
            #                 print("count is:",count)
            #         avgs=sums/count
            #     hr=repo_yearly.objects.filter(service='ampv4_cct',year=dd[0],device_id=device_id)
            #     if hr:
            #         yr_data=repo_yearly.objects.filter(device_id=device_id).update(device_id=device_id,service='ampv4_cct',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
            #     else:
            #         yr_data=repo_yearly.objects.create(device_id=device_id,service='ampv4_cct',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
            #         yr_data.save()
                
            #  #    month
            #     yrdata=treat_ampv4.objects.filter(year=dd[0],month=dd[1],device_id=device_id)
            #     count=0
            #     sums=0
            #     avgs = 0
            #     if yrdata:
            #         for yr in yrdata:
            #             yr_d_id=yr.device_id
            #             if yr_d_id == device_id:
            #                 rmt=yr.rmt
            #                 print("rmt is:",rmt)
            #                 sums=sums+rmt
            #                 count=count+1
            #                 print("sums is:",sums)
            #                 print("count is:",count)
            #         avgs=sums/count
            #     hr=repo_monthly.objects.filter(service='ampv4_rmt',year=dd[0],month=dd[1],device_id=device_id)
            #     if hr:
            #         yr_data=repo_monthly.objects.filter(year=dd[0],month=dd[1],device_id=device_id).update(device_id=device_id,service='ampv4_rmt',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
            #     else:
            #         yr_data=repo_monthly.objects.create(device_id=device_id,service='ampv4_rmt',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
            #         yr_data.save()
            #     yrdata=treat_ampv4.objects.filter(year=dd[0],month=dd[1],device_id=device_id)
            #     count=0
            #     sums=0
            #     avgs = 0
            #     if yrdata:
            #         for yr in yrdata:
            #             yr_d_id=yr.device_id
            #             if yr_d_id == device_id:
            #                 cct=yr.cct
            #                 print("cct is:",cct)
            #                 sums=sums+cct
            #                 count=count+1
            #                 print("sums is:",sums)
            #                 print("count is:",count)
            #         avgs=sums/count
            #     hr=repo_monthly.objects.filter(service='ampv4_cct',year=dd[0],month=dd[1],device_id=device_id)
            #     if hr:
            #         yr_data=repo_monthly.objects.filter(year=dd[0],month=dd[1],device_id=device_id).update(device_id=device_id,service='ampv4_cct',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
            #     else:
            #         yr_data=repo_monthly.objects.create(device_id=device_id,service='ampv4_cct',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
            #         yr_data.save()
        
            #     # day

            #     yrdata=treat_ampv4.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id)
            #     count=0
            #     sums=0
            #     avgs = 0
            #     if yrdata:
            #         for yr in yrdata:
            #             yr_d_id=yr.device_id
            #             if yr_d_id == device_id:
            #                 rmt=yr.rmt
            #                 print("rmt is:",rmt)
            #                 sums=sums+rmt
            #                 count=count+1
            #                 print("sums is:",sums)
            #                 print("count is:",count)
            #         avgs=sums/count
            #     hr=repo_daily.objects.filter(service='ampv4_rmt',year=dd[0],month=dd[1],day=dd[2],device_id=device_id)
            #     if hr:
            #         yr_data=repo_daily.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id).update(device_id=device_id,service='ampv4_rmt',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0],day=dd[2])
            #     else:
            #         yr_data=repo_daily.objects.create(device_id=device_id,service='ampv4_rmt',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0],day=dd[2])
            #         yr_data.save()
            #     yrdata=treat_ampv4.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id)
            #     count=0
            #     sums=0
            #     avgs = 0
            #     if yrdata:
            #         for yr in yrdata:
            #             yr_d_id=yr.device_id
            #             if yr_d_id == device_id:
            #                 cct=yr.cct
            #                 print("cct is:",cct)
            #                 sums=sums+cct
            #                 count=count+1
            #                 print("sums is:",sums)
            #                 print("count is:",count)
            #         avgs=sums/count
            #     hr=repo_daily.objects.filter(service='ampv4_cct',year=dd[0],month=dd[1],day=dd[2],device_id=device_id)
            #     if hr:
            #         yr_data=repo_daily.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id).update(device_id=device_id,service='ampv4_cct',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0],day=dd[2])
            #     else:
            #         yr_data=repo_daily.objects.create(device_id=device_id,service='ampv4_cct',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0],day=dd[2])
            #         yr_data.save()
            #     # hour

            #     yrdata=treat_ampv4.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id)
            #     count=0
            #     sums=0
            #     avgs = 0
            #     if yrdata:
            #         for yr in yrdata:
            #             yr_d_id=yr.device_id
            #             if yr_d_id == device_id:
            #                 rmt=yr.rmt
            #                 print("rmt is:",rmt)
            #                 sums=sums+rmt
            #                 count=count+1
            #                 print("sums is:",sums)
            #                 print("count is:",count)
            #         avgs=sums/count
            #     hr=repo_hourly.objects.filter(service='ampv4_rmt',year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id)
            #     if hr:
            #         yr_data=repo_hourly.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id).update(device_id=device_id,service='ampv4_rmt',sum=sums,count=count,avg=avgs,hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
            #     else:
            #         yr_data=repo_hourly.objects.create(device_id=device_id,service='ampv4_rmt',sum=sums,count=count,avg=avgs,hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
            #         yr_data.save()
            #     yrdata=treat_ampv4.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id)
            #     count=0
            #     sums=0
            #     avgs = 0
            #     if yrdata:
            #         for yr in yrdata:
            #             yr_d_id=yr.device_id
            #             if yr_d_id == device_id:
            #                 cct=yr.cct
            #                 print("cct is:",cct)
            #                 sums=sums+cct
            #                 count=count+1
            #                 print("sums is:",sums)
            #                 print("count is:",count)
            #         avgs=sums/count
            #     hr=repo_hourly.objects.filter(service='ampv4_cct',year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id)
            #     if hr:
            #         yr_data=repo_hourly.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id).update(device_id=device_id,service='ampv4_cct',sum=sums,count=count,avg=avgs,hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
            #     else:
            #         yr_data=repo_hourly.objects.create(device_id=device_id,service='ampv4_cct',sum=sums,count=count,avg=avgs,hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
            #         yr_data.save()
        except Exception as e:
            print("error ==>", e)
            error_message = e
            # global eg
            eg = e
            print("eg is:",eg)
            print("Error massage:",e)
            EchoConsumer.websocket_receive('event','event') 
        try:       
            if 'ampv5'==components:
                # com=cl
                if device_id not in device_idlist:
                     repo_latestdata.objects.create(device_id=device_id,message_type=msg_type,ampv5=mydata1)
                else:
                    repo_latestobj = repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id, message_type=msg_type, ampv5=mydata1)

                    get_device_id=repo_latestdata.objects.all()
                    for did in get_device_id:
                        s=str(did.device_id)
                        if device_id == s:
                            ampv5=did.ampv5
                    klist = list(ampv5.keys())
                    print("klist is:",klist)
                    mydatakey = list(mydata1.keys())
                    print("mydatakey:",mydatakey)
                    for k,v in ampv5.items():
                         if k not in mydatakey:
                              olddata.update({k:v})
                              
                    mydata5=olddata.update(mydata1)    
                    print("old data is:",olddata) # add/update keys in mydata1 to olddata
                    repo_latestobj = repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id, message_type=msg_type, ampv5=olddata)

                ds=treat_ampv5.objects.create(device_id=device_id,message_type=msg_type,pos=pos,rmt=rmt,cct=cct,srt=srt,bkt=bkt,rst=rst,mot=mot,stp=stp,op1=op1,op2=op2,op3=op3,ip1=ip1,ip2=ip2,ip3=ip3,psi=psi,year=dd[0],month=dd[1],day=dd[2],hour=dd[3],minit=dd[4],second=dd[5])
                ds.save()

                #hour
                yrdata=treat_ampv5.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id)
                count=0
                zerocount=-1
                sumd={}
                sums_rmt=0
                sums_cct=0
                sums_srt=0
                sums_bkt=0
                sums_rst=0
                sums_mot=0
                avgs_rmt = 0
                avgs_cct = 0
                avgs_srt = 0
                avgs_bkt = 0
                avgs_rst = 0
                avgs_mot = 0
                # avgs_bktsums_bkt = 0
                if yrdata:
                    for yr in yrdata:
                        yr_d_id=yr.device_id
                        if yr_d_id == device_id:
                            rmt=yr.rmt
                            cct=yr.cct
                            srt=yr.srt
                            bkt=yr.bkt
                            rst=yr.rst
                            mot=yr.mot
                            sums_rmt=sums_rmt+rmt
                            sums_cct=sums_cct+cct
                            sums_srt=sums_srt+srt
                            sums_bkt=sums_bkt+bkt
                            sums_rst=sums_rst+rst
                            sums_mot=sums_mot+mot
                            count=count+1
                    avgs_rmt=sums_rmt/count
                    avgs_cct=sums_cct/count
                    avgs_srt=sums_srt/count
                    avgs_bkt=sums_bkt/count
                    avgs_rst=sums_rst/count
                    avgs_mot=sums_mot/count
                hr=ampv5_repo_hourly.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id)
                if hr:
                    yr_data=ampv5_repo_hourly.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id).update(device_id=device_id,service='ampv5',rmt={'sum':sums_rmt,'avg':avgs_rmt,'count':count},cct={'sum':sums_cct,'avg':avgs_cct,'count':count},srt={'sum':sums_srt,'avg':avgs_srt,'count':count},bkt={'sum':sums_bkt,'avg':avgs_bkt,'count':count},rst={'sum':sums_rst,'avg':avgs_rst,'count':count},mot={'sum':sums_mot,'avg':avgs_mot,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                else:
                    yr_data=ampv5_repo_hourly.objects.create(device_id=device_id,service='ampv5',rmt={'sum':sums_rmt,'avg':avgs_rmt,'count':count},cct={'sum':sums_cct,'avg':avgs_cct,'count':count},srt={'sum':sums_srt,'avg':avgs_srt,'count':count},bkt={'sum':sums_bkt,'avg':avgs_bkt,'count':count},rst={'sum':sums_rst,'avg':avgs_rst,'count':count},mot={'sum':sums_mot,'avg':avgs_mot,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                    yr_data.save()
                #daily
                yrdata=treat_ampv5.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id)
                count=0
                zerocount=-1
                sumd={}
                sums_rmt=0
                sums_cct=0
                sums_srt=0
                sums_bkt=0
                sums_rst=0
                sums_mot=0
                avgs_rmt = 0
                avgs_cct = 0
                avgs_srt = 0
                avgs_bkt = 0
                avgs_rst = 0
                avgs_mot = 0
                # avgs_bktsums_bkt = 0
                if yrdata:
                    for yr in yrdata:
                        yr_d_id=yr.device_id
                        if yr_d_id == device_id:
                            rmt=yr.rmt
                            cct=yr.cct
                            srt=yr.srt
                            bkt=yr.bkt
                            rst=yr.rst
                            mot=yr.mot
                            sums_rmt=sums_rmt+rmt
                            sums_cct=sums_cct+cct
                            sums_srt=sums_srt+srt
                            sums_bkt=sums_bkt+bkt
                            sums_rst=sums_rst+rst
                            sums_mot=sums_mot+mot
                            count=count+1
                    avgs_rmt=sums_rmt/count
                    avgs_cct=sums_cct/count
                    avgs_srt=sums_srt/count
                    avgs_bkt=sums_bkt/count
                    avgs_rst=sums_rst/count
                    avgs_mot=sums_mot/count
                hr=ampv5_repo_daily.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id)
                if hr:
                    yr_data=ampv5_repo_daily.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id).update(device_id=device_id,service='ampv5',rmt={'sum':sums_rmt,'avg':avgs_rmt,'count':count},cct={'sum':sums_cct,'avg':avgs_cct,'count':count},srt={'sum':sums_srt,'avg':avgs_srt,'count':count},bkt={'sum':sums_bkt,'avg':avgs_bkt,'count':count},rst={'sum':sums_rst,'avg':avgs_rst,'count':count},mot={'sum':sums_mot,'avg':avgs_mot,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                else:
                    yr_data=ampv5_repo_daily.objects.create(device_id=device_id,service='ampv5',rmt={'sum':sums_rmt,'avg':avgs_rmt,'count':count},cct={'sum':sums_cct,'avg':avgs_cct,'count':count},srt={'sum':sums_srt,'avg':avgs_srt,'count':count},bkt={'sum':sums_bkt,'avg':avgs_bkt,'count':count},rst={'sum':sums_rst,'avg':avgs_rst,'count':count},mot={'sum':sums_mot,'avg':avgs_mot,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                    yr_data.save()
                #month
                yrdata=treat_ampv5.objects.filter(year=dd[0],month=dd[1],device_id=device_id)
                count=0
                zerocount=-1
                sumd={}
                sums_rmt=0
                sums_cct=0
                sums_srt=0
                sums_bkt=0
                sums_rst=0
                sums_mot=0
                avgs_rmt = 0
                avgs_cct = 0
                avgs_srt = 0
                avgs_bkt = 0
                avgs_rst = 0
                avgs_mot = 0
                # avgs_bktsums_bkt = 0
                if yrdata:
                    for yr in yrdata:
                        yr_d_id=yr.device_id
                        if yr_d_id == device_id:
                            rmt=yr.rmt
                            cct=yr.cct
                            srt=yr.srt
                            bkt=yr.bkt
                            rst=yr.rst
                            mot=yr.mot
                            sums_rmt=sums_rmt+rmt
                            sums_cct=sums_cct+cct
                            sums_srt=sums_srt+srt
                            sums_bkt=sums_bkt+bkt
                            sums_rst=sums_rst+rst
                            sums_mot=sums_mot+mot
                            count=count+1
                    avgs_rmt=sums_rmt/count
                    avgs_cct=sums_cct/count
                    avgs_srt=sums_srt/count
                    avgs_bkt=sums_bkt/count
                    avgs_rst=sums_rst/count
                    avgs_mot=sums_mot/count
                hr=ampv5_repo_monthly.objects.filter(year=dd[0],month=dd[1],device_id=device_id)
                if hr:
                    yr_data=ampv5_repo_monthly.objects.filter(year=dd[0],month=dd[1],device_id=device_id).update(device_id=device_id,service='ampv5',rmt={'sum':sums_rmt,'avg':avgs_rmt,'count':count},cct={'sum':sums_cct,'avg':avgs_cct,'count':count},srt={'sum':sums_srt,'avg':avgs_srt,'count':count},bkt={'sum':sums_bkt,'avg':avgs_bkt,'count':count},rst={'sum':sums_rst,'avg':avgs_rst,'count':count},mot={'sum':sums_mot,'avg':avgs_mot,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                else:
                    yr_data=ampv5_repo_monthly.objects.create(device_id=device_id,service='ampv5',rmt={'sum':sums_rmt,'avg':avgs_rmt,'count':count},cct={'sum':sums_cct,'avg':avgs_cct,'count':count},srt={'sum':sums_srt,'avg':avgs_srt,'count':count},bkt={'sum':sums_bkt,'avg':avgs_bkt,'count':count},rst={'sum':sums_rst,'avg':avgs_rst,'count':count},mot={'sum':sums_mot,'avg':avgs_mot,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                    yr_data.save()
                #year
                yrdata=treat_ampv5.objects.filter(year=dd[0],device_id=device_id)
                count=0
                zerocount=-1
                sumd={}
                sums_rmt=0
                sums_cct=0
                sums_srt=0
                sums_bkt=0
                sums_rst=0
                sums_mot=0
                avgs_rmt = 0
                avgs_cct = 0
                avgs_srt = 0
                avgs_bkt = 0
                avgs_rst = 0
                avgs_mot = 0
                # avgs_bktsums_bkt = 0
                if yrdata:
                    for yr in yrdata:
                        yr_d_id=yr.device_id
                        if yr_d_id == device_id:
                            rmt=yr.rmt
                            cct=yr.cct
                            srt=yr.srt
                            bkt=yr.bkt
                            rst=yr.rst
                            mot=yr.mot
                            sums_rmt=sums_rmt+rmt
                            sums_cct=sums_cct+cct
                            sums_srt=sums_srt+srt
                            sums_bkt=sums_bkt+bkt
                            sums_rst=sums_rst+rst
                            sums_mot=sums_mot+mot
                            count=count+1
                    avgs_rmt=sums_rmt/count
                    avgs_cct=sums_cct/count
                    avgs_srt=sums_srt/count
                    avgs_bkt=sums_bkt/count
                    avgs_rst=sums_rst/count
                    avgs_mot=sums_mot/count
                hr=ampv5_repo_yearly.objects.filter(year=dd[0],device_id=device_id)
                if hr:
                    yr_data=ampv5_repo_yearly.objects.filter(year=dd[0],device_id=device_id).update(device_id=device_id,service='ampv5',rmt={'sum':sums_rmt,'avg':avgs_rmt,'count':count},cct={'sum':sums_cct,'avg':avgs_cct,'count':count},srt={'sum':sums_srt,'avg':avgs_srt,'count':count},bkt={'sum':sums_bkt,'avg':avgs_bkt,'count':count},rst={'sum':sums_rst,'avg':avgs_rst,'count':count},mot={'sum':sums_mot,'avg':avgs_mot,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                else:
                    yr_data=ampv5_repo_yearly.objects.create(device_id=device_id,service='ampv5',rmt={'sum':sums_rmt,'avg':avgs_rmt,'count':count},cct={'sum':sums_cct,'avg':avgs_cct,'count':count},srt={'sum':sums_srt,'avg':avgs_srt,'count':count},bkt={'sum':sums_bkt,'avg':avgs_bkt,'count':count},rst={'sum':sums_rst,'avg':avgs_rst,'count':count},mot={'sum':sums_mot,'avg':avgs_mot,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                    yr_data.save()


            #     yrdata=treat_ampv5.objects.filter(year=dd[0],device_id=device_id)
            #     count=0
            #     sums=0
            #     avgs = 0
            #     if yrdata:
            #         for yr in yrdata:
            #             yr_d_id=yr.device_id
            #             if yr_d_id == device_id:
            #                 rmt=yr.rmt
            #                 print("rmt is:",rmt)
            #                 sums=sums+rmt
            #                 count=count+1
            #                 print("sums is:",sums)
            #                 print("count is:",count)
            #         avgs=sums/count
            #     hr=repo_yearly.objects.filter(service='ampv5_rmt',year=dd[0],device_id=device_id)
            #     if hr:
            #         yr_data=repo_yearly.objects.filter(device_id=device_id).update(device_id=device_id,service='ampv5_rmt',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
            #     else:
            #         yr_data=repo_yearly.objects.create(device_id=device_id,service='ampv5_rmt',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
            #         yr_data.save()
            #     yrdata=treat_ampv5.objects.filter(year=dd[0],device_id=device_id)
            #     count=0
            #     sums=0
            #     avgs = 0
            #     if yrdata:
            #         for yr in yrdata:
            #             yr_d_id=yr.device_id
            #             if yr_d_id == device_id:
            #                 cct=yr.cct
            #                 print("cct is:",cct)
            #                 sums=sums+cct
            #                 count=count+1
            #                 print("sums is:",sums)
            #                 print("count is:",count)
            #         avgs=sums/count
            #     hr=repo_yearly.objects.filter(service='ampv5_cct',year=dd[0],device_id=device_id)
            #     if hr:
            #         yr_data=repo_yearly.objects.filter(device_id=device_id).update(device_id=device_id,service='ampv5_cct',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
            #     else:
            #         yr_data=repo_yearly.objects.create(device_id=device_id,service='ampv5_cct',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
            #         yr_data.save()
                
            # # month
            #     yrdata=treat_ampv5.objects.filter(year=dd[0],month=dd[1],device_id=device_id)
            #     count=0
            #     sums=0
            #     avgs = 0
            #     if yrdata:
            #         for yr in yrdata:
            #             yr_d_id=yr.device_id
            #             if yr_d_id == device_id:
            #                 rmt=yr.rmt
            #                 print("rmt is:",rmt)
            #                 sums=sums+rmt
            #                 count=count+1
            #                 print("sums is:",sums)
            #                 print("count is:",count)
            #         avgs=sums/count
            #     hr=repo_monthly.objects.filter(service='ampv5_rmt',year=dd[0],month=dd[1],device_id=device_id)
            #     if hr:
            #         yr_data=repo_monthly.objects.filter(year=dd[0],month=dd[1],device_id=device_id).update(device_id=device_id,service='ampv5_rmt',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
            #     else:
            #         yr_data=repo_monthly.objects.create(device_id=device_id,service='ampv5_rmt',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
            #         yr_data.save()
            #     yrdata=treat_ampv5.objects.filter(year=dd[0],month=dd[1],device_id=device_id)
            #     count=0
            #     sums=0
            #     avgs = 0
            #     if yrdata:
            #         for yr in yrdata:
            #             yr_d_id=yr.device_id
            #             if yr_d_id == device_id:
            #                 cct=yr.cct
            #                 print("cct is:",cct)
            #                 sums=sums+cct
            #                 count=count+1
            #                 print("sums is:",sums)
            #                 print("count is:",count)
            #         avgs=sums/count
            #     hr=repo_monthly.objects.filter(service='ampv5_cct',year=dd[0],month=dd[1],device_id=device_id)
            #     if hr:
            #         yr_data=repo_monthly.objects.filter(year=dd[0],month=dd[1],device_id=device_id).update(device_id=device_id,service='ampv5_cct',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
            #     else:
            #         yr_data=repo_monthly.objects.create(device_id=device_id,service='ampv5_cct',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
            #         yr_data.save()
            # # day

            #     yrdata=treat_ampv5.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id)
            #     count=0
            #     sums=0
            #     avgs = 0
            #     if yrdata:
            #         for yr in yrdata:
            #             yr_d_id=yr.device_id
            #             if yr_d_id == device_id:
            #                 rmt=yr.rmt
            #                 print("rmt is:",rmt)
            #                 sums=sums+rmt
            #                 count=count+1
            #                 print("sums is:",sums)
            #                 print("count is:",count)
            #         avgs=sums/count
            #     hr=repo_daily.objects.filter(service='ampv5_rmt',year=dd[0],month=dd[1],day=dd[2],device_id=device_id)
            #     if hr:
            #         yr_data=repo_daily.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id).update(device_id=device_id,service='ampv5_rmt',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0],day=dd[2])
            #     else:
            #         yr_data=repo_daily.objects.create(device_id=device_id,service='ampv5_rmt',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0],day=dd[2])
            #         yr_data.save()
            #     yrdata=treat_ampv5.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id)
            #     count=0
            #     sums=0
            #     avgs = 0
            #     if yrdata:
            #         for yr in yrdata:
            #             yr_d_id=yr.device_id
            #             if yr_d_id == device_id:
            #                 cct=yr.cct
            #                 print("cct is:",cct)
            #                 sums=sums+cct
            #                 count=count+1
            #                 print("sums is:",sums)
            #                 print("count is:",count)
            #         avgs=sums/count
            #     hr=repo_daily.objects.filter(service='ampv5_cct',year=dd[0],month=dd[1],day=dd[2],device_id=device_id)
            #     if hr:
            #         yr_data=repo_daily.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id).update(device_id=device_id,service='ampv5_cct',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0],day=dd[2])
            #     else:
            #         yr_data=repo_daily.objects.create(device_id=device_id,service='ampv5_cct',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0],day=dd[2])
            #         yr_data.save()
            #     # hour

            #     yrdata=treat_ampv5.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id)
            #     count=0
            #     sums=0
            #     avgs = 0
            #     if yrdata:
            #         for yr in yrdata:
            #             yr_d_id=yr.device_id
            #             if yr_d_id == device_id:
            #                 rmt=yr.rmt
            #                 print("rmt is:",rmt)
            #                 sums=sums+rmt
            #                 count=count+1
            #                 print("sums is:",sums)
            #                 print("count is:",count)
            #         avgs=sums/count
            #     hr=repo_hourly.objects.filter(service='ampv5_rmt',year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id)
            #     if hr:
            #         yr_data=repo_hourly.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id).update(device_id=device_id,service='ampv5_rmt',sum=sums,count=count,avg=avgs,hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
            #     else:
            #         yr_data=repo_hourly.objects.create(device_id=device_id,service='ampv5_rmt',sum=sums,count=count,avg=avgs,hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
            #         yr_data.save()
            #     yrdata=treat_ampv5.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id)
            #     count=0
            #     sums=0
            #     avgs = 0
            #     if yrdata:
            #         for yr in yrdata:
            #             yr_d_id=yr.device_id
            #             if yr_d_id == device_id:
            #                 cct=yr.cct
            #                 print("cct is:",cct)
            #                 sums=sums+cct
            #                 count=count+1
            #                 print("sums is:",sums)
            #                 print("count is:",count)
            #         avgs=sums/count
            #     hr=repo_hourly.objects.filter(service='ampv5_cct',year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id)
            #     if hr:
            #         yr_data=repo_hourly.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id).update(device_id=device_id,service='ampv5_cct',sum=sums,count=count,avg=avgs,hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
            #     else:
            #         yr_data=repo_hourly.objects.create(device_id=device_id,service='ampv5_cct',sum=sums,count=count,avg=avgs,hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
            #         yr_data.save()
        except Exception as e:
            print("error ==>", e)
            error_message = e
            # global eg
            eg = e
            print("eg is:",eg)
            print("Error massage:",e)
            EchoConsumer.websocket_receive('event','event') 
        try:
            if 'atm'==components:
                # com=cl
                if device_id not in device_idlist:
                     repo_latestdata.objects.create(device_id=device_id,message_type=msg_type,atm=mydata1)
                else:
                    repo_latestobj = repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id, message_type=msg_type, atm=mydata1)

                    get_device_id=repo_latestdata.objects.all()
                    for did in get_device_id:
                        s=str(did.device_id)
                        if device_id == s:
                            atm=did.atm
                    klist = list(atm.keys())
                    print("klist is:",klist)
                    mydatakey = list(mydata1.keys())
                    print("mydatakey:",mydatakey)
                    for k,v in atm.items():
                         if k not in mydatakey:
                              olddata.update({k:v})
                              
                    mydata5=olddata.update(mydata1)    
                    print("old data is:",olddata) # add/update keys in mydata1 to olddata
                    repo_latestobj = repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id, message_type=msg_type, atm=olddata)

                ds=disp_atm.objects.create(device_id=device_id,message_type=msg_type,sts=sts,ndv=ndv,ntt=ntt,nta=nta,tmp=tmp,ntp=ntp,nov=nov,vl1=vl1,vl2=vl2,vl3=vl3,vl4=vl4,re1=re1,re2=re2,re3=re3,re4=re4,year=dd[0],month=dd[1],day=dd[2],hour=dd[3],minit=dd[4],second=dd[5])
                ds.save()
                #hourly
                yrdata=disp_atm.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id)
                count=0
                zerocount=-1
                sumd={}
                sums_ndv=0
                sums_nta=0
                sums_tmp=0
                sums_ntp=0
                sums_nov=0
                sums_vl1=0
                sums_vl2=0
                sums_vl3=0
                sums_vl4=0
                sums_re1=0
                sums_re2=0
                sums_re3=0
                sums_re4=0
                avgs_ndv = 0
                avgs_nta = 0
                avgs_tmp = 0
                avgs_ntp = 0
                avgs_nov = 0
                avgs_vl1 = 0
                avgs_vl2 = 0
                avgs_vl3 = 0
                avgs_vl4 = 0
                avgs_re1 = 0
                avgs_re2 = 0
                avgs_re3 = 0
                avgs_re4 = 0
                if yrdata:
                    for yr in yrdata:
                        yr_d_id=yr.device_id
                        if yr_d_id == device_id:
                            ndv=yr.ndv
                            nta=yr.nta
                            tmp=yr.tmp
                            ntp=yr.ntp
                            nov=yr.nov
                            vl1=yr.vl1
                            vl2=yr.vl2
                            vl3=yr.vl3
                            vl4=yr.vl4
                            re1=yr.re1
                            re2=yr.re2
                            re3=yr.re3
                            re4=yr.re4
                            sums_ndv=sums_ndv+ndv
                            sums_nta=sums_nta+nta
                            sums_tmp=sums_tmp+tmp
                            sums_ntp=sums_ntp+ntp
                            sums_nov=sums_nov+nov
                            sums_vl1=sums_vl1+vl1
                            sums_vl2=sums_vl2+vl2
                            sums_vl3=sums_vl3+vl3
                            sums_vl4=sums_vl4+vl4
                            sums_re1=sums_re1+re1
                            sums_re2=sums_re2+re2
                            sums_re3=sums_re3+re3
                            sums_re4=sums_re4+re4
                            count=count+1
                    avgs_ndv=sums_ndv/count
                    avgs_nta=sums_nta/count
                    avgs_tmp=sums_tmp/count
                    avgs_ntp=sums_ntp/count
                    avgs_nov=sums_nov/count
                    avgs_vl1=sums_vl1/count
                    avgs_vl2=sums_vl2/count
                    avgs_vl3=sums_vl3/count
                    avgs_vl4=sums_vl4/count
                    avgs_re1=sums_re1/count
                    avgs_re2=sums_re2/count
                    avgs_re3=sums_re3/count
                    avgs_re4=sums_re4/count
                hr=atm_repo_hourly.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id)
                if hr:
                    yr_data=atm_repo_hourly.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id).update(device_id=device_id,service='atm',ndv={'sum':sums_ndv,'avg':avgs_ndv,'count':count},nta={'sum':sums_nta,'avg':avgs_nta,'count':count},tmp={'sum':sums_tmp,'avg':avgs_tmp,'count':count},ntp={'sum':sums_ntp,'avg':avgs_ntp,'count':count},nov={'sum':sums_nov,'avg':avgs_nov,'count':count},vl1={'sum':sums_vl1,'avg':avgs_vl1,'count':count},vl2={'sum':sums_vl2,'avg':avgs_vl2,'count':count},vl3={'sum':sums_vl3,'avg':avgs_vl3,'count':count},vl4={'sum':sums_vl4,'avg':avgs_vl4,'count':count},re1={'sum':sums_re1,'avg':avgs_re1,'count':count},re2={'sum':sums_re2,'avg':avgs_re2,'count':count},re3={'sum':sums_re3,'avg':avgs_re3,'count':count},re4={'sum':sums_re4,'avg':avgs_re4,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                else:
                    yr_data=atm_repo_hourly.objects.create(device_id=device_id,service='atm',ndv={'sum':sums_ndv,'avg':avgs_ndv,'count':count},nta={'sum':sums_nta,'avg':avgs_nta,'count':count},tmp={'sum':sums_tmp,'avg':avgs_tmp,'count':count},ntp={'sum':sums_ntp,'avg':avgs_ntp,'count':count},nov={'sum':sums_nov,'avg':avgs_nov,'count':count},vl1={'sum':sums_vl1,'avg':avgs_vl1,'count':count},vl2={'sum':sums_vl2,'avg':avgs_vl2,'count':count},vl3={'sum':sums_vl3,'avg':avgs_vl3,'count':count},vl4={'sum':sums_vl4,'avg':avgs_vl4,'count':count},re1={'sum':sums_re1,'avg':avgs_re1,'count':count},re2={'sum':sums_re2,'avg':avgs_re2,'count':count},re3={'sum':sums_re3,'avg':avgs_re3,'count':count},re4={'sum':sums_re4,'avg':avgs_re4,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                    yr_data.save()

                #day
                yrdata=disp_atm.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id)
                count=0
                zerocount=-1
                sumd={}
                sums_ndv=0
                sums_nta=0
                sums_tmp=0
                sums_ntp=0
                sums_nov=0
                sums_vl1=0
                sums_vl2=0
                sums_vl3=0
                sums_vl4=0
                sums_re1=0
                sums_re2=0
                sums_re3=0
                sums_re4=0
                avgs_ndv = 0
                avgs_nta = 0
                avgs_tmp = 0
                avgs_ntp = 0
                avgs_nov = 0
                avgs_vl1 = 0
                avgs_vl2 = 0
                avgs_vl3 = 0
                avgs_vl4 = 0
                avgs_re1 = 0
                avgs_re2 = 0
                avgs_re3 = 0
                avgs_re4 = 0
                if yrdata:
                    for yr in yrdata:
                        yr_d_id=yr.device_id
                        if yr_d_id == device_id:
                            ndv=yr.ndv
                            nta=yr.nta
                            tmp=yr.tmp
                            ntp=yr.ntp
                            nov=yr.nov
                            vl1=yr.vl1
                            vl2=yr.vl2
                            vl3=yr.vl3
                            vl4=yr.vl4
                            re1=yr.re1
                            re2=yr.re2
                            re3=yr.re3
                            re4=yr.re4
                            sums_ndv=sums_ndv+ndv
                            sums_nta=sums_nta+nta
                            sums_tmp=sums_tmp+tmp
                            sums_ntp=sums_ntp+ntp
                            sums_nov=sums_nov+nov
                            sums_vl1=sums_vl1+vl1
                            sums_vl2=sums_vl2+vl2
                            sums_vl3=sums_vl3+vl3
                            sums_vl4=sums_vl4+vl4
                            sums_re1=sums_re1+re1
                            sums_re2=sums_re2+re2
                            sums_re3=sums_re3+re3
                            sums_re4=sums_re4+re4
                            count=count+1
                    avgs_ndv=sums_ndv/count
                    avgs_nta=sums_nta/count
                    avgs_tmp=sums_tmp/count
                    avgs_ntp=sums_ntp/count
                    avgs_nov=sums_nov/count
                    avgs_vl1=sums_vl1/count
                    avgs_vl2=sums_vl2/count
                    avgs_vl3=sums_vl3/count
                    avgs_vl4=sums_vl4/count
                    avgs_re1=sums_re1/count
                    avgs_re2=sums_re2/count
                    avgs_re3=sums_re3/count
                    avgs_re4=sums_re4/count
                hr=atm_repo_daily.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id)
                if hr:
                    yr_data=atm_repo_daily.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id).update(device_id=device_id,service='atm',ndv={'sum':sums_ndv,'avg':avgs_ndv,'count':count},nta={'sum':sums_nta,'avg':avgs_nta,'count':count},tmp={'sum':sums_tmp,'avg':avgs_tmp,'count':count},ntp={'sum':sums_ntp,'avg':avgs_ntp,'count':count},nov={'sum':sums_nov,'avg':avgs_nov,'count':count},vl1={'sum':sums_vl1,'avg':avgs_vl1,'count':count},vl2={'sum':sums_vl2,'avg':avgs_vl2,'count':count},vl3={'sum':sums_vl3,'avg':avgs_vl3,'count':count},vl4={'sum':sums_vl4,'avg':avgs_vl4,'count':count},re1={'sum':sums_re1,'avg':avgs_re1,'count':count},re2={'sum':sums_re2,'avg':avgs_re2,'count':count},re3={'sum':sums_re3,'avg':avgs_re3,'count':count},re4={'sum':sums_re4,'avg':avgs_re4,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                else:
                    yr_data=atm_repo_daily.objects.create(device_id=device_id,service='atm',ndv={'sum':sums_ndv,'avg':avgs_ndv,'count':count},nta={'sum':sums_nta,'avg':avgs_nta,'count':count},tmp={'sum':sums_tmp,'avg':avgs_tmp,'count':count},ntp={'sum':sums_ntp,'avg':avgs_ntp,'count':count},nov={'sum':sums_nov,'avg':avgs_nov,'count':count},vl1={'sum':sums_vl1,'avg':avgs_vl1,'count':count},vl2={'sum':sums_vl2,'avg':avgs_vl2,'count':count},vl3={'sum':sums_vl3,'avg':avgs_vl3,'count':count},vl4={'sum':sums_vl4,'avg':avgs_vl4,'count':count},re1={'sum':sums_re1,'avg':avgs_re1,'count':count},re2={'sum':sums_re2,'avg':avgs_re2,'count':count},re3={'sum':sums_re3,'avg':avgs_re3,'count':count},re4={'sum':sums_re4,'avg':avgs_re4,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                    yr_data.save()

                #monthly
                yrdata=disp_atm.objects.filter(year=dd[0],month=dd[1],device_id=device_id)
                count=0
                zerocount=-1
                sumd={}
                sums_ndv=0
                sums_nta=0
                sums_tmp=0
                sums_ntp=0
                sums_nov=0
                sums_vl1=0
                sums_vl2=0
                sums_vl3=0
                sums_vl4=0
                sums_re1=0
                sums_re2=0
                sums_re3=0
                sums_re4=0
                avgs_ndv = 0
                avgs_nta = 0
                avgs_tmp = 0
                avgs_ntp = 0
                avgs_nov = 0
                avgs_vl1 = 0
                avgs_vl2 = 0
                avgs_vl3 = 0
                avgs_vl4 = 0
                avgs_re1 = 0
                avgs_re2 = 0
                avgs_re3 = 0
                avgs_re4 = 0
                if yrdata:
                    for yr in yrdata:
                        yr_d_id=yr.device_id
                        if yr_d_id == device_id:
                            ndv=yr.ndv
                            nta=yr.nta
                            tmp=yr.tmp
                            ntp=yr.ntp
                            nov=yr.nov
                            vl1=yr.vl1
                            vl2=yr.vl2
                            vl3=yr.vl3
                            vl4=yr.vl4
                            re1=yr.re1
                            re2=yr.re2
                            re3=yr.re3
                            re4=yr.re4
                            sums_ndv=sums_ndv+ndv
                            sums_nta=sums_nta+nta
                            sums_tmp=sums_tmp+tmp
                            sums_ntp=sums_ntp+ntp
                            sums_nov=sums_nov+nov
                            sums_vl1=sums_vl1+vl1
                            sums_vl2=sums_vl2+vl2
                            sums_vl3=sums_vl3+vl3
                            sums_vl4=sums_vl4+vl4
                            sums_re1=sums_re1+re1
                            sums_re2=sums_re2+re2
                            sums_re3=sums_re3+re3
                            sums_re4=sums_re4+re4
                            count=count+1
                    avgs_ndv=sums_ndv/count
                    avgs_nta=sums_nta/count
                    avgs_tmp=sums_tmp/count
                    avgs_ntp=sums_ntp/count
                    avgs_nov=sums_nov/count
                    avgs_vl1=sums_vl1/count
                    avgs_vl2=sums_vl2/count
                    avgs_vl3=sums_vl3/count
                    avgs_vl4=sums_vl4/count
                    avgs_re1=sums_re1/count
                    avgs_re2=sums_re2/count
                    avgs_re3=sums_re3/count
                    avgs_re4=sums_re4/count
                hr=atm_repo_monthly.objects.filter(year=dd[0],month=dd[1],device_id=device_id)
                if hr:
                    yr_data=atm_repo_monthly.objects.filter(year=dd[0],month=dd[1],device_id=device_id).update(device_id=device_id,service='atm',ndv={'sum':sums_ndv,'avg':avgs_ndv,'count':count},nta={'sum':sums_nta,'avg':avgs_nta,'count':count},tmp={'sum':sums_tmp,'avg':avgs_tmp,'count':count},ntp={'sum':sums_ntp,'avg':avgs_ntp,'count':count},nov={'sum':sums_nov,'avg':avgs_nov,'count':count},vl1={'sum':sums_vl1,'avg':avgs_vl1,'count':count},vl2={'sum':sums_vl2,'avg':avgs_vl2,'count':count},vl3={'sum':sums_vl3,'avg':avgs_vl3,'count':count},vl4={'sum':sums_vl4,'avg':avgs_vl4,'count':count},re1={'sum':sums_re1,'avg':avgs_re1,'count':count},re2={'sum':sums_re2,'avg':avgs_re2,'count':count},re3={'sum':sums_re3,'avg':avgs_re3,'count':count},re4={'sum':sums_re4,'avg':avgs_re4,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                else:
                    yr_data=atm_repo_monthly.objects.create(device_id=device_id,service='atm',ndv={'sum':sums_ndv,'avg':avgs_ndv,'count':count},nta={'sum':sums_nta,'avg':avgs_nta,'count':count},tmp={'sum':sums_tmp,'avg':avgs_tmp,'count':count},ntp={'sum':sums_ntp,'avg':avgs_ntp,'count':count},nov={'sum':sums_nov,'avg':avgs_nov,'count':count},vl1={'sum':sums_vl1,'avg':avgs_vl1,'count':count},vl2={'sum':sums_vl2,'avg':avgs_vl2,'count':count},vl3={'sum':sums_vl3,'avg':avgs_vl3,'count':count},vl4={'sum':sums_vl4,'avg':avgs_vl4,'count':count},re1={'sum':sums_re1,'avg':avgs_re1,'count':count},re2={'sum':sums_re2,'avg':avgs_re2,'count':count},re3={'sum':sums_re3,'avg':avgs_re3,'count':count},re4={'sum':sums_re4,'avg':avgs_re4,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                    yr_data.save()

                #yearly
                yrdata=disp_atm.objects.filter(year=dd[0],device_id=device_id)
                count=0
                zerocount=-1
                sumd={}
                sums_ndv=0
                sums_nta=0
                sums_tmp=0
                sums_ntp=0
                sums_nov=0
                sums_vl1=0
                sums_vl2=0
                sums_vl3=0
                sums_vl4=0
                sums_re1=0
                sums_re2=0
                sums_re3=0
                sums_re4=0
                avgs_ndv = 0
                avgs_nta = 0
                avgs_tmp = 0
                avgs_ntp = 0
                avgs_nov = 0
                avgs_vl1 = 0
                avgs_vl2 = 0
                avgs_vl3 = 0
                avgs_vl4 = 0
                avgs_re1 = 0
                avgs_re2 = 0
                avgs_re3 = 0
                avgs_re4 = 0
                if yrdata:
                    for yr in yrdata:
                        yr_d_id=yr.device_id
                        if yr_d_id == device_id:
                            ndv=yr.ndv
                            nta=yr.nta
                            tmp=yr.tmp
                            ntp=yr.ntp
                            nov=yr.nov
                            vl1=yr.vl1
                            vl2=yr.vl2
                            vl3=yr.vl3
                            vl4=yr.vl4
                            re1=yr.re1
                            re2=yr.re2
                            re3=yr.re3
                            re4=yr.re4
                            sums_ndv=sums_ndv+ndv
                            sums_nta=sums_nta+nta
                            sums_tmp=sums_tmp+tmp
                            sums_ntp=sums_ntp+ntp
                            sums_nov=sums_nov+nov
                            sums_vl1=sums_vl1+vl1
                            sums_vl2=sums_vl2+vl2
                            sums_vl3=sums_vl3+vl3
                            sums_vl4=sums_vl4+vl4
                            sums_re1=sums_re1+re1
                            sums_re2=sums_re2+re2
                            sums_re3=sums_re3+re3
                            sums_re4=sums_re4+re4
                            count=count+1
                    avgs_ndv=sums_ndv/count
                    avgs_nta=sums_nta/count
                    avgs_tmp=sums_tmp/count
                    avgs_ntp=sums_ntp/count
                    avgs_nov=sums_nov/count
                    avgs_vl1=sums_vl1/count
                    avgs_vl2=sums_vl2/count
                    avgs_vl3=sums_vl3/count
                    avgs_vl4=sums_vl4/count
                    avgs_re1=sums_re1/count
                    avgs_re2=sums_re2/count
                    avgs_re3=sums_re3/count
                    avgs_re4=sums_re4/count
                hr=atm_repo_yearly.objects.filter(year=dd[0],device_id=device_id)
                if hr:
                    yr_data=atm_repo_yearly.objects.filter(year=dd[0],device_id=device_id).update(device_id=device_id,service='atm',ndv={'sum':sums_ndv,'avg':avgs_ndv,'count':count},nta={'sum':sums_nta,'avg':avgs_nta,'count':count},tmp={'sum':sums_tmp,'avg':avgs_tmp,'count':count},ntp={'sum':sums_ntp,'avg':avgs_ntp,'count':count},nov={'sum':sums_nov,'avg':avgs_nov,'count':count},vl1={'sum':sums_vl1,'avg':avgs_vl1,'count':count},vl2={'sum':sums_vl2,'avg':avgs_vl2,'count':count},vl3={'sum':sums_vl3,'avg':avgs_vl3,'count':count},vl4={'sum':sums_vl4,'avg':avgs_vl4,'count':count},re1={'sum':sums_re1,'avg':avgs_re1,'count':count},re2={'sum':sums_re2,'avg':avgs_re2,'count':count},re3={'sum':sums_re3,'avg':avgs_re3,'count':count},re4={'sum':sums_re4,'avg':avgs_re4,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                else:
                    yr_data=atm_repo_yearly.objects.create(device_id=device_id,service='atm',ndv={'sum':sums_ndv,'avg':avgs_ndv,'count':count},nta={'sum':sums_nta,'avg':avgs_nta,'count':count},tmp={'sum':sums_tmp,'avg':avgs_tmp,'count':count},ntp={'sum':sums_ntp,'avg':avgs_ntp,'count':count},nov={'sum':sums_nov,'avg':avgs_nov,'count':count},vl1={'sum':sums_vl1,'avg':avgs_vl1,'count':count},vl2={'sum':sums_vl2,'avg':avgs_vl2,'count':count},vl3={'sum':sums_vl3,'avg':avgs_vl3,'count':count},vl4={'sum':sums_vl4,'avg':avgs_vl4,'count':count},re1={'sum':sums_re1,'avg':avgs_re1,'count':count},re2={'sum':sums_re2,'avg':avgs_re2,'count':count},re3={'sum':sums_re3,'avg':avgs_re3,'count':count},re4={'sum':sums_re4,'avg':avgs_re4,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                    yr_data.save()

            #     yrdata=disp_atm.objects.filter(year=dd[0],device_id=device_id)
            #     count=0
            #     sums=0
            #     avgs = 0
            #     if yrdata:
            #         for yr in yrdata:
            #             yr_d_id=yr.device_id
            #             if yr_d_id == device_id:
            #                 ndv=yr.ndv
            #                 print("ndv is:",ndv)
            #                 sums=sums+ndv
            #                 count=count+1
            #                 print("sums is:",sums)
            #                 print("count is:",count)
            #         avgs=sums/count
            #     hr=repo_yearly.objects.filter(year=dd[0],device_id=device_id)
            #     if hr:
            #         yr_data=repo_yearly.objects.filter(device_id=device_id).update(device_id=device_id,service='atm_ndv',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
            #     else:
            #         yr_data=repo_yearly.objects.create(device_id=device_id,service='atm_ndv',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
            #         yr_data.save()
                               

            #     yrdata=disp_atm.objects.filter(year=dd[0],device_id=device_id)
            #     count=0
            #     sums=0
            #     avgs = 0
            #     if yrdata:
            #         for yr in yrdata:
            #             yr_d_id=yr.device_id
            #             if yr_d_id == device_id:
            #                 nta=yr.nta
            #                 print("nta is:",nta)
            #                 sums=sums+nta
            #                 count=count+1
            #                 print("sums is:",sums)
            #                 print("count is:",count)
            #         avgs=sums/count
            #     hr=repo_yearly.objects.filter(year=dd[0],device_id=device_id)
            #     if hr:
            #         yr_data=repo_yearly.objects.filter(device_id=device_id).update(device_id=device_id,service='atm_nta',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
            #     else:
            #         yr_data=repo_yearly.objects.create(device_id=device_id,service='atm_nta',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
            #         yr_data.save()
                               

            #     yrdata=disp_atm.objects.filter(year=dd[0],device_id=device_id)
            #     count=0
            #     sums=0
            #     avgs = 0
            #     if yrdata:
            #         for yr in yrdata:
            #             yr_d_id=yr.device_id
            #             if yr_d_id == device_id:
            #                 tmp=yr.tmp
            #                 print("tmp is:",tmp)
            #                 sums=sums+tmp
            #                 count=count+1
            #                 print("sums is:",sums)
            #                 print("count is:",count)
            #         avgs=sums/count
            #     hr=repo_yearly.objects.filter(year=dd[0],device_id=device_id)
            #     if hr:
            #         yr_data=repo_yearly.objects.filter(device_id=device_id).update(device_id=device_id,service='atm_tmp',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
            #     else:
            #         yr_data=repo_yearly.objects.create(device_id=device_id,service='atm_tmp',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
            #         yr_data.save()
                               
            #  #    month

            #     yrdata=disp_atm.objects.filter(year=dd[0],month=dd[1],device_id=device_id)
            #     count=0
            #     sums=0
            #     avgs = 0
            #     if yrdata:
            #         for yr in yrdata:
            #             yr_d_id=yr.device_id
            #             if yr_d_id == device_id:
            #                 ndv=yr.ndv
            #                 print("ndv is:",ndv)
            #                 sums=sums+ndv
            #                 count=count+1
            #                 print("sums is:",sums)
            #                 print("count is:",count)
            #         avgs=sums/count
            #     hr=repo_monthly.objects.filter(year=dd[0],month=dd[1],device_id=device_id)
            #     if hr:
            #         yr_data=repo_monthly.objects.filter(year=dd[0],month=dd[1],device_id=device_id).update(device_id=device_id,service='atm_ndv',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
            #     else:
            #         yr_data=repo_monthly.objects.create(device_id=device_id,service='atm_ndv',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
            #         yr_data.save()
            #     yrdata=disp_atm.objects.filter(year=dd[0],month=dd[1],device_id=device_id)
            #     count=0
            #     sums=0
            #     avgs = 0
            #     if yrdata:
            #         for yr in yrdata:
            #             yr_d_id=yr.device_id
            #             if yr_d_id == device_id:
            #                 nta=yr.nta
            #                 print("nta is:",nta)
            #                 sums=sums+nta
            #                 count=count+1
            #                 print("sums is:",sums)
            #                 print("count is:",count)
            #         avgs=sums/count
            #     hr=repo_monthly.objects.filter(year=dd[0],month=dd[1],device_id=device_id)
            #     if hr:
            #         yr_data=repo_monthly.objects.filter(year=dd[0],month=dd[1],device_id=device_id).update(device_id=device_id,service='atm_nta',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
            #     else:
            #         yr_data=repo_monthly.objects.create(device_id=device_id,service='atm_nta',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
            #         yr_data.save()
            #     yrdata=disp_atm.objects.filter(year=dd[0],month=dd[1],device_id=device_id)
            #     count=0
            #     sums=0
            #     avgs = 0
            #     if yrdata:
            #         for yr in yrdata:
            #             yr_d_id=yr.device_id
            #             if yr_d_id == device_id:
            #                 tmp=yr.tmp
            #                 print("tmp is:",tmp)
            #                 sums=sums+tmp
            #                 count=count+1
            #                 print("sums is:",sums)
            #                 print("count is:",count)
            #         avgs=sums/count
            #     hr=repo_monthly.objects.filter(year=dd[0],month=dd[1],device_id=device_id)
            #     if hr:
            #         yr_data=repo_monthly.objects.filter(year=dd[0],month=dd[1],device_id=device_id).update(device_id=device_id,service='atm_tmp',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
            #     else:
            #         yr_data=repo_monthly.objects.create(device_id=device_id,service='atm_tmp',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
            #         yr_data.save()
                
            #     # day
            #     yrdata=disp_atm.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id)
            #     count=0
            #     sums=0
            #     avgs = 0
            #     if yrdata:
            #         for yr in yrdata:
            #             yr_d_id=yr.device_id
            #             if yr_d_id == device_id:
            #                 ndv=yr.ndv
            #                 print("ndv is:",ndv)
            #                 sums=sums+ndv
            #                 count=count+1
            #                 print("sums is:",sums)
            #                 print("count is:",count)
            #         avgs=sums/count
            #     hr=repo_daily.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id)
            #     if hr:
            #         yr_data=repo_daily.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id).update(device_id=device_id,service='atm_ndv',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0],day=dd[2])
            #     else:
            #         yr_data=repo_daily.objects.create(device_id=device_id,service='atm_ndv',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0],day=dd[2])
            #         yr_data.save()
            #     yrdata=disp_atm.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id)
            #     count=0
            #     sums=0
            #     avgs = 0
            #     if yrdata:
            #         for yr in yrdata:
            #             yr_d_id=yr.device_id
            #             if yr_d_id == device_id:
            #                 nta=yr.nta
            #                 print("nta is:",nta)
            #                 sums=sums+nta
            #                 count=count+1
            #                 print("sums is:",sums)
            #                 print("count is:",count)
            #         avgs=sums/count
            #     hr=repo_daily.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id)
            #     if hr:
            #         yr_data=repo_daily.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id).update(device_id=device_id,service='atm_nta',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0],day=dd[2])
            #     else:
            #         yr_data=repo_daily.objects.create(device_id=device_id,service='atm_nta',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0],day=dd[2])
            #         yr_data.save()
            #     yrdata=disp_atm.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id)
            #     count=0
            #     sums=0
            #     avgs = 0
            #     if yrdata:
            #         for yr in yrdata:
            #             yr_d_id=yr.device_id
            #             if yr_d_id == device_id:
            #                 tmp=yr.tmp
            #                 print("tmp is:",tmp)
            #                 sums=sums+tmp
            #                 count=count+1
            #                 print("sums is:",sums)
            #                 print("count is:",count)
            #         avgs=sums/count
            #     hr=repo_daily.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id)
            #     if hr:
            #         yr_data=repo_daily.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id).update(device_id=device_id,service='atm_tmp',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0],day=dd[2])
            #     else:
            #         yr_data=repo_daily.objects.create(device_id=device_id,service='atm_tmp',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0],day=dd[2])
            #         yr_data.save()
            #     # hour

            #     yrdata=disp_atm.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id)
            #     count=0
            #     sums=0
            #     avgs = 0
            #     if yrdata:
            #         for yr in yrdata:
            #             yr_d_id=yr.device_id
            #             if yr_d_id == device_id:
            #                 ndv=yr.ndv
            #                 print("ndv is:",ndv)
            #                 sums=sums+ndv
            #                 count=count+1
            #                 print("sums is:",sums)
            #                 print("count is:",count)
            #         avgs=sums/count
            #     hr=repo_hourly.objects.filter(service='atm_ndv',year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id)
            #     if hr:
            #         yr_data=repo_hourly.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id).update(device_id=device_id,service='atm_ndv',sum=sums,count=count,avg=avgs,hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
            #     else:
            #         yr_data=repo_hourly.objects.create(device_id=device_id,service='atm_ndv',sum=sums,count=count,avg=avgs,hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
            #         yr_data.save()

            #     yrdata=disp_atm.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id)
            #     count=0
            #     sums=0
            #     avgs = 0
            #     if yrdata:
            #         for yr in yrdata:
            #             yr_d_id=yr.device_id
            #             if yr_d_id == device_id:
            #                 nta=yr.nta
            #                 print("nta is:",nta)
            #                 sums=sums+nta
            #                 count=count+1
            #                 print("sums is:",sums)
            #                 print("count is:",count)
            #         avgs=sums/count
            #     hr=repo_hourly.objects.filter(service='atm_nta',year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id)
            #     if hr:
            #         yr_data=repo_hourly.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id).update(device_id=device_id,service='atm_nta',sum=sums,count=count,avg=avgs,hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
            #     else:
            #         yr_data=repo_hourly.objects.create(device_id=device_id,service='atm_nta',sum=sums,count=count,avg=avgs,hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
            #         yr_data.save()

            #     yrdata=disp_atm.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id)
            #     count=0
            #     sums=0
            #     avgs = 0
            #     if yrdata:
            #         for yr in yrdata:
            #             yr_d_id=yr.device_id
            #             if yr_d_id == device_id:
            #                 tmp=yr.tmp
            #                 print("tmp is:",tmp)
            #                 sums=sums+tmp
            #                 count=count+1
            #                 print("sums is:",sums)
            #                 print("count is:",count)
            #         avgs=sums/count
            #     hr=repo_hourly.objects.filter(service='atm_tmp',year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id)
            #     if hr:
            #         yr_data=repo_hourly.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id).update(device_id=device_id,service='atm_tmp',sum=sums,count=count,avg=avgs,hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
            #     else:
            #         yr_data=repo_hourly.objects.create(device_id=device_id,service='atm_tmp',sum=sums,count=count,avg=avgs,hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
            #         yr_data.save()
        except Exception as e:
            print("error ==>", e)
            error_message = e
            # global eg
            eg = e
            print("eg is:",eg)
            print("Error massage:",e)
            EchoConsumer.websocket_receive('event','event')        
        if 'tap1'==components:
                # com=cl
                if device_id not in device_idlist:
                     repo_latestdata.objects.create(device_id=device_id,message_type=msg_type,tap1=mydata1)
                else:

                    # repo_latestobj = repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id, message_type=msg_type, flowsen=mydata1)
                    repo_latestobj = repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id, message_type=msg_type, tap1=mydata1)

                    get_device_id=repo_latestdata.objects.all()
                    for did in get_device_id:
                        s=str(did.device_id)
                        if device_id == s:
                            tap1=did.tap1
                    klist = list(tap1.keys())
                    print("klist is:",klist)
                    mydatakey = list(mydata1.keys())
                    print("mydatakey:",mydatakey)
                    for k,v in tap1.items():
                         if k not in mydatakey:
                              olddata.update({k:v})
                              
                    mydata5=olddata.update(mydata1)    
                    print("old data is:",olddata) # add/update keys in mydata1 to olddata
                    repo_latestobj = repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id, message_type=msg_type, tap1=olddata)

                # repo_latestobj=repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id,message_type=msg_type,tap1=mydata1)
                # repo_latestobj.save()  
                ds=disp_tap1.objects.create(device_id=device_id,message_type=msg_type,p1=p1,p2=p2,p3=p3,p4=p4,year=dd[0],month=dd[1],day=dd[2],hour=dd[3],minit=dd[4],second=dd[5])
                ds.save()
                #hourly
                yrdata=disp_tap1.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id)
                count=0
                zerocount=-1
                sumd={}
                sums_p1=0
                sums_p2=0
                sums_p3=0
                sums_p4=0
                avgs_p1 = 0
                avgs_p2 = 0
                avgs_p3 = 0
                avgs_p4 = 0
                if yrdata:
                    for yr in yrdata:
                        yr_d_id=yr.device_id
                        if yr_d_id == device_id:
                            p1=yr.p1
                            p2=yr.p2
                            p3=yr.p3
                            p4=yr.p4
                            sums_p1=sums_p1+p1
                            sums_p2=sums_p2+p2
                            sums_p3=sums_p3+p3
                            sums_p4=sums_p4+p4
                            count=count+1
                    avgs_p1=sums_p1/count
                    avgs_p2=sums_p2/count
                    avgs_p3=sums_p3/count
                    avgs_p4=sums_p4/count
                hr=tap1_repo_hourly.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id)
                if hr:
                    yr_data=tap1_repo_hourly.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id).update(device_id=device_id,service='tap1',p1={'sum':sums_p1,'avg':avgs_p1,'count':count},p2={'sum':sums_p2,'avg':avgs_p2,'count':count},p3={'sum':sums_p3,'avg':avgs_p3,'count':count},p4={'sum':sums_p4,'avg':avgs_p4,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                else:
                    yr_data=tap1_repo_hourly.objects.create(device_id=device_id,service='tap1',p1={'sum':sums_p1,'avg':avgs_p1,'count':count},p2={'sum':sums_p2,'avg':avgs_p2,'count':count},p3={'sum':sums_p3,'avg':avgs_p3,'count':count},p4={'sum':sums_p4,'avg':avgs_p4,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                    yr_data.save()

                #daily
                yrdata=disp_tap1.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id)
                count=0
                zerocount=-1
                sumd={}
                sums_p1=0
                sums_p2=0
                sums_p3=0
                sums_p4=0
                avgs_p1 = 0
                avgs_p2 = 0
                avgs_p3 = 0
                avgs_p4 = 0
                if yrdata:
                    for yr in yrdata:
                        yr_d_id=yr.device_id
                        if yr_d_id == device_id:
                            p1=yr.p1
                            p2=yr.p2
                            p3=yr.p3
                            p4=yr.p4
                            sums_p1=sums_p1+p1
                            sums_p2=sums_p2+p2
                            sums_p3=sums_p3+p3
                            sums_p4=sums_p4+p4
                            count=count+1
                    avgs_p1=sums_p1/count
                    avgs_p2=sums_p2/count
                    avgs_p3=sums_p3/count
                    avgs_p4=sums_p4/count
                hr=tap1_repo_daily.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id)
                if hr:
                    yr_data=tap1_repo_daily.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id).update(device_id=device_id,service='tap1',p1={'sum':sums_p1,'avg':avgs_p1,'count':count},p2={'sum':sums_p2,'avg':avgs_p2,'count':count},p3={'sum':sums_p3,'avg':avgs_p3,'count':count},p4={'sum':sums_p4,'avg':avgs_p4,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                else:
                    yr_data=tap1_repo_daily.objects.create(device_id=device_id,service='tap1',p1={'sum':sums_p1,'avg':avgs_p1,'count':count},p2={'sum':sums_p2,'avg':avgs_p2,'count':count},p3={'sum':sums_p3,'avg':avgs_p3,'count':count},p4={'sum':sums_p4,'avg':avgs_p4,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                    yr_data.save()
                #monthly
                yrdata=disp_tap1.objects.filter(year=dd[0],month=dd[1],device_id=device_id)
                count=0
                zerocount=-1
                sumd={}
                sums_p1=0
                sums_p2=0
                sums_p3=0
                sums_p4=0
                avgs_p1 = 0
                avgs_p2 = 0
                avgs_p3 = 0
                avgs_p4 = 0
                if yrdata:
                    for yr in yrdata:
                        yr_d_id=yr.device_id
                        if yr_d_id == device_id:
                            p1=yr.p1
                            p2=yr.p2
                            p3=yr.p3
                            p4=yr.p4
                            sums_p1=sums_p1+p1
                            sums_p2=sums_p2+p2
                            sums_p3=sums_p3+p3
                            sums_p4=sums_p4+p4
                            count=count+1
                    avgs_p1=sums_p1/count
                    avgs_p2=sums_p2/count
                    avgs_p3=sums_p3/count
                    avgs_p4=sums_p4/count
                hr=tap1_repo_monthly.objects.filter(year=dd[0],month=dd[1],device_id=device_id)
                if hr:
                    yr_data=tap1_repo_monthly.objects.filter(year=dd[0],month=dd[1],device_id=device_id).update(device_id=device_id,service='tap1',p1={'sum':sums_p1,'avg':avgs_p1,'count':count},p2={'sum':sums_p2,'avg':avgs_p2,'count':count},p3={'sum':sums_p3,'avg':avgs_p3,'count':count},p4={'sum':sums_p4,'avg':avgs_p4,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                else:
                    yr_data=tap1_repo_monthly.objects.create(device_id=device_id,service='tap1',p1={'sum':sums_p1,'avg':avgs_p1,'count':count},p2={'sum':sums_p2,'avg':avgs_p2,'count':count},p3={'sum':sums_p3,'avg':avgs_p3,'count':count},p4={'sum':sums_p4,'avg':avgs_p4,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                    yr_data.save()
                #yearly
                yrdata=disp_tap1.objects.filter(year=dd[0],device_id=device_id)
                count=0
                zerocount=-1
                sumd={}
                sums_p1=0
                sums_p2=0
                sums_p3=0
                sums_p4=0
                avgs_p1 = 0
                avgs_p2 = 0
                avgs_p3 = 0
                avgs_p4 = 0
                if yrdata:
                    for yr in yrdata:
                        yr_d_id=yr.device_id
                        if yr_d_id == device_id:
                            p1=yr.p1
                            p2=yr.p2
                            p3=yr.p3
                            p4=yr.p4
                            sums_p1=sums_p1+p1
                            sums_p2=sums_p2+p2
                            sums_p3=sums_p3+p3
                            sums_p4=sums_p4+p4
                            count=count+1
                    avgs_p1=sums_p1/count
                    avgs_p2=sums_p2/count
                    avgs_p3=sums_p3/count
                    avgs_p4=sums_p4/count
                hr=tap1_repo_yearly.objects.filter(year=dd[0],device_id=device_id)
                if hr:
                    yr_data=tap1_repo_yearly.objects.filter(year=dd[0],device_id=device_id).update(device_id=device_id,service='tap1',p1={'sum':sums_p1,'avg':avgs_p1,'count':count},p2={'sum':sums_p2,'avg':avgs_p2,'count':count},p3={'sum':sums_p3,'avg':avgs_p3,'count':count},p4={'sum':sums_p4,'avg':avgs_p4,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                else:
                    yr_data=tap1_repo_yearly.objects.create(device_id=device_id,service='tap1',p1={'sum':sums_p1,'avg':avgs_p1,'count':count},p2={'sum':sums_p2,'avg':avgs_p2,'count':count},p3={'sum':sums_p3,'avg':avgs_p3,'count':count},p4={'sum':sums_p4,'avg':avgs_p4,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                    yr_data.save()
        if 'tap2'==components:
                # com=cl
                if device_id not in device_idlist:
                     repo_latestdata.objects.create(device_id=device_id,message_type=msg_type,tap2=mydata1)
                else:
                    repo_latestobj = repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id, message_type=msg_type, tap2=mydata1)

                    get_device_id=repo_latestdata.objects.all()
                    for did in get_device_id:
                        s=str(did.device_id)
                        if device_id == s:
                            tap2=did.tap2
                    klist = list(tap2.keys())
                    print("klist is:",klist)
                    mydatakey = list(mydata1.keys())
                    print("mydatakey:",mydatakey)
                    for k,v in tap2.items():
                         if k not in mydatakey:
                              olddata.update({k:v})
                              
                    mydata5=olddata.update(mydata1)    
                    print("old data is:",olddata) # add/update keys in mydata1 to olddata
                    repo_latestobj = repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id, message_type=msg_type, tap2=olddata)

                # repo_latestobj=repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id,message_type=msg_type,tap2=mydata1)
                # repo_latestobj.save()
                ds=disp_tap2.objects.create(device_id=device_id,message_type=msg_type,p1=p1,p2=p2,p3=p3,p4=p4,year=dd[0],month=dd[1],day=dd[2],hour=dd[3],minit=dd[4],second=dd[5])
                ds.save()
                #hourly
                yrdata=disp_tap2.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id)
                count=0
                zerocount=-1
                sumd={}
                sums_p1=0
                sums_p2=0
                sums_p3=0
                sums_p4=0
                avgs_p1 = 0
                avgs_p2 = 0
                avgs_p3 = 0
                avgs_p4 = 0
                if yrdata:
                    for yr in yrdata:
                        yr_d_id=yr.device_id
                        if yr_d_id == device_id:
                            p1=yr.p1
                            p2=yr.p2
                            p3=yr.p3
                            p4=yr.p4
                            sums_p1=sums_p1+p1
                            sums_p2=sums_p2+p2
                            sums_p3=sums_p3+p3
                            sums_p4=sums_p4+p4
                            count=count+1
                    avgs_p1=sums_p1/count
                    avgs_p2=sums_p2/count
                    avgs_p3=sums_p3/count
                    avgs_p4=sums_p4/count
                hr=tap2_repo_hourly.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id)
                if hr:
                    yr_data=tap2_repo_hourly.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id).update(device_id=device_id,service='tap2',p1={'sum':sums_p1,'avg':avgs_p1,'count':count},p2={'sum':sums_p2,'avg':avgs_p2,'count':count},p3={'sum':sums_p3,'avg':avgs_p3,'count':count},p4={'sum':sums_p4,'avg':avgs_p4,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                else:
                    yr_data=tap2_repo_hourly.objects.create(device_id=device_id,service='tap2',p1={'sum':sums_p1,'avg':avgs_p1,'count':count},p2={'sum':sums_p2,'avg':avgs_p2,'count':count},p3={'sum':sums_p3,'avg':avgs_p3,'count':count},p4={'sum':sums_p4,'avg':avgs_p4,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                    yr_data.save()

                #daily
                yrdata=disp_tap2.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id)
                count=0
                zerocount=-1
                sumd={}
                sums_p1=0
                sums_p2=0
                sums_p3=0
                sums_p4=0
                avgs_p1 = 0
                avgs_p2 = 0
                avgs_p3 = 0
                avgs_p4 = 0
                if yrdata:
                    for yr in yrdata:
                        yr_d_id=yr.device_id
                        if yr_d_id == device_id:
                            p1=yr.p1
                            p2=yr.p2
                            p3=yr.p3
                            p4=yr.p4
                            sums_p1=sums_p1+p1
                            sums_p2=sums_p2+p2
                            sums_p3=sums_p3+p3
                            sums_p4=sums_p4+p4
                            count=count+1
                    avgs_p1=sums_p1/count
                    avgs_p2=sums_p2/count
                    avgs_p3=sums_p3/count
                    avgs_p4=sums_p4/count
                hr=tap2_repo_daily.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id)
                if hr:
                    yr_data=tap2_repo_daily.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id).update(device_id=device_id,service='tap2',p1={'sum':sums_p1,'avg':avgs_p1,'count':count},p2={'sum':sums_p2,'avg':avgs_p2,'count':count},p3={'sum':sums_p3,'avg':avgs_p3,'count':count},p4={'sum':sums_p4,'avg':avgs_p4,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                else:
                    yr_data=tap2_repo_daily.objects.create(device_id=device_id,service='tap2',p1={'sum':sums_p1,'avg':avgs_p1,'count':count},p2={'sum':sums_p2,'avg':avgs_p2,'count':count},p3={'sum':sums_p3,'avg':avgs_p3,'count':count},p4={'sum':sums_p4,'avg':avgs_p4,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                    yr_data.save()
                #monthly
                yrdata=disp_tap2.objects.filter(year=dd[0],month=dd[1],device_id=device_id)
                count=0
                zerocount=-1
                sumd={}
                sums_p1=0
                sums_p2=0
                sums_p3=0
                sums_p4=0
                avgs_p1 = 0
                avgs_p2 = 0
                avgs_p3 = 0
                avgs_p4 = 0
                if yrdata:
                    for yr in yrdata:
                        yr_d_id=yr.device_id
                        if yr_d_id == device_id:
                            p1=yr.p1
                            p2=yr.p2
                            p3=yr.p3
                            p4=yr.p4
                            sums_p1=sums_p1+p1
                            sums_p2=sums_p2+p2
                            sums_p3=sums_p3+p3
                            sums_p4=sums_p4+p4
                            count=count+1
                    avgs_p1=sums_p1/count
                    avgs_p2=sums_p2/count
                    avgs_p3=sums_p3/count
                    avgs_p4=sums_p4/count
                hr=tap2_repo_monthly.objects.filter(year=dd[0],month=dd[1],device_id=device_id)
                if hr:
                    yr_data=tap2_repo_monthly.objects.filter(year=dd[0],month=dd[1],device_id=device_id).update(device_id=device_id,service='tap2',p1={'sum':sums_p1,'avg':avgs_p1,'count':count},p2={'sum':sums_p2,'avg':avgs_p2,'count':count},p3={'sum':sums_p3,'avg':avgs_p3,'count':count},p4={'sum':sums_p4,'avg':avgs_p4,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                else:
                    yr_data=tap2_repo_monthly.objects.create(device_id=device_id,service='tap2',p1={'sum':sums_p1,'avg':avgs_p1,'count':count},p2={'sum':sums_p2,'avg':avgs_p2,'count':count},p3={'sum':sums_p3,'avg':avgs_p3,'count':count},p4={'sum':sums_p4,'avg':avgs_p4,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                    yr_data.save()
                #yearly
                yrdata=disp_tap2.objects.filter(year=dd[0],device_id=device_id)
                count=0
                zerocount=-1
                sumd={}
                sums_p1=0
                sums_p2=0
                sums_p3=0
                sums_p4=0
                avgs_p1 = 0
                avgs_p2 = 0
                avgs_p3 = 0
                avgs_p4 = 0
                if yrdata:
                    for yr in yrdata:
                        yr_d_id=yr.device_id
                        if yr_d_id == device_id:
                            p1=yr.p1
                            p2=yr.p2
                            p3=yr.p3
                            p4=yr.p4
                            sums_p1=sums_p1+p1
                            sums_p2=sums_p2+p2
                            sums_p3=sums_p3+p3
                            sums_p4=sums_p4+p4
                            count=count+1
                    avgs_p1=sums_p1/count
                    avgs_p2=sums_p2/count
                    avgs_p3=sums_p3/count
                    avgs_p4=sums_p4/count
                hr=tap2_repo_yearly.objects.filter(year=dd[0],device_id=device_id)
                if hr:
                    yr_data=tap2_repo_yearly.objects.filter(year=dd[0],device_id=device_id).update(device_id=device_id,service='tap2',p1={'sum':sums_p1,'avg':avgs_p1,'count':count},p2={'sum':sums_p2,'avg':avgs_p2,'count':count},p3={'sum':sums_p3,'avg':avgs_p3,'count':count},p4={'sum':sums_p4,'avg':avgs_p4,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                else:
                    yr_data=tap2_repo_yearly.objects.create(device_id=device_id,service='tap2',p1={'sum':sums_p1,'avg':avgs_p1,'count':count},p2={'sum':sums_p2,'avg':avgs_p2,'count':count},p3={'sum':sums_p3,'avg':avgs_p3,'count':count},p4={'sum':sums_p4,'avg':avgs_p4,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                    yr_data.save()
        if 'tap3'==components:
                # com=cl
                if device_id not in device_idlist:
                     repo_latestdata.objects.create(device_id=device_id,message_type=msg_type,tap3=mydata1)
                else:
                    repo_latestobj = repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id, message_type=msg_type, tap3=mydata1)

                    get_device_id=repo_latestdata.objects.all()
                    for did in get_device_id:
                        s=str(did.device_id)
                        if device_id == s:
                            tap3=did.tap3
                    
                    klist = list(tap3.keys())
                    print("klist is:",klist)
                    mydatakey = list(mydata1.keys())
                    print("mydatakey:",mydatakey)
                    for k,v in tap3.items():
                         if k not in mydatakey:
                              olddata.update({k:v})
                              
                    mydata5=olddata.update(mydata1)    
                    print("old data is:",olddata) # add/update keys in mydata1 to olddata
                    repo_latestobj = repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id, message_type=msg_type, tap3=olddata)

                # repo_latestobj=repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id,message_type=msg_type,tap3=mydata1)
                # repo_latestobj.save()   
                ds=disp_tap3.objects.create(device_id=device_id,message_type=msg_type,p1=p1,p2=p2,p3=p3,p4=p4,year=dd[0],month=dd[1],day=dd[2],hour=dd[3],minit=dd[4],second=dd[5])
                ds.save()
                #hourly
                yrdata=disp_tap3.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id)
                count=0
                zerocount=-1
                sumd={}
                sums_p1=0
                sums_p2=0
                sums_p3=0
                sums_p4=0
                avgs_p1 = 0
                avgs_p2 = 0
                avgs_p3 = 0
                avgs_p4 = 0
                if yrdata:
                    for yr in yrdata:
                        yr_d_id=yr.device_id
                        if yr_d_id == device_id:
                            p1=yr.p1
                            p2=yr.p2
                            p3=yr.p3
                            p4=yr.p4
                            sums_p1=sums_p1+p1
                            sums_p2=sums_p2+p2
                            sums_p3=sums_p3+p3
                            sums_p4=sums_p4+p4
                            count=count+1
                    avgs_p1=sums_p1/count
                    avgs_p2=sums_p2/count
                    avgs_p3=sums_p3/count
                    avgs_p4=sums_p4/count
                hr=tap3_repo_hourly.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id)
                if hr:
                    yr_data=tap3_repo_hourly.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id).update(device_id=device_id,service='tap3',p1={'sum':sums_p1,'avg':avgs_p1,'count':count},p2={'sum':sums_p2,'avg':avgs_p2,'count':count},p3={'sum':sums_p3,'avg':avgs_p3,'count':count},p4={'sum':sums_p4,'avg':avgs_p4,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                else:
                    yr_data=tap3_repo_hourly.objects.create(device_id=device_id,service='tap3',p1={'sum':sums_p1,'avg':avgs_p1,'count':count},p2={'sum':sums_p2,'avg':avgs_p2,'count':count},p3={'sum':sums_p3,'avg':avgs_p3,'count':count},p4={'sum':sums_p4,'avg':avgs_p4,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                    yr_data.save()

                #daily
                yrdata=disp_tap3.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id)
                count=0
                zerocount=-1
                sumd={}
                sums_p1=0
                sums_p2=0
                sums_p3=0
                sums_p4=0
                avgs_p1 = 0
                avgs_p2 = 0
                avgs_p3 = 0
                avgs_p4 = 0
                if yrdata:
                    for yr in yrdata:
                        yr_d_id=yr.device_id
                        if yr_d_id == device_id:
                            p1=yr.p1
                            p2=yr.p2
                            p3=yr.p3
                            p4=yr.p4
                            sums_p1=sums_p1+p1
                            sums_p2=sums_p2+p2
                            sums_p3=sums_p3+p3
                            sums_p4=sums_p4+p4
                            count=count+1
                    avgs_p1=sums_p1/count
                    avgs_p2=sums_p2/count
                    avgs_p3=sums_p3/count
                    avgs_p4=sums_p4/count
                hr=tap3_repo_daily.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id)
                if hr:
                    yr_data=tap3_repo_daily.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id).update(device_id=device_id,service='tap3',p1={'sum':sums_p1,'avg':avgs_p1,'count':count},p2={'sum':sums_p2,'avg':avgs_p2,'count':count},p3={'sum':sums_p3,'avg':avgs_p3,'count':count},p4={'sum':sums_p4,'avg':avgs_p4,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                else:
                    yr_data=tap3_repo_daily.objects.create(device_id=device_id,service='tap3',p1={'sum':sums_p1,'avg':avgs_p1,'count':count},p2={'sum':sums_p2,'avg':avgs_p2,'count':count},p3={'sum':sums_p3,'avg':avgs_p3,'count':count},p4={'sum':sums_p4,'avg':avgs_p4,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                    yr_data.save()
                #monthly
                yrdata=disp_tap3.objects.filter(year=dd[0],month=dd[1],device_id=device_id)
                count=0
                zerocount=-1
                sumd={}
                sums_p1=0
                sums_p2=0
                sums_p3=0
                sums_p4=0
                avgs_p1 = 0
                avgs_p2 = 0
                avgs_p3 = 0
                avgs_p4 = 0
                if yrdata:
                    for yr in yrdata:
                        yr_d_id=yr.device_id
                        if yr_d_id == device_id:
                            p1=yr.p1
                            p2=yr.p2
                            p3=yr.p3
                            p4=yr.p4
                            sums_p1=sums_p1+p1
                            sums_p2=sums_p2+p2
                            sums_p3=sums_p3+p3
                            sums_p4=sums_p4+p4
                            count=count+1
                    avgs_p1=sums_p1/count
                    avgs_p2=sums_p2/count
                    avgs_p3=sums_p3/count
                    avgs_p4=sums_p4/count
                hr=tap3_repo_monthly.objects.filter(year=dd[0],month=dd[1],device_id=device_id)
                if hr:
                    yr_data=tap3_repo_monthly.objects.filter(year=dd[0],month=dd[1],device_id=device_id).update(device_id=device_id,service='tap3',p1={'sum':sums_p1,'avg':avgs_p1,'count':count},p2={'sum':sums_p2,'avg':avgs_p2,'count':count},p3={'sum':sums_p3,'avg':avgs_p3,'count':count},p4={'sum':sums_p4,'avg':avgs_p4,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                else:
                    yr_data=tap3_repo_monthly.objects.create(device_id=device_id,service='tap3',p1={'sum':sums_p1,'avg':avgs_p1,'count':count},p2={'sum':sums_p2,'avg':avgs_p2,'count':count},p3={'sum':sums_p3,'avg':avgs_p3,'count':count},p4={'sum':sums_p4,'avg':avgs_p4,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                    yr_data.save()
                #yearly
                yrdata=disp_tap3.objects.filter(year=dd[0],device_id=device_id)
                count=0
                zerocount=-1
                sumd={}
                sums_p1=0
                sums_p2=0
                sums_p3=0
                sums_p4=0
                avgs_p1 = 0
                avgs_p2 = 0
                avgs_p3 = 0
                avgs_p4 = 0
                if yrdata:
                    for yr in yrdata:
                        yr_d_id=yr.device_id
                        if yr_d_id == device_id:
                            p1=yr.p1
                            p2=yr.p2
                            p3=yr.p3
                            p4=yr.p4
                            sums_p1=sums_p1+p1
                            sums_p2=sums_p2+p2
                            sums_p3=sums_p3+p3
                            sums_p4=sums_p4+p4
                            count=count+1
                    avgs_p1=sums_p1/count
                    avgs_p2=sums_p2/count
                    avgs_p3=sums_p3/count
                    avgs_p4=sums_p4/count
                hr=tap3_repo_yearly.objects.filter(year=dd[0],device_id=device_id)
                if hr:
                    yr_data=tap3_repo_yearly.objects.filter(year=dd[0],device_id=device_id).update(device_id=device_id,service='tap3',p1={'sum':sums_p1,'avg':avgs_p1,'count':count},p2={'sum':sums_p2,'avg':avgs_p2,'count':count},p3={'sum':sums_p3,'avg':avgs_p3,'count':count},p4={'sum':sums_p4,'avg':avgs_p4,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                else:
                    yr_data=tap3_repo_yearly.objects.create(device_id=device_id,service='tap3',p1={'sum':sums_p1,'avg':avgs_p1,'count':count},p2={'sum':sums_p2,'avg':avgs_p2,'count':count},p3={'sum':sums_p3,'avg':avgs_p3,'count':count},p4={'sum':sums_p4,'avg':avgs_p4,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                    yr_data.save()
        if 'tap4'==components:
                # com=cl
                if device_id not in device_idlist:
                     repo_latestdata.objects.create(device_id=device_id,message_type=msg_type,tap4=mydata1)
                else:
                    repo_latestobj = repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id, message_type=msg_type, tap4=mydata1)

                    get_device_id=repo_latestdata.objects.all()
                    for did in get_device_id:
                        s=str(did.device_id)
                        if device_id == s:
                            tap4=did.tap4
                    klist = list(tap4.keys())
                    print("klist is:",klist)
                    mydatakey = list(mydata1.keys())
                    print("mydatakey:",mydatakey)
                    for k,v in tap4.items():
                         if k not in mydatakey:
                              olddata.update({k:v})
                              
                    mydata5=olddata.update(mydata1)    
                    print("old data is:",olddata) # add/update keys in mydata1 to olddata
                    repo_latestobj = repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id, message_type=msg_type, tap4=olddata)

                # repo_latestobj=repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id,message_type=msg_type,tap4=mydata1)
                # repo_latestobj.save()
                ds=disp_tap4.objects.create(device_id=device_id,message_type=msg_type,p1=p1,p2=p2,p3=p3,p4=p4,year=dd[0],month=dd[1],day=dd[2],hour=dd[3],minit=dd[4],second=dd[5])
                ds.save()
                #hourly
                yrdata=disp_tap4.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id)
                count=0
                zerocount=-1
                sumd={}
                sums_p1=0
                sums_p2=0
                sums_p3=0
                sums_p4=0
                avgs_p1 = 0
                avgs_p2 = 0
                avgs_p3 = 0
                avgs_p4 = 0
                if yrdata:
                    for yr in yrdata:
                        yr_d_id=yr.device_id
                        if yr_d_id == device_id:
                            p1=yr.p1
                            p2=yr.p2
                            p3=yr.p3
                            p4=yr.p4
                            sums_p1=sums_p1+p1
                            sums_p2=sums_p2+p2
                            sums_p3=sums_p3+p3
                            sums_p4=sums_p4+p4
                            count=count+1
                    avgs_p1=sums_p1/count
                    avgs_p2=sums_p2/count
                    avgs_p3=sums_p3/count
                    avgs_p4=sums_p4/count
                hr=tap4_repo_hourly.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id)
                if hr:
                    yr_data=tap4_repo_hourly.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id).update(device_id=device_id,service='tap4',p1={'sum':sums_p1,'avg':avgs_p1,'count':count},p2={'sum':sums_p2,'avg':avgs_p2,'count':count},p3={'sum':sums_p3,'avg':avgs_p3,'count':count},p4={'sum':sums_p4,'avg':avgs_p4,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                else:
                    yr_data=tap4_repo_hourly.objects.create(device_id=device_id,service='tap4',p1={'sum':sums_p1,'avg':avgs_p1,'count':count},p2={'sum':sums_p2,'avg':avgs_p2,'count':count},p3={'sum':sums_p3,'avg':avgs_p3,'count':count},p4={'sum':sums_p4,'avg':avgs_p4,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                    yr_data.save()

                #daily
                yrdata=disp_tap4.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id)
                count=0
                zerocount=-1
                sumd={}
                sums_p1=0
                sums_p2=0
                sums_p3=0
                sums_p4=0
                avgs_p1 = 0
                avgs_p2 = 0
                avgs_p3 = 0
                avgs_p4 = 0
                if yrdata:
                    for yr in yrdata:
                        yr_d_id=yr.device_id
                        if yr_d_id == device_id:
                            p1=yr.p1
                            p2=yr.p2
                            p3=yr.p3
                            p4=yr.p4
                            sums_p1=sums_p1+p1
                            sums_p2=sums_p2+p2
                            sums_p3=sums_p3+p3
                            sums_p4=sums_p4+p4
                            count=count+1
                    avgs_p1=sums_p1/count
                    avgs_p2=sums_p2/count
                    avgs_p3=sums_p3/count
                    avgs_p4=sums_p4/count
                hr=tap4_repo_daily.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id)
                if hr:
                    yr_data=tap4_repo_daily.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id).update(device_id=device_id,service='tap4',p1={'sum':sums_p1,'avg':avgs_p1,'count':count},p2={'sum':sums_p2,'avg':avgs_p2,'count':count},p3={'sum':sums_p3,'avg':avgs_p3,'count':count},p4={'sum':sums_p4,'avg':avgs_p4,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                else:
                    yr_data=tap4_repo_daily.objects.create(device_id=device_id,service='tap4',p1={'sum':sums_p1,'avg':avgs_p1,'count':count},p2={'sum':sums_p2,'avg':avgs_p2,'count':count},p3={'sum':sums_p3,'avg':avgs_p3,'count':count},p4={'sum':sums_p4,'avg':avgs_p4,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                    yr_data.save()
                #monthly
                yrdata=disp_tap4.objects.filter(year=dd[0],month=dd[1],device_id=device_id)
                count=0
                zerocount=-1
                sumd={}
                sums_p1=0
                sums_p2=0
                sums_p3=0
                sums_p4=0
                avgs_p1 = 0
                avgs_p2 = 0
                avgs_p3 = 0
                avgs_p4 = 0
                if yrdata:
                    for yr in yrdata:
                        yr_d_id=yr.device_id
                        if yr_d_id == device_id:
                            p1=yr.p1
                            p2=yr.p2
                            p3=yr.p3
                            p4=yr.p4
                            sums_p1=sums_p1+p1
                            sums_p2=sums_p2+p2
                            sums_p3=sums_p3+p3
                            sums_p4=sums_p4+p4
                            count=count+1
                    avgs_p1=sums_p1/count
                    avgs_p2=sums_p2/count
                    avgs_p3=sums_p3/count
                    avgs_p4=sums_p4/count
                hr=tap4_repo_monthly.objects.filter(year=dd[0],month=dd[1],device_id=device_id)
                if hr:
                    yr_data=tap4_repo_monthly.objects.filter(year=dd[0],month=dd[1],device_id=device_id).update(device_id=device_id,service='tap4',p1={'sum':sums_p1,'avg':avgs_p1,'count':count},p2={'sum':sums_p2,'avg':avgs_p2,'count':count},p3={'sum':sums_p3,'avg':avgs_p3,'count':count},p4={'sum':sums_p4,'avg':avgs_p4,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                else:
                    yr_data=tap4_repo_monthly.objects.create(device_id=device_id,service='tap4',p1={'sum':sums_p1,'avg':avgs_p1,'count':count},p2={'sum':sums_p2,'avg':avgs_p2,'count':count},p3={'sum':sums_p3,'avg':avgs_p3,'count':count},p4={'sum':sums_p4,'avg':avgs_p4,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                    yr_data.save()
                #yearly
                yrdata=disp_tap4.objects.filter(year=dd[0],device_id=device_id)
                count=0
                zerocount=-1
                sumd={}
                sums_p1=0
                sums_p2=0
                sums_p3=0
                sums_p4=0
                avgs_p1 = 0
                avgs_p2 = 0
                avgs_p3 = 0
                avgs_p4 = 0
                if yrdata:
                    for yr in yrdata:
                        yr_d_id=yr.device_id
                        if yr_d_id == device_id:
                            p1=yr.p1
                            p2=yr.p2
                            p3=yr.p3
                            p4=yr.p4
                            sums_p1=sums_p1+p1
                            sums_p2=sums_p2+p2
                            sums_p3=sums_p3+p3
                            sums_p4=sums_p4+p4
                            count=count+1
                    avgs_p1=sums_p1/count
                    avgs_p2=sums_p2/count
                    avgs_p3=sums_p3/count
                    avgs_p4=sums_p4/count
                hr=tap4_repo_yearly.objects.filter(year=dd[0],device_id=device_id)
                if hr:
                    yr_data=tap4_repo_yearly.objects.filter(year=dd[0],device_id=device_id).update(device_id=device_id,service='tap4',p1={'sum':sums_p1,'avg':avgs_p1,'count':count},p2={'sum':sums_p2,'avg':avgs_p2,'count':count},p3={'sum':sums_p3,'avg':avgs_p3,'count':count},p4={'sum':sums_p4,'avg':avgs_p4,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                else:
                    yr_data=tap4_repo_yearly.objects.create(device_id=device_id,service='tap4',p1={'sum':sums_p1,'avg':avgs_p1,'count':count},p2={'sum':sums_p2,'avg':avgs_p2,'count':count},p3={'sum':sums_p3,'avg':avgs_p3,'count':count},p4={'sum':sums_p4,'avg':avgs_p4,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                    yr_data.save()
        try:
            if 'consen'==components:
                # com=cl
                if device_id not in device_idlist:
                     repo_latestdata.objects.create(device_id=device_id,message_type=msg_type,consen=mydata1)
                else:
                    repo_latestobj = repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id, message_type=msg_type, consen=mydata1)

                    get_device_id=repo_latestdata.objects.all()
                    for did in get_device_id:
                        s=str(did.device_id)
                        if device_id == s:
                            consen=did.consen
                    klist = list(consen.keys())
                    print("klist is:",klist)
                    mydatakey = list(mydata1.keys())
                    print("mydatakey:",mydatakey)
                    for k,v in consen.items():
                         if k not in mydatakey:
                              olddata.update({k:v})
                              
                    mydata5=olddata.update(mydata1)    
                    print("old data is:",olddata) # add/update keys in mydata1 to olddata
                    repo_latestobj = repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id, message_type=msg_type, consen=olddata)

                ds=disp_consen.objects.create(device_id=device_id,message_type=msg_type,cnd=cnd,spn=spn,asp=asp,year=dd[0],month=dd[1],day=dd[2],hour=dd[3],minit=dd[4],second=dd[5])
                ds.save() 
                #hourly
                yrdata=disp_consen.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id)
                count=0
                zerocount=-1
                sumd={}
                sums_cnd=0
                sums_spn=0
                sums_asp=0
                avgs_cnd = 0
                avgs_spn = 0
                avgs_asp = 0
                
                if yrdata:
                    for yr in yrdata:
                        yr_d_id=yr.device_id
                        if yr_d_id == device_id:
                            cnd=yr.cnd
                            spn=yr.spn
                            asp=yr.asp
                            
                            sums_cnd=sums_cnd+cnd
                            sums_spn=sums_spn+spn
                            sums_asp=sums_asp+asp
                            
                            count=count+1
                    avgs_cnd=sums_cnd/count
                    avgs_spn=sums_spn/count
                    avgs_asp=sums_asp/count
               
                hr=consen_repo_hourly.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id)
                if hr:
                    yr_data=consen_repo_hourly.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id).update(device_id=device_id,service='consen',cnd={'sum':sums_cnd,'avg':avgs_cnd,'count':count},spn={'sum':sums_spn,'avg':avgs_spn,'count':count},asp={'sum':sums_asp,'avg':avgs_asp,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                else:
                    yr_data=consen_repo_hourly.objects.create(device_id=device_id,service='consen',cnd={'sum':sums_cnd,'avg':avgs_cnd,'count':count},spn={'sum':sums_spn,'avg':avgs_spn,'count':count},asp={'sum':sums_asp,'avg':avgs_asp,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                    yr_data.save()
                #daily
                yrdata=disp_consen.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id)
                count=0
                zerocount=-1
                sumd={}
                sums_cnd=0
                sums_spn=0
                sums_asp=0
                avgs_cnd = 0
                avgs_spn = 0
                avgs_asp = 0
                
                if yrdata:
                    for yr in yrdata:
                        yr_d_id=yr.device_id
                        if yr_d_id == device_id:
                            cnd=yr.cnd
                            spn=yr.spn
                            asp=yr.asp
                            
                            sums_cnd=sums_cnd+cnd
                            sums_spn=sums_spn+spn
                            sums_asp=sums_asp+asp
                            
                            count=count+1
                    avgs_cnd=sums_cnd/count
                    avgs_spn=sums_spn/count
                    avgs_asp=sums_asp/count
               
                hr=consen_repo_daily.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id)
                if hr:
                    yr_data=consen_repo_daily.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id).update(device_id=device_id,service='consen',cnd={'sum':sums_cnd,'avg':avgs_cnd,'count':count},spn={'sum':sums_spn,'avg':avgs_spn,'count':count},asp={'sum':sums_asp,'avg':avgs_asp,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                else:
                    yr_data=consen_repo_daily.objects.create(device_id=device_id,service='consen',cnd={'sum':sums_cnd,'avg':avgs_cnd,'count':count},spn={'sum':sums_spn,'avg':avgs_spn,'count':count},asp={'sum':sums_asp,'avg':avgs_asp,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                    yr_data.save()
                #monthly
                yrdata=disp_consen.objects.filter(year=dd[0],month=dd[1],device_id=device_id)
                count=0
                zerocount=-1
                sumd={}
                sums_cnd=0
                sums_spn=0
                sums_asp=0
                avgs_cnd = 0
                avgs_spn = 0
                avgs_asp = 0
                
                if yrdata:
                    for yr in yrdata:
                        yr_d_id=yr.device_id
                        if yr_d_id == device_id:
                            cnd=yr.cnd
                            spn=yr.spn
                            asp=yr.asp
                            
                            sums_cnd=sums_cnd+cnd
                            sums_spn=sums_spn+spn
                            sums_asp=sums_asp+asp
                            
                            count=count+1
                    avgs_cnd=sums_cnd/count
                    avgs_spn=sums_spn/count
                    avgs_asp=sums_asp/count
               
                hr=consen_repo_monthly.objects.filter(year=dd[0],month=dd[1],device_id=device_id)
                if hr:
                    yr_data=consen_repo_monthly.objects.filter(year=dd[0],month=dd[1],device_id=device_id).update(device_id=device_id,service='consen',cnd={'sum':sums_cnd,'avg':avgs_cnd,'count':count},spn={'sum':sums_spn,'avg':avgs_spn,'count':count},asp={'sum':sums_asp,'avg':avgs_asp,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                else:
                    yr_data=consen_repo_monthly.objects.create(device_id=device_id,service='consen',cnd={'sum':sums_cnd,'avg':avgs_cnd,'count':count},spn={'sum':sums_spn,'avg':avgs_spn,'count':count},asp={'sum':sums_asp,'avg':avgs_asp,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                    yr_data.save()
                #yearly
                yrdata=disp_consen.objects.filter(year=dd[0],device_id=device_id)
                count=0
                zerocount=-1
                sumd={}
                sums_cnd=0
                sums_spn=0
                sums_asp=0
                avgs_cnd = 0
                avgs_spn = 0
                avgs_asp = 0
                
                if yrdata:
                    for yr in yrdata:
                        yr_d_id=yr.device_id
                        if yr_d_id == device_id:
                            cnd=yr.cnd
                            spn=yr.spn
                            asp=yr.asp
                            
                            sums_cnd=sums_cnd+cnd
                            sums_spn=sums_spn+spn
                            sums_asp=sums_asp+asp
                            
                            count=count+1
                    avgs_cnd=sums_cnd/count
                    avgs_spn=sums_spn/count
                    avgs_asp=sums_asp/count
               
                hr=consen_repo_yearly.objects.filter(year=dd[0],device_id=device_id)
                if hr:
                    yr_data=consen_repo_yearly.objects.filter(year=dd[0],device_id=device_id).update(device_id=device_id,service='consen',cnd={'sum':sums_cnd,'avg':avgs_cnd,'count':count},spn={'sum':sums_spn,'avg':avgs_spn,'count':count},asp={'sum':sums_asp,'avg':avgs_asp,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                else:
                    yr_data=consen_repo_yearly.objects.create(device_id=device_id,service='consen',cnd={'sum':sums_cnd,'avg':avgs_cnd,'count':count},spn={'sum':sums_spn,'avg':avgs_spn,'count':count},asp={'sum':sums_asp,'avg':avgs_asp,'count':count},hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                    yr_data.save()
                # yrdata=disp_consen.objects.filter(year=dd[0],device_id=device_id)
                # count=0
                # sums=0
                # avgs = 0
                # if yrdata:
                #     for yr in yrdata:
                #         yr_d_id=yr.device_id
                #         if yr_d_id == device_id:
                #             cnds=yr.cnd
                #             print("cnds is:",cnds)
                #             sums=sums+cnds
                #             count=count+1
                #             print("sums is:",sums)
                #             print("count is:",count)
                #     avgs=sums/count
                # hr=repo_yearly.objects.filter(year=dd[0],device_id=device_id)
                # if hr:
                #     yr_data=repo_yearly.objects.filter(device_id=device_id).update(device_id=device_id,service='consen_cnd',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
                # else:
                #     yr_data=repo_yearly.objects.create(device_id=device_id,service='consen_cnd',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
                #     yr_data.save()
            
                # # month
                # yrdata=disp_consen.objects.filter(year=dd[0],month=dd[1],device_id=device_id)
                # count=0
                # sums=0
                # avgs = 0
                # if yrdata:
                #     for yr in yrdata:
                #         yr_d_id=yr.device_id
                #         if yr_d_id == device_id:
                #             cnds=yr.cnd
                #             print("cnds is:",cnds)
                #             sums=sums+cnds
                #             count=count+1
                #             print("sums is:",sums)
                #             print("count is:",count)
                #     avgs=sums/count
                # hr=repo_monthly.objects.filter(year=dd[0],month=dd[1],device_id=device_id)
                # if hr:
                #     yr_data=repo_monthly.objects.filter(year=dd[0],month=dd[1],device_id=device_id).update(device_id=device_id,service='consen_cnd',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
                # else:
                #     yr_data=repo_monthly.objects.create(device_id=device_id,service='consen_cnd',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
                #     yr_data.save()
                
                # # day
                # yrdata=disp_consen.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id)
                # count=0
                # sums=0
                # avgs = 0
                # if yrdata:
                #     for yr in yrdata:
                #         yr_d_id=yr.device_id
                #         if yr_d_id == device_id:
                #             cnds=yr.cnd
                #             print("cnds is:",cnds)
                #             sums=sums+cnds
                #             count=count+1
                #             print("sums is:",sums)
                #             print("count is:",count)
                #     avgs=sums/count
                # hr=repo_daily.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id)
                # if hr:
                #     yr_data=repo_daily.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id).update(device_id=device_id,service='consen_cnd',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0],day=dd[2])
                # else:
                #     yr_data=repo_daily.objects.create(device_id=device_id,service='consen_cnd',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0],day=dd[2])
                #     yr_data.save()
                
                # # hour
                # yrdata=disp_consen.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id)
                # count=0
                # sums=0
                # avgs = 0
                # if yrdata:
                #     for yr in yrdata:
                #         yr_d_id=yr.device_id
                #         if yr_d_id == device_id:
                #             cnds=yr.cnd
                #             print("cnds is:",cnds)
                #             sums=sums+cnds
                #             count=count+1
                #             print("sums is:",sums)
                #             print("count is:",count)
                #     avgs=sums/count
                # hr=repo_hourly.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id)
                # if hr:
                #     yr_data=repo_hourly.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id).update(device_id=device_id,service='consen_cnd',sum=sums,count=count,avg=avgs,hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                # else:
                #     yr_data=repo_hourly.objects.create(device_id=device_id,service='consen_cnd',sum=sums,count=count,avg=avgs,hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                #     yr_data.save()
        except Exception as e:
            print("error ==>", e)
            error_message = e
            # global eg
            eg = e
            print("eg is:",eg)
            print("Error massage:",e)
            EchoConsumer.websocket_receive('event','event') 


        # class EchoConsumer(SyncConsumer):
        #     def websocket_connect(self, event):
            
        #         print("connect event is called")

        #         self.send({
        #             'type': 'websocket.accept'
        #         })

        #     def websocket_receive(self, event):
            
        #         print("event in receive", event)
        #         # msg=input("Enter message: ")
        #         # if msgo:
        #         try:
        #             # Call another function that may raise an exception
        #             result = on_message()
        #             # Process the result
                    
        #         except Exception as e:
        #             print("First error:", e)
        #         try:
        #             # Simulate an exception
        #             1 / 0
        #         except Exception as e:
        #                 # Send the exception message to the WebSocket client
        #                 self.send({
        #                     'type': 'websocket.send',
        #                     # 'text': event.get('text')
        #                     'text': str(e),
                            
        #                 })
        #         # self.send({
        #         #     'type': 'websocket.send',
        #         #     # 'text': event.get('text')
        #         #     'text': msg
        #         # })
        #         self.websocket_receive(event)

        # #    async def websocket_disconnect(self, event):
        # #         print("connection is disconnected")

        #     def disconnect(self, close_code):
        # # Leave room group
        #         async_to_sync(self.channel_layer.group_discard)(
        #             self.room_group_name,
        #             self.channel_name
        #         )
        #         raise StopConsumer()

        # from channels.layers import get_channel_layer
        # from asgiref.sync import async_to_sync

        # def my_view(request):
        #     channel_layer = get_channel_layer()
        #     async_to_sync(channel_layer.group_send)(
        #         'exceptions',  # Group name
        #         {
        #             'type': 'send.exception',
        #             'exception': 'This is an exception message.',
        #         }
        #     )
    # Rest of your view logic


        # if response.status_code == 200:
        #     print("HELLO",response.json())
    # rwp=rwp_setting.objects.last()
    # print("RWP",rwp)
    # comd.update({'olc':rwp.olc,'drc':rwp.drc,'spn':rwp.spn})
    # print("comd",comd)
    # print("rwp is:",rwp)
    # print("olc is:",rwp.olc)
    # print("drc is:",rwp.drc)
    # print("spn is:",rwp.spn)
    # print("unit_type is:",rwp.unit_type)
    # print("company_name is:",rwp.company_name)
    # print("componant_name:",rwp.componant_name)
    # print("-x-"*25)
    # dinfo=devices_info.objects.filter(componant_name=rwp.componant_name,unit_type=rwp.unit_type,company_name=rwp.company_name)
    # # print("dinfo is:",dinfo.componant_name)
    # cmpname=str()
    # did=0
    # for x in dinfo:
    #     print("did id:",x.Device_id)
    #     did=x.Device_id
    #     cmpname=x.componant_name

    #     urlo=f"wd/{did}/updset/{cmpname}"
    #     print("url is ",urlo)
    #     testlist={f'wd/{did}/updset/{cmpname}':str(comd)}#,'test/topic/2':comd
    #     print("****",testlist)
    #     for k,v in testlist.items():
    #         rc, mid = mqtt_client.publish(k,v)
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message
    # client.username_pw_set(settings.MQTT_USER, settings.MQTT_PASSWORD)
    # client.connect(
    #     host=settings.MQTT_SERVER,
    #     port=settings.MQTT_PORT,
    #     keepalive=settings.MQTT_KEEPALIVE
    # )
    # mqtt_client.connect('broker.example.com', 1883)

    # Start the client loop

    mqtt_client.loop_forever()
    # EchoConsumer.websocket_receive('event','event')

