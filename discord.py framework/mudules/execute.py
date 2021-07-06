from commands.count import count
from mudules.discord.channel import channel
from commands.response import response
from commands.setactivity import setactivity
from mudules.discord.isBot import isBot
from mudules.discord.newCommand import newCommand
from mudules.discord.hasPrefix import hasPrefix
from commands.shutdown import shutdown


async def execute(message, client):
    # executed every message
    if hasPrefix(message) and not isBot(message):
        # if command needs prefix
        await newCommand(message,  "test", response)
        await newCommand(message,  "setactivity", setactivity, client)
        await newCommand(message,  "shutdown", shutdown, client)

    elif not isBot(message):
        # if command doesn't need prefix
        if channel(message, "counting"):
            await count(message)
