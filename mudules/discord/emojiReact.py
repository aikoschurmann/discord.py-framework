async def emojiReact(message, emoji):
    "replies with a emoji to given message"
    await message.add_reaction(emoji)
