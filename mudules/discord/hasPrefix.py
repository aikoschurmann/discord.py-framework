from mudules.getPrefix import getPrefix


def hasPrefix(message):
    "checks if message starts with prefix given in config.json"
    prefix = getPrefix()
    return message.content.startswith(prefix)
