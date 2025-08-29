import requests
import pandas as pd

api_key = 'a6255d0f011142e8b8c104239252908'

def tomorrow_forecast(cities):
    for city in cities:
        response = requests.get(f'http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days=2&aqi=no&alerts=no')
        data = response.json()
        maxtemp_c = data['forecast']['forecastday'][1]['day']['maxtemp_c']
        mintemp_c = data['forecast']['forecastday'][1]['day']['mintemp_c']
        avghumidity = data['forecast']['forecastday'][1]['day']['avghumidity']
        maxwind_kph = data['forecast']['forecastday'][1]['day']['maxwind_kph']

        wind_dir = 'Uknown'
        hours = data['forecast']['forecastday'][1]['hour']
        for hour in range(0, 24):
            if hours[hour]['wind_kph'] == maxwind_kph:
                wind_dir = hours[hour]['wind_dir']
            else:
                continue
        print(maxtemp_c, mintemp_c, avghumidity, maxwind_kph, wind_dir)

tomorrow_forecast(['Kyiv', 'Madrid'])