from django.urls import path
from .views import *
urlpatterns = [
    path("dashboard/",view_dashboard,name="dashboard"),
    path("change_password/",password_change,name="change-password")
]
