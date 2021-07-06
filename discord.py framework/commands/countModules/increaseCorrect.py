async def increaseCorrect(message, data):
    if message.author.name + "#" + message.author.discriminator not in data["correct"]:
        data["correct"][message.author.name + "#" +
                        message.author.discriminator] = 1
    else:
        data["correct"][message.author.name + "#" +
                        message.author.discriminator] += 1
    return data
