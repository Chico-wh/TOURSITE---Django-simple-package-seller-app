from django.urls import path
from .views import *

urlpatterns = [
    path('', travel_package_list, name='travel_packages_list'),
    path('book/<int:package_id>/', booking_handler_view, name='booking_handler_view'),
    path('success/', booking_success, name='booking_success'),
    path('fail/', booking_fail, name='booking_fail'),
]
