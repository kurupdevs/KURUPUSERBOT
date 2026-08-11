# AFK module for userbot
from pyrogram import Client, filters
from pyrogram.types import Message
import time

AFK_DATA = {}

@Client.on_message(filters.command("afk"))
async def afk_command(client: Client, message: Message):
    reason = " ".join(message.command[1:]) or "No reason"
    AFK_DATA[message.from_user.id] = {"reason": reason, "time": time.time()}
    await message.reply(f"You are now AFK. Reason: {reason}")
