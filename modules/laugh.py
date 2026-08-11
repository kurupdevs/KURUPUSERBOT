# Laugh reaction module
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("laugh"))
async def laugh_command(client: Client, message: Message):
    await message.reply("😂")
