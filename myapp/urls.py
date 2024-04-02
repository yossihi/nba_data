"""
aplication
"""
from django.contrib import admin
from django.urls import path

from myapp.views import all_players

urlpatterns = [
    path('all_players', all_players)
]
