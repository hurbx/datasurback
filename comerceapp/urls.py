from django.contrib import admin
from django.urls import path
from .views import DataView, DataList, MiscList, DataChart

urlpatterns = [
    path('extract/', DataView.as_view()),
    path('list/', DataList.as_view()),
    path('misc/', MiscList.as_view()),
    path('chart/', DataChart.as_view()),
]