import collections
import operator


async def giveCoin(message, data):
    "gives user a coin"
    coinsGiven = data["settings"]["reward"]
    if message.author.name + "#" + message.author.discriminator not in data["coins"]:
        data["coins"][message.author.name + "#" +
                      message.author.discriminator] = coinsGiven
    else:
        data["coins"][message.author.name + "#" +
                      message.author.discriminator] += coinsGiven
        data["coins"] = collections.OrderedDict(data["coins"])
        data["coins"] = dict(
            sorted(data["coins"].items(), key=operator.itemgetter(1), reverse=True))

    return data
