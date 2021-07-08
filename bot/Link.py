
from mudules.makeDir import makeDir
from mudules.loadJSON import loadJSON
from mudules.saveJSON import saveJSON
from mudules.isFile import isFile


class Link():

    def __init__(self, flux):
        self.message = flux.message
        self.client = flux.client
        self.flux = flux
        self.args = flux.GetArgs()
        self.path = self.GetFilePath()
        self.dirpath = self.getDirPath()
        self.data = self.Setup()

    def HasLinks(self):
        if len(self.data["links"]) == 0:
            return False
        else:
            return True

    def GetFilePath(self):
        dirpath = "Serverdata"
        filepath = dirpath + "/" + str(self.message.guild.id) + ".json"
        return filepath

    def Template(self):
        return{
            "settings": {
                "repeat": True,
                "timeout": True,
                "reset": True,
                "reward": 1
            },
            "count": 0,
            "correct": {},
            "incorrect": {},
            "coins": {},
            "links": [],
            "origin": None,
            "lastCount": None
        }

    def getDirPath(self):
        dirpath = "Serverdata"
        return dirpath

    def Setup(self):
        if not isFile(self.path):
            makeDir(self.dirpath)
            saveJSON(self.path, self.Template())
        data = loadJSON(self.path)
        return data

    def IsNew(self):
        if self.id not in self.data["links"]:
            return True
        else:
            return False

    async def AutoMessage(self):
        if self.HasOrigin() and self.HasLinks():
            if str(self.message.channel.id) == self.data["origin"]:
                for ID in self.data["links"]:
                    if self.IsChannel(ID):
                        channel = await self.client.fetch_channel(ID)
                        await channel.send(self.message.content)

    def HasOrigin(self):
        if self.data["origin"] == None:
            return False
        else:
            return True

    async def SetOrigin(self, bot):

        if len(self.args) == 2:
            if self.args[1] == "this":
                self.args[1] = str(self.message.channel.id)
            if await self.IsChannel(self.args[1]):
                self.data["origin"] = self.id
                saveJSON(self.path, self.data)
                await bot.SendMessage(bot.GetUser() + "succes setting origin!")
            else:
                await bot.SendMessage(bot.GetUser() + "invalid channel ID!")

        else:
            await self.flux.SendMessage("please use .setorigin ID | .setorigin this")

    async def NewLink(self, bot):
        if len(self.args) == 2:
            if self.args[1] == "this":
                self.args[1] = str(self.message.channel.id)
            if await self.IsChannel(self.args[1]):

                if self.IsNew():
                    await bot.SendMessage(bot.GetUser() + "succes linking!")
                    self.data["links"].append(self.args[1])
                    saveJSON(self.path, self.data)
                else:
                    await bot.SendMessage(bot.GetUser() + "this id is already linked!")
            else:
                await bot.SendMessage(bot.GetUser() + "invalid channel ID!")

        else:
            await self.flux.SendMessage("please use .newlink ID | .newlink this")

    async def IsChannel(self, ID):
        self.id = ID
        await self.client.fetch_channel(ID)
        try:
            await self.client.fetch_channel(ID)
            return True
        except:
            return False
