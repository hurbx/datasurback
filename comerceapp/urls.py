from django.contrib import admin
from django.urls import path
from .views import DataView, DataList

urlpatterns = [
    path('extract/', DataView.as_view()),
    path('list/', DataList.as_view()),
]