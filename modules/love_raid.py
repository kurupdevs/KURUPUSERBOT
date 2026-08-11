# Love Raid module
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("love_raid"))
async def love_raid_command(client: Client, message: Message):
    await message.reply("Love raid started!")
