from mudules.discord.displayActivity import displayActivity
from mudules.loadJSON import loadJSON
from mudules.saveJSON import saveJSON


def setActivity(activity):
    "sets the activity of the bot"
    data = loadJSON("./config.json")
    data["activity"] = activity
    saveJSON("./config.json", data)
