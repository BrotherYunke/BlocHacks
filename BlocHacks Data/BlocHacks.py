import json
import sys
data  = open('LocationHistory.json')
sys.stdout = open('log.json', 'w')

def FindCoordinates():
    json_string = data.read()
    json_data = json.loads (json_string)

    locations = json_data["data"]["items"]

    for location in locations:
        sys.stdout = open('log.json', 'a')
        print (location["latitude"], location["longitude"])

    fileHandle = open('LocationHistory.json', "r")
    lineList = fileHandle.readlines()
    fileHandle.close()

    sys.stdout = open('log.json', 'a')
    print (lineList[-4])
    sys.stdout = open('log.json', 'a')
    print (lineList[-5])

    data.close()

FindCoordinates()

