from asyncio.windows_events import INFINITE
from bot.Link import Link
from mudules.isFile import isFile
from bot.Count import Count
from mudules.loadJSON import loadJSON
from mudules.saveJSON import saveJSON
import discord
import copy


class Flux(object):
    def __init__(self, message, client):
        self.message = message
        self.client = client

    def HasPrefix(self):
        "checks if message starts with prefix given in config.json"
        prefix = self.GetPrefix()
        return self.message.content.startswith(prefix)

    def GetPrefix(self):
        "returns prefix specified in config.json"
        return loadJSON("./config.json")["prefix"]

    def IsBot(self) -> bool:
        "checks if message comes from a bot"
        return self.message.author.bot

    def Channel(self, channelName: str) -> bool:
        if self.message.channel.name == channelName:
            return True
        else:
            return False

    def Role(self, roleName: str) -> bool:
        roles = self.message.author.roles
        for role in roles:
            if role.name == roleName:
                return True
        return False

    def GetArgs(self):
        "Returns arguments of given message"
        prefix = self.GetPrefix()
        if self.HasPrefix():
            sliceObject = slice(len(prefix), INFINITE)
            a = self.message.content[sliceObject].split(" ")

        else:
            a = self.message.content.split(" ")
        return a

    def GetUser(self):
        "returns the user that send the message"
        return "<@!"+str(self.message.author.id)+"> "

    def logArgs(self):
        "prints arguments to console of given message"
        prefix = self.GetPrefix()
        if self.HasPrefix():
            sliceObject = slice(len(prefix), INFINITE)
            a = self.message.content[sliceObject].split(" ")

        else:
            a = self.message.content.split(" ")
        print(a)

    def SaveMessage(self, path: str = "log.txt"):
        "saves message to given path"
        server = self.message.guild.name
        name = self.message.author.name + "#" + self.message.author.discriminator
        suffix = server + "  |  " + name + "  |  "
        line = suffix + self.message.content + "\n"
        with open(path, 'a') as f:
            f.write(line)

    async def SetActivity(self, activity: str):
        "sets the activity of the bot"
        data = loadJSON("./config.json")
        data["activity"] = activity
        saveJSON("./config.json", data)
        await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=activity))

    async def SendMessage(self, text: str):
        "sends a message in the channel the message was recieved in"
        await self.message.channel.send(text)

    async def EmojiReact(self, emoji: str):
        "replies with a emoji to given message"
        await self.message.add_reaction(emoji)

    async def NewCommand(self, command: str, function, args: list[int] = [], exact: bool = False):
        "makes a new Discord command"
        a = self.GetArgs()
        b = copy.copy(a)
        b.pop(0)
        correct = False
        index = 0
        if command == a[0].lower():
            if exact:
                if len(b) == len(args):
                    if len(args) == 0:
                        correct = True
                    else:
                        while index < len(args):
                            if b[index] == args[index]:
                                correct = True
                                index += 1
                            else:
                                correct = False
                                break
                else:
                    print("EXACT MODE : The message was " + str(len(b)) +
                          " arguments long but " + str(len(args)) + " were needed")
                    print("needed :" + str(args))
                    print("given :" + str(b))
            else:
                if len(b) >= len(args):
                    if len(args) == 0:
                        correct = True
                    else:
                        while index < len(args):
                            if b[index] == args[index]:
                                correct = True
                                index += 1
                            else:
                                correct = False
                                break
        if correct:
            await function(self)

    async def Count(self):
        game = Count(self)
        number = game.NumberCorrect()
        user = game.CheckLastUser()
        if number and user:
            game.IncreaseCount()
            game.IncreaseCorrect()
            game.SaveData()
            await self.EmojiReact("✅")

    async def Linker(self):
        link = Link(self)
        await self.NewCommand("newlink", link.NewLink)
        await self.NewCommand("setorigin", link.SetOrigin)

    async def LinkerSender(self):
        link = Link(self)

        await link.AutoMessage()
