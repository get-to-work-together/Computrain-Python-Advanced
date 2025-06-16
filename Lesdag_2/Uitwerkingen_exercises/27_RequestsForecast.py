import requests
from datetime import datetime

city = input('City? ')

url = "http://api.openweathermap.org/data/2.5/forecast/daily"
url += "?appid=d1526a9039658a6f76950cff21823aff"
url += "&units=metric"
url += "&mode=json"
url += "&q=" + city

print(url)

response = requests.get(url)

if (response.status_code == 200):
    body = response.text
    decoded = response.json()

    for d in decoded['list']:
        dt = datetime.fromtimestamp(d['dt'])
        t = d['temp']['day']
        print(f'Op {dt} wordt het {t:7.2f}')

else:
    print("Error for city %s" % (city))
