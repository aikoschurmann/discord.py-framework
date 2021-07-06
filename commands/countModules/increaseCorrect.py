import collections
import operator


async def increaseCorrect(message, data):
    "gives user a correct count"
    if message.author.name + "#" + message.author.discriminator not in data["correct"]:
        data["correct"][message.author.name + "#" +
                        message.author.discriminator] = 1
    else:
        data["correct"][message.author.name + "#" +
                        message.author.discriminator] += 1
        data["correct"] = collections.OrderedDict(data["correct"])
        data["correct"] = dict(
            sorted(data["correct"].items(), key=operator.itemgetter(1), reverse=True))

    return data
