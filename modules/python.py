import sys
import io
import logging
from pyrogram import filters
from pyrogram.types import Message
from config.constants import prefix

@Client.on_message(filters.command("python", prefixes=prefix) & filters.me)
async def python_command(client, message: Message):
    code = message.text.split(None, 1)[1] if len(message.text.split()) > 1 else ""
    if not code:
        await message.edit("**Provide Python code to execute.**")
        return
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    try:
        exec(code)
        output = sys.stdout.getvalue()
    except Exception as e:
        output = f"Error: {str(e)}"
    finally:
        sys.stdout = old_stdout
    if len(output) > 4000:
        output = output[:3997] + "..."
    await message.edit(f"```\n{output}\n```")