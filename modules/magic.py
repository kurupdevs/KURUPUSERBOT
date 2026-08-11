# Magic module
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("magic"))
async def magic_command(client: Client, message: Message):
    await message.reply("Magic module active!")
