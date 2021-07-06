import collections
import operator


async def increaseWrong(message, data):
    "gives user a wrong count"
    if message.author.name + "#" + message.author.discriminator not in data["incorrect"]:
        data["incorrect"][message.author.name + "#" +
                          message.author.discriminator] = 1
    else:
        data["incorrect"][message.author.name + "#" +
                          message.author.discriminator] += 1
        data["incorrect"] = collections.OrderedDict(data["incorrect"])
        data["incorrect"] = dict(
            sorted(data["incorrect"].items(), key=operator.itemgetter(1), reverse=True))

    return data
