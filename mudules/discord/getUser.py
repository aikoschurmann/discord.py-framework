def getUser(message):
    "returns the user that send the message"
    return "<@!"+str(message.author.id)+"> "
