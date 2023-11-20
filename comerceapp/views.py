from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from bs4 import BeautifulSoup as bs

from .Serializer.data_serializer import SerializerData
from .models import Data


class DataView(APIView):
    def get(self, request):
        global uf_value, utm_value, dolar_obs_value, euro_value, date_value
        url = 'https://www.bcentral.cl/inicio'
        html = requests.get(url)
        content = html.content
        data = bs(content, 'html.parser')

        uf_p_tag = data.find('div', {'class': 'tooltip-wrap'}).find_all('p', {
            'class': 'basic-text fs-2 f-opensans-bold text-center c-blue-nb-2'})

        if uf_p_tag:
            uf_value = uf_p_tag[0].text.strip()
            print(uf_value)
        else:
            print('data not found in uf_p_tag')

        utm_p_tag = data.find_all('div', {'class': 'tooltip-wrap'})[1].find_all('p', {
            'class': 'basic-text fs-2 f-opensans-bold text-center c-blue-nb-2'})

        if utm_p_tag:
            utm_value = utm_p_tag[0].text.strip()
            print(utm_value)
        else:
            print('data not found in utm_p_tag')

        dolar_obs_p_tag = data.find_all('div', {'class': 'tooltip-wrap'})[2].find_all('p', {
            'class': 'basic-text fs-2 f-opensans-bold text-center c-blue-nb-2'})

        if dolar_obs_p_tag:
            dolar_obs_value = dolar_obs_p_tag[0].text.strip()
            print(dolar_obs_value)
        else:
            print('data not found in dolar_obs_p_tag')

        euro_p_tag = data.find_all('div', {'class': 'tooltip-wrap'})[3].find_all('p', {
            'class': 'basic-text fs-2 f-opensans-bold text-center c-blue-nb-2'})

        if euro_p_tag:

            euro_value = euro_p_tag[0].text.strip()
            print(euro_value)
        else:
            print('data not found in euro_p_tag')

        date_p_tag = data.find('p', {
            'class': 'basic-text f-opensans-semibold c-beige-nb-1 fs-1 mb-1 text-center text-lg-left'})

        if date_p_tag:
            date_value = date_p_tag.text.strip()
            print(date_value)
        else:
            print('date not found in date_p_tag')

        # saving data in model
        Data.objects.create(date=date_value, uf=uf_value.replace('$', ''),
                            utm=utm_value.replace('$', ''),
                            dolar_obs=dolar_obs_value.replace('$', ''),
                            euro=euro_value.replace('$', '')).save()

        return Response('data saved successfully')


class AllData(APIView):
    def get(self, request):
        DataView().get(request)
        data = Data.objects.all()
        serializer = SerializerData(data, many=True)
        return Response(serializer.data)
