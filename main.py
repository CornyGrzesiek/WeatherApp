import requests
import datetime as dt
import time

API_KEY = "59cfaf0abc0da981bd5654fd569d9868"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?q="
CITY = input("Enter your city to see the weather!")


def unix_to_date(unix_timestamp):
    return time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(unix_timestamp))


url = BASE_URL + CITY + "&appid=" + API_KEY
response = requests.get(url).json()

weather_description = response["weather"][0]["description"]
temperature = response["main"]["temp"] - 273.15
temperature_feels_like = response["main"]["feels_like"] - 273.15
pressure = response["main"]["pressure"]
humidity = response["main"]["humidity"]
wind_speed = response["wind"]["speed"]
country = response["sys"]["country"]
sunrise = response["sys"]["sunrise"] - response["timezone"]
sunset = response["sys"]["sunset"] - response["timezone"]
print(f"The Weather in {CITY} ({country}) is {weather_description}, sunrise at {unix_to_date(sunrise)[11:]}"
      f" and sunset at {unix_to_date(sunset)[11:]}. \nThe temperature is {int(temperature)} but it feels like i"
      f"t is {int(temperature_feels_like)}, humidity is at {humidity}% \nThe wind speed is {wind_speed} km/h"
      f", pressure is at {pressure} hPA")
