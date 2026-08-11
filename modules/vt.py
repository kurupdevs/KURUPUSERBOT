# VT module
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("vt"))
async def vt_command(client: Client, message: Message):
    await message.reply("VirusTotal scan started!")
