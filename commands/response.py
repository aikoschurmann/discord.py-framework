
import discord


async def response(bot):
    await bot.SendMessage(bot.GetUser() + "it works!")
