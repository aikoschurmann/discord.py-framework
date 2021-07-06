from mudules.saveJSON import saveJSON
from commands.countModules.increaseCorrect import increaseCorrect
from commands.countModules.increaseCount import increaseCount
from commands.countModules.getWrongMessage import getWrongMessage
from mudules.discord.emojiReact import emojiReact
from commands.countModules.checkLastUser import checkLastUser
from commands.countModules.getCount import getCount
from mudules.discord.getUser import getUser
from commands.countModules.numberCorrect import numberCorrect
from commands.countModules.getSettings import getSettings
from commands.countModules.setup import setup
from commands.countModules.getUserMessage import getUserMessage
from commands.countModules.isNumber import isNumber
from mudules.loadJSON import loadJSON
from mudules.discord.getArgs import getArgs
from mudules.discord.sendMessage import sendMessage


async def count(message):
    args = getArgs(message)
    path = setup(message)

    if isNumber(message):
        data = loadJSON(path)
        number = numberCorrect(args, data)
        user = checkLastUser(message, data)
        if number and user:
            data = await increaseCount(data)
            await saveJSON(path, data)
            data = await increaseCorrect(message, data)
            await saveJSON(path, data)
            await emojiReact(message, "✅")

        elif number and not user:
            await sendMessage(message, getUser(message) + getUserMessage())
            await emojiReact(message, "⛔")
        else:
            await sendMessage(message, getUser(message) + getWrongMessage(data))
            await emojiReact(message, "⛔")
