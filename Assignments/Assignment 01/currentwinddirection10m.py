#   Program to print current wind direction from api Open Meteo
#   Author:     Daniel Mc Donagh


import requests
import json

url = "https://api.open-meteo.com/v1/forecast?latitude=53.82&longitude=-9.5&current=wind_direction_10m"
response = requests.get(url)
data = response.json()

with open("currentwinddir10m.json", "w") as fp:         # Opens Json file in write mode
   json.dump(data, fp)                                  # Adds data to json file

current = data["current"]                               # Retrieves object current from data
winddir10m = current["wind_direction_10m"]              # Retrieves object winddir10m from current

print(winddir10m,chr(176))