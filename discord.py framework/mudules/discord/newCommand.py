from asyncio.windows_events import INFINITE
from mudules.discord.getArgs import getArgs
from mudules.getPrefix import getPrefix
from mudules.loadJSON import loadJSON

prefix = getPrefix()


async def newCommand(message,  command, function, client=None):
    "makes a new Discord command"
    a = getArgs(message)
    c = a[0].lower()

    if command == c:
        await function(message, a, client)
