from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

from .Serializer.data_serializer import SerializerData
from .models import Data

import re


class DataView(APIView):
    def get(self, request):
        # buscar tabla por su id
        # extraer los encabezados de la tabla
        # extraer filas de la tabla
        # crear lista con los datos de las columnas
        # crear dataframe
        # subir dataframe completo a modelo de django
        url = 'https://www.sii.cl/valores_y_fechas/uf/uf2023.htm'
        html = requests.get(url)
        content = html.content
        data = bs(content, 'html.parser')
        table = data.find('table', {'id': 'table_export'})
        rows = table.find('tbody').find_all('tr')
        headers = [th.text.strip() for th in rows[0].find_all('th')]
        #print(headers)




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


