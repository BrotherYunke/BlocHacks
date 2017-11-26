import json

def createJsonFile(array):
    f = open("data.json","w+")
    with f as output:
        jsonData = json.dumps(array)
        with f as a:
            json.dump(jsonData, a)
