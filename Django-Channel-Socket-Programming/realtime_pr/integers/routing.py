from django.urls import path

from .consumers import WSConsumer       # .dot means current folder

ws_urlpatterns = [
    path('ws/some_url/', WSConsumer.as_asgi())
]
