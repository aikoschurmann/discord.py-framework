from bot.Count import Count
from commands.countModules.setID import setID
from commands.countModules.giveCoin import giveCoin
from commands.countModules.increaseWrong import increaseWrong
from mudules.saveJSON import saveJSON
from commands.countModules.increaseCorrect import increaseCorrect
from commands.countModules.increaseCount import increaseCount
from commands.countModules.getWrongMessage import getWrongMessage
from commands.countModules.checkLastUser import checkLastUser
from commands.countModules.numberCorrect import numberCorrect
from commands.countModules.getUserMessage import getUserMessage
from commands.countModules.isNumber import isNumber
from mudules.loadJSON import loadJSON


async def count(self, message):
    "counting minigame"
    args = self.GetArgs()
    path = self.CountSetup()

    count = Count(message, self)

    if count.IsNumber():
        print("yay")
        data = loadJSON(path)
        number = numberCorrect(args, data)
        user = checkLastUser(message, data)
        if number and user:
            data = await increaseCount(data)
            data = await increaseCorrect(message, data)
            data = await giveCoin(message, data)
            data = setID(message, data)
            saveJSON(path, data)
            await self.EmojiReact("✅")

        elif number and not user:
            await self.SendMessage(self.GetUser(message) + getUserMessage())
            data = await increaseWrong(message, data)
            saveJSON(path, data)
            await self.EmojiReact("⛔")

        else:
            await self.SendMessage(self.GetUser(message) + getWrongMessage(data))
            data = await increaseWrong(message, data)
            saveJSON(path, data)
            await self.EmojiReact("⛔")
