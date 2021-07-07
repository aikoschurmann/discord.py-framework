from bot.execute import execute
from mudules.loadJSON import loadJSON
import discord

client = discord.Client()
token = loadJSON("./config.json")["token"]


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    await execute(message, client)
    #saveMessage(message, "log.txt")


client.run(token)
