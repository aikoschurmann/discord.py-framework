def setID(message, data):
    data["lastCount"] = message.author.id
    return data
