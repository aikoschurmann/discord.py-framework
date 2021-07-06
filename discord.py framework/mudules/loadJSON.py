import json


def loadJSON(path):
    "returns json data at given path"
    with open(path) as json_file:
        data = json.load(json_file)
    return data
