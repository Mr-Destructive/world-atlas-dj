import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "WorldAtlas.settings")
import django
django.setup()

from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from play import routing

#application = get_asgi_application()

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    "websocket":AuthMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns
        )
    )
})
