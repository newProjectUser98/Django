from channels.consumer import SyncConsumer
from devices.views import msgo
class EchoConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print("connect event is called")

        self.send({
            'type': 'websocket.accept'
        })

    def websocket_receive(self, event):
        print("event in receive", event)
        msg=input("Enter message: ")
        self.send({
            'type': 'websocket.send',
            # 'text': event.get('text')
            'text': msg
        })
        self.websocket_receive(event)

    def websocket_disconnect(self, event):
        print("connection is disconnected")
        