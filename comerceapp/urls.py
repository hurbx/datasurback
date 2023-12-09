from django.contrib import admin
from django.urls import path
from .views import DataView

urlpatterns = [
    path('extract/', DataView.as_view()),
]