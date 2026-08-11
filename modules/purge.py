# Purge module
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("purge"))
async def purge_command(client: Client, message: Message):
    if not message.reply_to_message:
        await message.reply("Reply to a message to purge.")
        return
    msg_ids = range(message.reply_to_message.id, message.id + 1)
    await client.delete_messages(message.chat.id, list(msg_ids))
