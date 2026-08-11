"""SendMod module — send installed modules to the chat."""

import os

from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(filters.command("sendmod"))
async def sendmod_command(client: Client, message: Message) -> None:
    """Send an installed module file as an attachment.

    Usage: /sendmod <module_name>

    Sends the .py file from the modules directory as a document.
    """
    name = " ".join(message.command[1:])
    path = f"modules/{name}.py"
    if os.path.exists(path):
        await client.send_document(message.chat.id, path)
    else:
        await message.reply("Module not found.")
