from mudules.discord.getUser import getUser
from mudules.discord.sendMessage import sendMessage
import discord


async def response(message, a):
    await sendMessage(message, getUser(message) + "it works!")
