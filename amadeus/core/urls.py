from django.contrib import admin
from django.urls import path, include
from .views import *
from .views import login_view, register_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('', home_view, name='home'),
    path('register/', register_view, name='register'),
    path('add-admin/', add_admin_view, name='add_admin'),
    path('remove-admin/', remove_admin_view, name='remove_admin'),
    # Other URLs
]












