from django.contrib import admin
from django.urls import path
from .views import DataView, AllData

urlpatterns = [
    path('extract/', DataView.as_view()),
    path('data/', AllData.as_view()),
]