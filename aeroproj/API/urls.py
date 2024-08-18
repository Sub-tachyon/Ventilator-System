from django.urls import path
from . import views

urlpatterns = [
    path('adddevices',views.addDevices),
]
