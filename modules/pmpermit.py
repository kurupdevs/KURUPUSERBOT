import logging
from pyrogram import filters
from pyrogram.types import Message
from config.constants import prefix
from utils.db import db

@Client.on_message(filters.private & filters.incoming & ~filters.me)
async def pmpermit_handler(client, message: Message):
    if not db.get("core.pmpermit", "enabled", False):
        return
    user = message.from_user
    approved = db.get("core.pmpermit", "approved", [])
    if user.id not in approved:
        await message.reply("**PM Permit enabled. Wait for approval.**")
        await client.send_message(config.log_channel, f"#PMPermit\nUser: {user.mention}\nID: `{user.id}`")