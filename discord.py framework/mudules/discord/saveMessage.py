def saveMessage(message, path):
    "saves message to given path"
    server = message.guild.name
    name = message.author.name + "#" + message.author.discriminator
    suffix = server + "  |  " + name + "  |  "
    line = suffix + message.content + "\n"
    with open(path, 'a') as f:
        f.write(line)
