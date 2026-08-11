"""Say module — make the bot speak a message."""

from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(filters.command("say"))
async def say_command(client: Client, message: Message) -> None:
    """Make the bot repeat a message.

    Usage: /say <text>

    Deletes your command and sends the specified text
    as the bot.

    Args:
        client: The Pyrogram client.
        message: The trigger message.
    """
    text = " ".join(message.command[1:])
    if not text:
        await message.reply("Usage: /say <text>")
        return
    await message.delete()
    await client.send_message(message.chat.id, text)
