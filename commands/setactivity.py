from mudules.discord.getUser import getUser
from mudules.discord.sendMessage import sendMessage
from mudules.discord.setActivity import setActivity
from mudules.discord.displayActivity import displayActivity
import discord


async def setactivity(message, a, client):

    if len(a) > 1:
        print(a)
        result = ""
        a.pop(0)
        for word in a:
            result = result + word + " "
        setActivity(result)
        await displayActivity(client)
    else:
        await sendMessage(message, getUser(message) + "You need to specify an activity!")
