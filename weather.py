import requests
import json
import math

WEATHER_API_KEY = 'f3376e388164f7d2ad5daf896c204883'

WEATHER_MAIN = {
    'Rain': '🌧',
    'Clear': '☀️',
    'Clouds': '🌤',
    'Snow': '🌨',
}


def get_weather():
    info_msg = ''
    
    response = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=55.78&lon=37.49&appid=f3376e388164f7d2ad5daf896c204883&units=metric')
    if response.status_code == 200:
        data = response.json()

        temp = math.trunc(round(data['main']['temp'], 0))
        feels_like = math.trunc(round(data['main']['feels_like'], 0))
        weather = ''
        try:
            weather = WEATHER_MAIN[data['weather'][0]['main']]
        except:
            weather = ''
     
        info_msg = f'Сегодня {("+" if temp > 0 else "") + str(temp)}°C (ощущается как {("+" if feels_like > 0 else "") + str(feels_like)}°C) {weather}'
    else:
        info_msg = 'Пока не знаю, спроси меня позже'
    
    return info_msg
