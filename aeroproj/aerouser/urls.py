from django.urls import path
from . import views

urlpatterns = [
    path("login", views.login, name="login"),
    path("signup",views.signup, name="signup" ),
    path("forgot/",views.forgot, name="forgot"),
    path("otp_verification",views.otp, name="otp_verification"),
    path("password_change/<str:token>",views.password_reset, name="password_change"),
    path("logout",views.logout, name="logout"),
    path("user_landing", views.user_landing, name='user_landing'),
    path("user_homepage/<str:serial_number>", views.user_homepage, name='user_homepage'),
    path("device_details", views.device_info, name='device_details'),
    path("patient_details", views.patient_info, name='patient_details'),
    path("monitor", views.monitors, name='monitor'),
]
