import requests
import pandas as pd
import json

with open('config.json', 'r') as f:
    config = json.load(f)

api_key = config['api_key']
pd.set_option("display.max_columns", None)

def tomorrow_forecast(cities):
    '''
    Accepts list of cities, returns tomorrow forecast
    :param cities: List
    :return: df
    '''

    forecast = {'max temperature': [], 'min temperature': [], 'average humidity': [],
                'max wind speed': [], 'wind direction': []}


    for city in cities:
        try:
            response = requests.get(f'http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days=2&aqi=no&alerts=no')
            data = response.json()
            data = data['forecast']['forecastday'][1]

            maxtemp_c = data['day']['maxtemp_c']
            mintemp_c = data['day']['mintemp_c']
            avghumidity = data['day']['avghumidity']
            maxwind_kph = data['day']['maxwind_kph']
            wind_dir = 'Unknown'

            for hour in range(0, 24):
                if data['hour'][hour]['wind_kph'] == maxwind_kph:
                    wind_dir = data['hour'][hour]['wind_dir']
                    break
                else:
                    continue

            forecast['max temperature'].append(maxtemp_c)
            forecast['min temperature'].append(mintemp_c)
            forecast['average humidity'].append(avghumidity)
            forecast['max wind speed'].append(maxwind_kph)
            forecast['wind direction'].append(wind_dir)

        except KeyError:
            cities.remove(city)
            print(f'Unable to load forecast for {city}. City does not exist')
        except requests.exceptions.RequestException:
            print('Encountered problem with request')
            raise


    df = pd.DataFrame(data=forecast, index=cities)
    return df


print(tomorrow_forecast(['Kyiv', 'Madrid', 'Chisinau', 'Amsterdam', 'ddd']))
