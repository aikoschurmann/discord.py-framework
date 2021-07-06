from mudules.discord.getArgs import getArgs


def isNumber(message, index=0):
    "checks if argument at given index is a number"
    args = getArgs(message)
    return args[index].isnumeric()
