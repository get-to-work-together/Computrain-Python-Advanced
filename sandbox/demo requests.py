from datetime import datetime
import requests
import locale

locale.setlocale(locale.LC_ALL, 'nl_nl')

city = input('Which city? : ')

url = "http://api.openweathermap.org/data/2.5/weather"
url += "?appid=d1526a9039658a6f76950cff21823aff"
url += "&units=metric"
url += "&mode=json"
url += "&q=" + city

response = requests.get(url)

if (response.status_code == 200):
    decoded = response.json()
    temperature = decoded['main']['temp']
    print(f'Het is nu {temperature:.0f}°C in {city}.')
else:
    print("Error for city {city}")


# ---------------------------------------
# voor de komende dagen

url = "http://api.openweathermap.org/data/2.5/forecast/daily"
url += "?appid=d1526a9039658a6f76950cff21823aff"
url += "&units=metric"
url += "&mode=json"
url += "&cnt=16"
url += "&q=" + city

response = requests.get(url)

print(f'\nVoorspelling voor de komende dagen:')
if (response.status_code == 200):
    decoded = response.json()
    for day_forecast in decoded['list']:
        datum = datetime.fromtimestamp(day_forecast['dt'])
        temperature = day_forecast['temp']['day']
        print(f'{datum.strftime('%A %d %B'):20} : {temperature:.0f}°C.')
else:
    print("Error for city {city}")