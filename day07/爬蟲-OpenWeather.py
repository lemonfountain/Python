# 網路位置: https://api.openweathermap.org/data/2.5/weather?q={},tw&appid={}
import json
import requests
if __name__ == '__main__':
    city_name = 'taipei'
    country = 'tw'
    key = 'b3b6bc7e80936b4b33669afb5c86df3c'  # 放個人的key OpenWeather
    url = 'https://api.openweathermap.org/data/2.5/weather?q={},{}&appid={}'.format(city_name, country, key)
    print(url)
    data = json.loads(requests.get(url).text)
    print(data)
    weather_main = data['weather'][0]['main']  # 選取 整個data 中的 第一列(0)
    weather_description = data['weather'][0]['description']
    weather_temp = '{:.2f}'.format(data['main']['temp'] - 273.15)
    weather_feels_like = '{:.2f}'.format(data['main']['feels_like'] - 273.15)
    weather_humidity = '{}%'.format(data['main']['humidity'])
    weather_clouds = '{}%'.format(data['clouds']['all'])
    weather_wind_speed = '{} m/s'.format(data['wind']['speed'])
    city_name = data['name']
    country = data['sys']['country']

    print(weather_temp)
    # 建立weather的 字典數組
    weather = {}
    weather.setdefault("天氣狀態:", weather_main)
    weather.setdefault("天氣敘述:", weather_description)
    weather.setdefault("現在溫度:", weather_temp)
    weather.setdefault("體感溫度:", weather_feels_like)
    weather.setdefault("現在濕度:", weather_humidity)
    weather.setdefault("雲層覆蓋:", weather_clouds)
    weather.setdefault("每秒風速::", weather_wind_speed)
    weather.setdefault('城市:', city_name)
    weather.setdefault('國家:', country)
    print(weather)
# 根據key值,逐一將字典資料輸出
    for key in weather.keys():
        print(key, weather[key])


