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
        # crear dataframe con pandas

        url = 'https://www.sii.cl/valores_y_fechas/uf/uf2023.htm'
        html = requests.get(url)
        content = html.content
        soup = bs(content, 'html.parser')

        table = soup.find('table', {'id': 'table_export'})
        headers = [th.text.strip() for th in table.find('thead').find_all('th')]
        # print(headers)
        collected_data = []
        for row in table.find('tbody').find_all('tr'):
            row_data = [td.text.strip() for td in row.find_all(['th', 'td'])]
            collected_data.append(row_data)

        df = pd.DataFrame(collected_data, columns=headers)
        columns = df.columns
        # print(df)
        # print(df['Día'])
        for month in columns[1:]:
            values_for_month = [row[month] for _, row in df.iterrows()]
            month_name = month[:3]
            for index, value in enumerate(values_for_month, start=1):
                data_instance = Data(day=index, month=month_name, value=value)
                data_instance.save()

        return Response('data saved successfully')


class DataList(APIView):
    def get(self, request):
        data = Data.data.all()
        serializer = SerializerData(data, many=True)
        return Response(serializer.data)
