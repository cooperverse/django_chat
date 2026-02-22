import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from urllib.parse import parse_qs
from .utils import get_user_from_jwt

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):

        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        query_string = parse_qs(self.scope["query_string"].decode())
        token_list = query_string.get("token")

        if not token_list:
            await self.close()
            return

        try:
            self.user = await get_user_from_jwt(token_list[0])
            if not self.user:
                await self.close()
                return
        except Exception:
            await self.close()
            return

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        if hasattr(self, 'room_group_name'):
            await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        try:
            data = json.loads(text_data)
            content = data.get("message")
            if not content: return

            
            message = await self.create_message(self.user.id, content)

            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    "type": "chat_message",
                    "sender": self.user.username,
                    "content": message.content,
                    "timestamp": message.timestamp.isoformat(),
                    "room": self.room_name,
                }
            )
        except Exception as e:
            print(f"Error: {e}")

    async def chat_message(self, event):
        await self.send(text_data=json.dumps(event))

    @database_sync_to_async
    def create_message(self, user_id, content):
        from .models import Message
        return Message.objects.create(
            sender_id=user_id,
            room=self.room_name,
            content=content
        )