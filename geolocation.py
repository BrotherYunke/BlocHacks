import urllib.request
import json


def createJsonFile(info_array):
    for thing in info_array:
        thing = str(thing)
    f = open("data.json","w+")
    with f as output:
        jsonData = json.dumps(info_array)
        with f as a:
            json.dump(jsonData, a)

# Automatically geolocate the connecting IP
f = urllib.request.urlopen('http://freegeoip.net/json/')
json_string = f.read()
f.close()


location = json.loads(json_string)
location_city = location['city']
location_state = location['region_name']
location_country = location['country_name']
location_latitude = location['latitude']
location_longitude = location['longitude']

info_array = [location_country, location_longitude, location_latitude]
createJsonFile(info_array)
