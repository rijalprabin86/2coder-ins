from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),  # Maps the root URL of the app to the `home` view
]