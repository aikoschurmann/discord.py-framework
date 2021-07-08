from mudules.loadJSON import loadJSON
from mudules.saveJSON import saveJSON
from mudules.isFile import isFile
from mudules.makeDir import makeDir
import collections
import operator


class Count():

    def __init__(self, flux):
        self.message = flux.message
        self.flux = flux
        self.args = flux.GetArgs()
        self.data = self.Setup()

    def IsNumber(self, index=0):
        "checks if argument at given index is a number"
        return self.args[index].isnumeric()

    def NumberCorrect(self, increment=1):
        if self.IsNumber():
            "checks if number is correct"
            if self.GetNumber() == self.GetCount() + increment:
                return True
            else:
                return False

    def GetNumber(self):
        return int(self.args[0])

    def GetCount(self):
        return int(self.data["count"])

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

    def Setup(self):
        dirpath = self.getDirPath()
        filepath = self.GetFilePath()
        makeDir(dirpath)
        if not isFile(filepath):
            saveJSON(filepath, self.Template())

        data = loadJSON(filepath)
        return data

    def GetFilePath(self):
        dirpath = "Serverdata"
        filepath = dirpath + "/" + str(self.message.guild.id) + ".json"
        return filepath

    def getDirPath(self):
        dirpath = "Serverdata"
        return dirpath

    def CheckLastUser(self):
        "checks if user is allowed to send"
        settings = self.data["settings"]
        if not self.data["lastCount"] == self.message.author.id:
            return True
        elif settings["repeat"]:
            return True
        else:
            return False

    def IncreaseCount(self):
        "increases minigame count"
        self.data["count"] += 1

    def IncreaseIncorrect(self):
        "gives user a correct count"
        if self.message.author.name + "#" + self.message.author.discriminator not in self.data["incorrect"]:
            self.data["incorrect"][self.message.author.name + "#" +
                                   self.message.author.discriminator] = 1
        else:
            self.data["incorrect"][self.message.author.name + "#" +
                                   self.message.author.discriminator] += 1
            self.data["incorrect"] = collections.OrderedDict(
                self.data["incorrect"])
            self.data["incorrect"] = dict(
                sorted(self.data["incorrect"].items(), key=operator.itemgetter(1), reverse=True))

    def IncreaseCorrect(self):
        "gives user a correct count"
        if self.message.author.name + "#" + self.message.author.discriminator not in self.data["correct"]:
            self.data["correct"][self.message.author.name + "#" +
                                 self.message.author.discriminator] = 1
        else:
            self.data["correct"][self.message.author.name + "#" +
                                 self.message.author.discriminator] += 1
            self.data["correct"] = collections.OrderedDict(
                self.data["correct"])
            self.data["correct"] = dict(
                sorted(self.data["correct"].items(), key=operator.itemgetter(1), reverse=True))

    def SaveData(self):
        saveJSON(self.GetFilePath(), self.data)
