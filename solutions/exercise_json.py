import json

s = '{"coord":{"lon":4.8897,"lat":52.374},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"base":"stations","main":{"temp":17.77,"feels_like":17.82,"temp_min":16.58,"temp_max":19.38,"pressure":1023,"humidity":85},"visibility":10000,"wind":{"speed":0.45,"deg":70,"gust":0.89},"clouds":{"all":0},"dt":1631000419,"sys":{"type":2,"id":2012552,"country":"NL","sunrise":1630990907,"sunset":1631038530},"timezone":7200,"id":2759794,"name":"Amsterdam","cod":200}'

d = json.loads(s)

print(d['coord'])