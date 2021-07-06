from commands.countModules.setID import setID
from commands.countModules.giveCoin import giveCoin
from commands.countModules.increaseWrong import increaseWrong
from mudules.saveJSON import saveJSON
from commands.countModules.increaseCorrect import increaseCorrect
from commands.countModules.increaseCount import increaseCount
from commands.countModules.getWrongMessage import getWrongMessage
from mudules.discord.emojiReact import emojiReact
from commands.countModules.checkLastUser import checkLastUser
from mudules.discord.getUser import getUser
from commands.countModules.numberCorrect import numberCorrect
from commands.countModules.setup import setup
from commands.countModules.getUserMessage import getUserMessage
from commands.countModules.isNumber import isNumber
from mudules.loadJSON import loadJSON
from mudules.discord.getArgs import getArgs
from mudules.discord.sendMessage import sendMessage


async def count(message):
    "counting minigame"
    args = getArgs(message)
    path = setup(message)

    if isNumber(message):
        data = loadJSON(path)
        number = numberCorrect(args, data)
        user = checkLastUser(message, data)
        if number and user:
            data = await increaseCount(data)
            data = await increaseCorrect(message, data)
            data = await giveCoin(message, data)
            data = setID(message, data)
            saveJSON(path, data)
            await emojiReact(message, "✅")

        elif number and not user:
            await sendMessage(message, getUser(message) + getUserMessage())
            data = await increaseWrong(message, data)
            saveJSON(path, data)
            await emojiReact(message, "⛔")

        else:
            await sendMessage(message, getUser(message) + getWrongMessage(data))
            data = await increaseWrong(message, data)
            saveJSON(path, data)
            await emojiReact(message, "⛔")
