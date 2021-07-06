from mudules.loadJSON import loadJSON


def getSettings(path):
    return loadJSON(path)["settings"]
