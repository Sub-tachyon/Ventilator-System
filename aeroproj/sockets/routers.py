from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/dummy_data/', consumers.DummyDataConsumer.as_asgi()),
]
