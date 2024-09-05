from django.contrib import admin
from django.urls import path
from .import views
from browser.views import today, browser_set

urlpatterns = [
    path('', today, name='today'),
    path('browser_set', views.browser_set),
]
