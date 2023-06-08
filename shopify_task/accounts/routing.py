from django.urls import re_path
from  accounts.consumers import PersonalChatConsumer

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<user_id>\d+)/$', PersonalChatConsumer.as_asgi()),

]