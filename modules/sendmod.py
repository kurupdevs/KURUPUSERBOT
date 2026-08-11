import os
import logging
from pyrogram import filters
from pyrogram.types import Message
from config.constants import prefix

@Client.on_message(filters.command("sendmod", prefixes=prefix) & filters.me)
async def sendmod_command(client, message: Message):
    if len(message.text.split()) < 2:
        await message.edit("**Usage:** `.sendmod <module_name>`")
        return
    module_name = message.text.split(None, 1)[1]
    module_path = f"modules/{module_name}.py"
    if os.path.exists(module_path):
        await client.send_document(message.chat.id, module_path, caption=f"**Module:** `{module_name}.py`")
        await message.delete()
    else:
        await message.edit(f"**Module `{module_name}` not found!**")