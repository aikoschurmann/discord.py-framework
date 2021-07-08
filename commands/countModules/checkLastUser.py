

def checkLastUser(message, data):
    "checks if user is allowed to send"
    settings = data["settings"]
    if not data["lastCount"] == message.author.id:
        return True
    elif settings["repeat"]:
        return True
    else:
        return False
