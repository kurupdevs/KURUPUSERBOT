# Gali Raid module
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("gali_raid"))
async def gali_raid_command(client: Client, message: Message):
    await message.reply("Gali raid started!")
