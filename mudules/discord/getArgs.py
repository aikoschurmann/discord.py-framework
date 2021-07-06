from asyncio.windows_events import INFINITE
from mudules.discord.hasPrefix import hasPrefix

from mudules.getPrefix import getPrefix
prefix = getPrefix()


def getArgs(message):
    "Returns arguments of given message"
    if hasPrefix(message):
        sliceObject = slice(len(prefix), INFINITE)
        a = message.content[sliceObject].split(" ")

    else:
        a = message.content.split(" ")
    return a
