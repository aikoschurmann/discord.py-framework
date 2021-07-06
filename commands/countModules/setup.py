from commands.countModules.template import template
from mudules.saveJSON import saveJSON
from mudules.isFile import isFile
from mudules.makeDir import makeDir


def setup(message):
    dirpath = "Serverdata"
    filepath = dirpath + "/" + str(message.guild.id) + ".json"
    makeDir(dirpath)
    if not isFile(filepath):
        saveJSON(filepath, template())
    return filepath
