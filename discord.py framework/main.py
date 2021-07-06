from mudules.execute import execute
from mudules.discord.setActivity import setActivity
from mudules.discord.displayActivity import displayActivity
from mudules.discord.saveMessage import saveMessage
from mudules.loadJSON import loadJSON
import discord

client = discord.Client()
token = loadJSON("./config.json")["token"]


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await displayActivity(client)


@client.event
async def on_message(message):
    await execute(message, client)
    saveMessage(message, "log.txt")


client.run(token)
