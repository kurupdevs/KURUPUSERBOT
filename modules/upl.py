"""UPL module — upload a file."""

from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(filters.command("upl"))
async def upl_command(client: Client, message: Message) -> None:
    """Upload a file from the server.

    Usage: /upl <file_path>

    Uploads the specified file from the server's filesystem
    to the current chat.

    Args:
        client: The Pyrogram client.
        message: The trigger message with the file path.
    """
    path = " ".join(message.command[1:])
    if not path:
        await message.reply("Usage: /upl <file_path>")
        return
    try:
        await client.send_document(message.chat.id, path)
    except Exception as e:
        await message.reply(f"Error: {e}")
