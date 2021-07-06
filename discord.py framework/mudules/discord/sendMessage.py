import discord


async def sendMessage(message, text):
    "sends a message in the channel the message was recieved in"
    await message.channel.send(text)
