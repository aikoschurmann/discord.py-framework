def channel(message, channelName):
    "checks if given message was send in given channel"
    if message.channel.name == channelName:
        return True
    else:
        return False
