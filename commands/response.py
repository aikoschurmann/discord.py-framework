
import discord


async def response(message, a):
    await sendMessage(message, getUser(message) + "it works!")
