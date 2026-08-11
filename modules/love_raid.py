# Love raid module
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("love"))
async def love_command(client: Client, message: Message):
    await message.reply("Love raid started! ❤️")
