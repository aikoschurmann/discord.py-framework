
import discord


async def setactivity(self, message, a, client):

    if len(a) > 1:
        print(a)
        result = ""
        a.pop(0)
        for word in a:
            result = result + word + " "
        self.SetActivity(result)
