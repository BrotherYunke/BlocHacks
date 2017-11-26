import urllib.request
import json

def createJsonFile(array):
    for thing in array:
        thing = str(thing)
    f = open("data.json","w+")
    data = json.dumps(array)
    f.write(data)
    f.close()

# Automatically geolocate the connecting IP
f = urllib.request.urlopen('http://freegeoip.net/json/')
json_string = f.read()
location = json.loads(json_string)

location_city = location['city']
location_state = location['region_name']
location_country = location['country_name']
location_latitude = location['latitude']
location_longitude = location['longitude']

array = {'Country':location_country, 'City':location_city, 'Longitude':location_longitude, 'Latitude':location_latitude}
createJsonFile(array)
