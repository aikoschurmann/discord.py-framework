from mudules.loadJSON import loadJSON


def getPrefix():
    "returns prefix specified in config.json"
    return loadJSON("./config.json")["prefix"]
