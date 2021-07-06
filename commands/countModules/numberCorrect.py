from commands.countModules.checkLastUser import checkLastUser
from commands.countModules.getCount import getCount
from commands.countModules.getNumber import getNumber
from json import load
from mudules.loadJSON import loadJSON
from commands.countModules.getSettings import getSettings


def numberCorrect(args, data, increment=1):
    "checks if number is correct"
    if getNumber(args) == getCount(data) + increment:
        return True
    else:
        return False
