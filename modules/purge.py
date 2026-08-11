import asyncio
import logging
from pyrogram import filters
from pyrogram.types import Message
from config.constants import prefix

@Client.on_message(filters.command("purge", prefixes=prefix) & filters.me)
async def purge_command(client, message: Message):
    if not message.reply_to_message:
        await message.edit("**Reply to a message to start purging.**")
        return
    chat_id = message.chat.id
    start_msg = message.reply_to_message.id
    end_msg = message.id
    await message.delete()
    deleted = 0
    for msg_id in range(start_msg, end_msg + 1):
        try:
            await client.delete_messages(chat_id, msg_id)
            deleted += 1
        except Exception:
            pass
    status = await client.send_message(chat_id, f"**Purged {deleted} messages.**")
    await asyncio.sleep(3)
    await status.delete()