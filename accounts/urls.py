from django.urls import path 

from .views import *

urlpatterns = [
    path('login', index, name='index'),
    path('register', about, name='about'),
    path('dashboard', contact, name='contact'),
    path('logout', services, name='services'),
    path('edit',)
    # Add more paths as needed