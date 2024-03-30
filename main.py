import requests
import datetime as dt
import time

API_KEY = "shhhh"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?q="
CITY = input("Enter your city to see the weather!")
url = BASE_URL + CITY + "&appid=" + API_KEY


def unix_to_date(unix_timestamp, unix_timezone):
    return time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(unix_timestamp + unix_timezone))


try:
    response = requests.get(url).json()
    if response['cod'] == 200:
        weather_description = response["weather"][0]["description"]
        temperature = response["main"]["temp"] - 273.15
        temperature_feels_like = response["main"]["feels_like"] - 273.15
        pressure = response["main"]["pressure"]
        humidity = response["main"]["humidity"]
        wind_speed = response["wind"]["speed"]
        country = response["sys"]["country"]
        timezone = response["timezone"]
        sunrise = unix_to_date(response["sys"]["sunrise"], timezone)[11:]
        sunset = unix_to_date(response["sys"]["sunset"], timezone)[11:]
        print(f"The Weather in {CITY} ({country}) is {weather_description}, sunrise at {sunrise}"
              f" and sunset at {sunset}. \nThe temperature is {int(temperature)} but it feels like i"
              f"t is {int(temperature_feels_like)}, humidity is at {humidity}% \nThe wind speed is {wind_speed} km/h"
              f", pressure is at {pressure} hPA")
    else:
        print("City not found!")
except Exception as e:
    print("an error occurred:", e)
