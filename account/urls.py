from django.urls import path
from .views import *
urlpatterns = [
    path("",home,name="home"),
    path("register/",register,name="register"),
    path("login/",login,name="login"),
    path("logout/",logout,name="logout"),
    path("password-reset/",password_reset,name="password-reset"),
    path("set-password/",set_password,name="set-password"),
]
