from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from .Serializer.data_serializer import SerializerData
from .models import Data
from django.db.models import Max
from django.db.models import Avg
from django.db.models import Min

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
        max_value = Data.data.aggregate(max_value=Max('value'))['max_value']
        print(max_value)
        return Response(serializer.data)


class MiscList(APIView):
    def get(self, request):
        filtered_data = Data.data.exclude(value='')
        max_value = filtered_data.aggregate(max_value=Max('value'))['max_value']
        average_value = filtered_data.aggregate(average_value=Avg('value'))['average_value']
        min_value = filtered_data.aggregate(min_value=Min('value'))['min_value']
        min_value = '' if min_value is None else min_value
        try:
            max_value = float(max_value)
        except (TypeError, ValueError):
            pass

        try:
            average_value = float(average_value)
        except (TypeError, ValueError):
            pass

        try:
            min_value = float(min_value)
        except (TypeError, ValueError):
            pass

        data = {
            'max_value': max_value,
            'average_value': average_value,
            'min_value': min_value
        }

        return Response(data)


class DataChart(APIView):
    def get(self, request):
        months = Data.data.values_list('month', flat=True).distinct()

        max_values_list = []

        for month in months:
            max_value_of_month = Data.data.filter(month=month).aggregate(max_value=Max('value'))['max_value']
            max_values_list.append(str(max_value_of_month) if max_value_of_month is not None else None)

        return Response(max_values_list)

