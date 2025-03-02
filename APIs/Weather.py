import requests
import consts as keys

def get_weather(city_name):
    try:
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": city_name,
            "appid": keys.OPEN_WEATHER_API,
            "units": "metric"  
        }
        response = requests.get(base_url, params=params)
        print(response)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return  

# response_data = {
#     'coord': {'lon': 24.0232, 'lat': 49.8383}, 
#     'weather': [{'id': 802, 
#                  'main': 'Clouds', 
#                  'description': 'scattered clouds', 
#                  'icon': '03n'}], 
#     'base': 'stations', 
#     'main': {'temp': 13.16, 
#              'feels_like': 11.97, 
#              'temp_min': 13.16, 
#              'temp_max': 13.16,
#              'pressure': 1017, 
#              'humidity': 55,
#              'sea_level': 1017,
#              'grnd_level': 981},
#     'visibility': 10000,
#     'wind': {'speed': 6.37, 
#              'deg': 142, 
#              'gust': 16.62}, 
#     'clouds': {'all': 45}, 
#     'dt': 1714598547, 
#     'sys': {'country': 'UA', 
#             'sunrise': 1714618706, 
#             'sunset': 1714671788}, 
#     'timezone': 10800, 
#     'id': 702550, 
#     'name': 'Lviv', 
#     'cod': 200}
