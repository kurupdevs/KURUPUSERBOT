# Prefix management module
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("prefix"))
async def prefix_command(client: Client, message: Message):
    await message.reply("Current prefix: .")
