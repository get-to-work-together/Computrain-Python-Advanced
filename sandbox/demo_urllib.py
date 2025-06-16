import urllib.request
import json

city = input('Which city? ')

url  = 'http://api.openweathermap.org/data/2.5/weather'
url += '?appid=d1526a9039658a6f76950cff21823aff'
url += '&units=metric'
url += '&mode=json'
url += '&q=' + city

print(url)

site = urllib.request.urlopen(url)

if site.status == 200:
    response = str(site.read(), encoding='UTF-8')

    d = json.loads(response)

    temperature = d['main']['temp']
    description = d['weather'][0]['description']

    print(f'Temperature in {city} is {temperature}° with {description}')

else:
    print('Could not get weather information for ' + city)