import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests
import time
import csv
import random

from api_keys import api_key

citylistpath = "city.list.json"

city_list_df = pd.read_json(citylistpath)
cityidlist = list(city_list_df['id'])
cityids = random.sample(cityidlist, 500)
print(len(cityids))

url = "http://api.openweathermap.org/data/2.5/weather?units=imperial"
namelist = []
cityidlist = []
latitudelist = []
longitudelist = []
temperaturelist = []
humiditylist = []
cloudinesslist = []
windspeedlist = []
countrylist = []

for cityid in cityids:
        query_url = url + "&appid=" + api_key + "&id=" + str(cityid)
        weather_response = requests.get(query_url)
        weather_json = weather_response.json()
        name = weather_json["name"]
        namelist.append(weather_json['name'])
        cityidlist.append(weather_json['id'])
        latitudelist.append(weather_json['coord']['lat'])
        longitudelist.append(weather_json['coord']['lon'])
        temperaturelist.append(weather_json['main']['temp'])
        humiditylist.append(weather_json['main']['humidity'])
        cloudinesslist.append(weather_json['clouds']['all'])
        windspeedlist.append(weather_json['wind']['speed'])
        countrylist.append(weather_json['sys']['country'])
        
        print(name+","+weather_json['sys']['country']+","+str(cityid))
        print(url+"&id="+str(cityid))
        
weather_dictionary = {
    "Name": namelist,
    "ID": cityidlist,
    "Country": countrylist,
    "Cloudiness": cloudinesslist,
    "Temperature": temperaturelist,
    "Latitude": latitudelist,
    "Longitude": longitudelist,
    "Humidity": humiditylist,
    "Wind Speed": windspeedlist
}

weather_df = pd.DataFrame(weather_dictionary, columns=("Name", "ID", "Country", "Cloudiness", "Temperature", "Latitude", "Longitude", "Humidity", "Wind Speed"))

plt.scatter(weather_df["Latitude"],weather_df["Temperature"], alpha = 0.5)
plt.title("Temperature vs. Latitude")
plt.xlabel("Latitude")
plt.ylabel("Temperature (F)")
plt.savefig("Output/Temperature.png")
plt.show()

plt.scatter(weather_df["Latitude"],weather_df["Humidity"], alpha = 0.75)
plt.title("Humidity vs. Latitude")
plt.xlabel("Latitude")
plt.ylabel("Humidity (%)")
plt.savefig("Output/Humidity.png")
plt.show()

plt.scatter(weather_df["Latitude"],weather_df["Cloudiness"], alpha = 0.75)
plt.title("Cloudiness vs. Latitude")
plt.xlabel("Latitude")
plt.ylabel("Cloudiness (%)")
plt.savefig("Output/Cloudiness.png")
plt.show()

plt.scatter(weather_df["Latitude"],weather_df["Wind Speed"], alpha= 0.75)
plt.title("Wind Speed vs Latitude")
plt.xlabel("Latitude")
plt.ylabel("Wind Speed (mph)")
plt.savefig("Output/Wind Speed.png")
plt.show()
