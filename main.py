import json
from datetime import datetime
import pandas as pandas
import requests

city_name = "Bangkok"
base_url = "https://api.openweathermap.org/data/2.5/weather?q="

with open("credentials.txt", 'r') as f:
    api_key = f.read()

full_url = base_url + city_name + "&appid=" + api_key

r = requests.get(full_url)
data = r.json()
print(data)

