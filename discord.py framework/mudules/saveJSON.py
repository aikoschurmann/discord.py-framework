import json


async def saveJSON(path, data):
    "saves data to path in json format"
    with open(path, 'w') as outfile:
        json.dump(data, outfile, indent=4)
