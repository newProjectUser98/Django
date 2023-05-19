# from channels.consumer import SyncConsumer
# from devices.views import msgo
# import json
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
#             self.send({
#                 'type': 'websocket.send',
#                 # 'text': event.get('text')
#                 'text': msg
#             })
#             self.websocket_receive(event)

#     def websocket_disconnect(self, event):
#         print("connection is disconnected")


#     async def send_exception(self, exception):
#         await self.send_json({
#             'type': 'exception',
#             'message': str(exception),
#         })
#     # def disconnect(self, close_code):
#     # # Leave room group
#     #     async_to_sync(self.channel_layer.group_discard)(
#     #         self.room_group_name,
#     #         self.channel_name
#     #     )
#     #     raise StopConsumer()


# from channels.generic.websocket import AsyncWebsocketConsumer

# class MyConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         await self.accept()

#     async def disconnect(self, close_code):
#         pass

#     async def receive(self, text_data):
#         await self.send(text_data="You said: " + text_data)