# PM Permit module
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("pmpermit"))
async def pmpermit_command(client: Client, message: Message):
    await message.reply("PM Permit enabled.")
