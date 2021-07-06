from mudules.loadJSON import loadJSON
import discord


async def displayActivity(client):
    "updates the activity visualy"
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=loadJSON("./config.json")["activity"]))
