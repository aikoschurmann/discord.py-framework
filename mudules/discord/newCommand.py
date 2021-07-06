from asyncio.windows_events import INFINITE
from mudules.discord.getArgs import getArgs
import copy


async def newCommand(message,  command, function, client=None, args=[], exact=False):
    "makes a new Discord command"
    a = getArgs(message)
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
        if client == None:
            await function(message, a)
        else:
            await function(message, a, client)
