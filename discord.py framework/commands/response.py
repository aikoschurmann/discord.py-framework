from mudules.discord.sendMessage import sendMessage
import discord


async def response(message, a, client):
    await sendMessage(message, "it works!")
