from django.contrib import admin
from django.urls import path
from .views import DataView, AllData, LastData

urlpatterns = [
    path('extract/', DataView.as_view()),
    path('data/', AllData.as_view()),
    path('last/', LastData.as_view()),
]