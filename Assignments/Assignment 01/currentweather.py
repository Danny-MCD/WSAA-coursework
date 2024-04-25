#   Program to print out current weather from api open-meteo
#   Author: Daniel Mc Donagh

import requests
import json

url = "https://api.open-meteo.com/v1/forecast?latitude=53.82&longitude=-9.5&current=temperature_2m"
response = requests.get(url)
data=response.json()

with open("currenttemperature2m.json", "w") as fp:
   json.dump(data, fp)

current = data["current"]               # Retrieves object current from data
temp2m = current["temperature_2m"]      # Retrieves object temp2m from current

print(temp2m, chr(176), "C")