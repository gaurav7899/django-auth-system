from django.urls import path
from .views import *
urlpatterns = [
    path("seller/",seller_dashboard_view,name="seller-dashboard")
]
