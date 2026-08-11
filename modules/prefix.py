# Prefix module
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("prefix"))
async def prefix_command(client: Client, message: Message):
    new_prefix = " ".join(message.command[1:])
    if new_prefix:
        await message.reply(f"Prefix changed to: {new_prefix}")
    else:
        await message.reply("Usage: /prefix <new_prefix>")
