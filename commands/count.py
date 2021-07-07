from bot.Count import Count
from commands.countModules.setID import setID
from commands.countModules.giveCoin import giveCoin
from mudules.saveJSON import saveJSON
from commands.countModules.getWrongMessage import getWrongMessage
from commands.countModules.checkLastUser import checkLastUser
from commands.countModules.getUserMessage import getUserMessage
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
