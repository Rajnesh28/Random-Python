import csv
import random
from urllib import request
import json
import datetime

def get_weather_forecast(coords={'lat' : 199,'lon' : 121}):
    try:
        api_key = a6ccb5e29a8696bec8e1e05038c85c01
        url = f'api.openweathermap.org/data/2.5/forecast?lat={coords["lat"]}&lon={coords["lon"]}&appid={API key}'
        data = json.load(request.urlopen(url))

        forecast = {'city' : data['city']['name'],
                    'country' : data['city']['country'],    
                    'periods' : list()}
        for period in data['list'][0:9]:
            forecast['periods'].append({'timestamp'})
        

    except Exception as e:    

def get_twitter_trends():
    pass

def get_wikipedia_article()
    pass

if __name__ = '__main__':
    pass