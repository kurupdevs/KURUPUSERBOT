"""Purge module — bulk delete messages."""

from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(filters.command("purge"))
async def purge_command(client: Client, message: Message) -> None:
    """Purge (delete) messages in bulk.

    Usage: Reply to a message with /purge to delete all messages
    from that message up to the command message.

    Args:
        client: The Pyrogram client.
        message: The trigger message (must be a reply).
    """
    if not message.reply_to_message:
        await message.reply("Reply to a message to purge from.")
        return
    msg_ids = range(message.reply_to_message.id, message.id + 1)
    await client.delete_messages(message.chat.id, list(msg_ids))
