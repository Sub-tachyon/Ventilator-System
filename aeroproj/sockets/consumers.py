from channels.generic.websocket import AsyncWebsocketConsumer
import json
import asyncio

class DummyDataConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send_dummy_data()  # Call the method to send dummy data after accepting the connection

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        pass

    async def send_dummy_data(self):
        for i in range(5):   
            dummy_data = {'device_id': i, 'status': 'Online'}
            await asyncio.sleep(2)  # delay (2 seconds)
            await self.send(text_data=json.dumps(dummy_data))  #sending json
