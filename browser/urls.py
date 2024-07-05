from django.contrib import admin
from django.urls import path
from .views import get_imagen

urlpatterns = [
    path('', get_imagen, name='get_imagen'),
]
