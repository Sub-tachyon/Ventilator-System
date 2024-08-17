from django.urls import path
from .import views

urlpatterns = [
    path("device_reg2", views.device_reg2, name="device_reg2"),
    path("patient/<str:serial_number1>", views.patient_data, name="patient"),
    path("unallocate_device/<str:serial_number2>", views.remove_device, name="unallocate_device"),
    path("patient_list", views.patient_list, name="patient_list"),
    path("device_list", views.device_list, name="device_list"),
    path("device_logs", views.device_logs_view, name="device_logs"),
    
]
