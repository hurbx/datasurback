from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from bs4 import BeautifulSoup as bs

from .Serializer.data_serializer import SerializerData
from .models import Data

import re


class DataView(APIView):
    def get(self, request):
        url = 'https://www.bcentral.cl/inicio'
        html = requests.get(url)
        content = html.content
        data = bs(content, 'html.parser')

        # uf_p_tag = data.find('div', {'class': 'tooltip-wrap'}).find_all('p', {
        #     'class': 'basic-text fs-2 f-opensans-bold text-center c-blue-nb-2'})
        #
        #
        # Data.data.create(uf=uf_value,
        #                  utm=utm_value,
        #                  dolar_obs=dolar_obs_value,
        #                  euro=euro_value,
        #                  date=date_value)

        return Response('data saved successfully')


