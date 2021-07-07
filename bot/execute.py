# framework
from bot.Flux import Flux


# commands
#from commands.response import response
#from commands.setactivity import setactivity
#from commands.shutdown import shutdown


# runs every message
async def execute(message, client):

    # initiates framework
    Client = Flux(message, client)

    # runs when message starts with prefix and author isnn't a bot
    if Client.HasPrefix() and not Client.IsBot():
        pass
        # await Client.NewCommand("test", response, args=["1"])
        # await Client.NewCommand("setactivity", setactivity, client)
        # await Client.NewCommand("shutdown", shutdown, client)

    # runs when no prefix is needed and author isn't a bot
    elif not Client.IsBot():

        # runs when message was send in specific channel
        if Client.Channel("counting"):

            await Client.Count()
