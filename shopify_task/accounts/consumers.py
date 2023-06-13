import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.layers import get_channel_layer
from channels.db import database_sync_to_async


class PersonalChatConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        # Get the user 
        user = self.scope['user']
            # Accept the connection for authenticated users
        await self.accept()

        channel_layer = get_channel_layer()
        await channel_layer.group_send(
            f"user_{user.id}",
            {
                "message": "You are connected via WebSocket."
            },
        )

    async def disconnect(self, close_code):
        user = self.scope['user']

        channel_layer = get_channel_layer()
        await channel_layer.group_send(
            f"user_{user.id}",
            {
                "type": "user.notification",
                "message": "You are disconnected from WebSocket.",
            },
        )

    async def receive(self, text_data):

        user = self.scope['user']
        message = json.loads(text_data)

        response = {
            'status': 'success',
            'message': 'Message received and processed successfully.',
        }
        await self.send(text_data=json.dumps(response))
    
    async def user_notification(self, event):

        message = event["message"]
        await self.send(text_data=json.dumps({"notification": message}))



# class PersonalChatConsumer(AsyncWebsocketConsumer):

#     async def connect(self):
#         # Get the connected user and suggested user
#         connected_user = self.scope['user']
#         suggested_user_id = self.scope['url_route']['kwargs']['user_id']

#         if connected_user.is_anonymous:
#             # Reject the connection for anonymous users
#             await self.close()
#         else:
#             # Accept the connection for authenticated users
#             await self.accept()

#             await self.channel_layer.group_add(
#                 f"user_{connected_user.id}",
#                 self.channel_name
#             )

#             await self.channel_layer.group_add(
#                 f"user_{suggested_user_id}",
#                 self.channel_name
#             )

#             await self.send_user_notification("You are connected via WebSocket.")

#     async def disconnect(self, close_code):
#         # Get the connected user
#         connected_user = self.scope['user']

#         await self.channel_layer.group_discard(
#             f"user_{connected_user.id}",
#             self.channel_name
#         )

#     async def receive(self, text_data):
#         # Get the connected user and suggested user
#         connected_user = self.scope['user']
#         suggested_user_id = self.scope['url_route']['kwargs']['user_id']

#         if connected_user.is_authenticated:
#             message = json.loads(text_data)

#             # Handle the received message from the connected user

#             # Send a response back to the connected user
#             response = {
#                 'status': 'success',
#                 'message': 'Message received and processed successfully.',
#             }
#             await self.send(json.dumps(response))
#         else:
#             response = {
#                 'status': 'error',
#                 'message': 'Authentication required.',
#             }
#             await self.send(json.dumps(response))

#     async def user_notification(self, event):
#         # Send a notification to the connected user
#         message = event["message"]
#         await self.send(json.dumps({"notification": message}))

#     async def send_user_notification(self, message):
#         await self.channel_layer.group_send(
#             f"user_{self.scope['user'].id}",
#             {
#                 "type": "user_notification",
#                 "message": message
#             }
#         )
