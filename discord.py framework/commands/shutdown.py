import discord
from mudules.loadJSON import loadJSON

token = loadJSON("./config.json")["token"]


async def shutdown(message, a, client):
    await client.logout()
