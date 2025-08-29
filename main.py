import requests
import pandas as pd

api_key = 'a6255d0f011142e8b8c104239252908'

def tomorrow_forecast(cities):
    for city in cities:
        response = requests.get(f'http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days=2&aqi=no&alerts=no')
        print(response.json())

tomorrow_forecast(['Kyiv', 'Madrid'])