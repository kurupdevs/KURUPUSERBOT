import subprocess
import logging
from pyrogram import filters
from pyrogram.types import Message
from config.constants import prefix

@Client.on_message(filters.command("shell", prefixes=prefix) & filters.me)
async def shell_command(client, message: Message):
    cmd = message.text.split(None, 1)[1] if len(message.text.split()) > 1 else ""
    if not cmd:
        await message.edit("**Usage:** `.shell <command>`")
        return
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=30)
        output = result.stdout or result.stderr
        if len(output) > 4000:
            output = output[:3997] + "..."
        await message.edit(f"**Shell Output:**\n```\n{output}\n```")
    except subprocess.TimeoutExpired:
        await message.edit("**Command timed out.**")