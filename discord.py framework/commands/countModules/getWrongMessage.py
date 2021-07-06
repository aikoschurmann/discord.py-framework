from commands.countModules.getCount import getCount


def getWrongMessage(data):
    return "you officialy failed to increase `" + str(getCount(
        data)) + "` by 1 \n" + "for your info, that is supposed to be: `" + str(getCount(data)+1) + "`!"
