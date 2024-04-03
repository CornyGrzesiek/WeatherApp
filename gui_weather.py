import time
import requests
from tkinter import *

API_KEY = "59cfaf0abc0da981bd5654fd569d9868"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?q="


def unix_to_date(unix_timestamp, unix_timezone):
    return time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(unix_timestamp + unix_timezone))


def display_input(event=None):
    try:
        city = entry.get()
        url = BASE_URL + city + "&appid=" + API_KEY
        response = requests.get(url).json()
        if response["cod"] == 200:
            weather_description = response["weather"][0]["description"]
            temperature = response["main"]["temp"] - 273.15
            temperature_feels_like = response["main"]["feels_like"] - 273.15
            pressure = response["main"]["pressure"]
            humidity = response["main"]["humidity"]
            wind_speed = response["wind"]["speed"]
            country = response["sys"]["country"]
            timezone = response["timezone"]
            time_there = unix_to_date(response["dt"], timezone)[11:]
            sunrise = unix_to_date(response["sys"]["sunrise"], timezone)[11:]
            sunset = unix_to_date(response["sys"]["sunset"], timezone)[11:]
            label_info.config(text=f"The Weather in {city[0].upper() + city[1:].lower()} ({country}) is {weather_description} \n"
                                   f"time there is: {time_there} \n "
                                   f"sunrise at {sunrise} and sunset at {sunset}.\n"
                                   f"The temperature is {int(temperature)}, feels like "
                                   f"{int(temperature_feels_like)}, humidity is at {humidity}% \n"
                                   f"The wind speed is {wind_speed} km/h, pressure is at {pressure} hPA")
            icon_url = "http://openweathermap.org/img/wn/" + response["weather"][0]["icon"] + ".png"
            icon_data = requests.get(icon_url).content
            icon_photo = PhotoImage(data=icon_data)
            icon_label.config(image=icon_photo)
            icon_label.image = icon_photo
            entry.delete(0, END)
        else:
            label_info.config(text="City not found!")
            icon_label.config(image="")
            entry.delete(0, END)
    except Exception as e:
        print("An error occurred:", e)


def focus_in_entry(event):
    if entry.get() == "Enter your city":
        entry.delete(0, END)
        entry.config(fg="black")


root = Tk()
root.geometry("500x550")
root.resizable(False, False)
root.configure(bg="lightblue")

form = Frame(root, bg="lightblue", width=500, height=500, padx=15, pady=15)
label = Label(form, text="Enter city to see the weather!", bg="lightblue", fg="black", font="Helvetica 12 bold")
label.pack()

entry = Entry(form, font="Helvetica 12", fg="gray")
entry.bind("<Return>", display_input)
entry.bind("<FocusIn>", focus_in_entry)
entry.insert(0, "Enter your city")
entry.pack(padx=15, pady=15)

button = Button(form, text="Submit City", command=display_input)
button.pack()

icon_label = Label(form, bg="lightblue")
icon_label.pack(padx=15, pady=15)

label_info = Label(form, text="", bg="lightblue", fg="black", font="Helvetica 12 bold")
label_info.pack()

form.pack()
root.mainloop()
