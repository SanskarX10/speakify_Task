import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.layers import get_channel_layer
from channels.db import database_sync_to_async


class PersonalChatConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        # Get the user 
        user = self.scope['user']

        if user.is_anonymous:
            # Reject the connection for anonymous users
            await self.close()
        else:
            # Accept the connection for authenticated users
            await self.accept()

            channel_layer = get_channel_layer()
            await channel_layer.group_send(
                f"user_{user.id}",
                {
                    "type": "user.notification",
                    "message": "You are connected via WebSocket.",
                },
            )

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):

        user = self.scope['user']
        if user.is_authenticated:
            message = json.loads(text_data)

            response = {
                'status': 'success',
                'message': 'Message received and processed successfully.',
            }
            await self.send(text_data=json.dumps(response))
        else:

            response = {
                'status': 'error',
                'message': 'Authentication required.',
            }
            await self.send(text_data=json.dumps(response))
    
    async def user_notification(self, event):

        message = event["message"]
        await self.send(text_data=json.dumps({"notification": message}))