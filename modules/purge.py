# Message purge module
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("purge"))
async def purge_command(client: Client, message: Message):
    await message.reply("Purge initiated!")
