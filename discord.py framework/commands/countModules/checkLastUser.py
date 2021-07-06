from commands.countModules.getSettings import getSettings


def checkLastUser(message, data):
    settings = data["settings"]
    if not data["lastCount"] == message.author.id:
        return True
    elif settings["repeat"]:
        return True
    else:
        return False
