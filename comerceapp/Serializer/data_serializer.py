from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from comerceapp.models import Data


class SerializerData(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = '__all__'