"""
ASGI config for shopify_task project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from channels.auth import AuthMiddlewareStack
from accounts.models import User
from accounts.consumers import PersonalChatConsumer
from django.contrib.auth.models import User

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shopify_task.settings')

application = get_asgi_application()

from django.urls import re_path
from  accounts.consumers import PersonalChatConsumer

websocket_urlpatterns = [
    re_path(r'^ws/chat/(?P<user_id>\w+)/$', PersonalChatConsumer.as_asgi()),

]

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(websocket_urlpatterns))
    ,
    "http": get_asgi_application()
})