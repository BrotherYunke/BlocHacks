import urllib.request
import json

# Automatically geolocate the connecting IP
f = urllib.request.urlopen('http://freegeoip.net/json/')
json_string = f.read()
f.close()
# print(json_string)
location = json.loads(json_string)
# print(location)
location_city = location['city']
location_state = location['region_name']
location_country = location['country_name']
location_latitude = location['latitude']
location_longitude = location['longitude']
print(location_country)
print(location_latitude)
print(location_longitude)