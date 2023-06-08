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
from accounts.consumers import PersonalChatConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shopify_task.settings')

application = get_asgi_application()

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter([
            path('ws/<int:id>/', PersonalChatConsumer)
        ])
    ),
    "http": get_asgi_application()
})