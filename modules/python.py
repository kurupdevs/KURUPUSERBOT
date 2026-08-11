import subprocess
import sys
from pyrogram import Client, filters
from pyrogram.types import Message


async def setup(client: Client):
    client.on_message(filters.command("python", prefixes=".") & filters.me)(python_handler)


async def python_handler(client: Client, message: Message):
    code = message.text.split(None, 1)
    if len(code) < 2:
        await message.edit("**Usage:** `.python <code>`")
        return
    try:
        result = subprocess.run(
            [sys.executable, "-c", code[1]],
            capture_output=True, text=True, timeout=10
        )
        output = result.stdout or result.stderr
        await message.edit(f"```\n{output[:2000]}\n```")
    except subprocess.TimeoutExpired:
        await message.edit("**Timeout!**")
    except Exception as e:
        await message.edit(f"**Error:** {e}")
