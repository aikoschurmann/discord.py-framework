from commands.countModules.checkLastUser import checkLastUser
from commands.countModules.getCount import getCount
from commands.countModules.getNumber import getNumber
from json import load
from mudules.loadJSON import loadJSON
from commands.countModules.getSettings import getSettings


def numberCorrect(args, data):

    if getNumber(args) == getCount(data) + 1:
        return True
    else:
        return False
