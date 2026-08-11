import subprocess
from pyrogram import Client, filters
from pyrogram.types import Message

ALLOWED_USERS = set()


async def setup(client: Client):
    client.on_message(filters.command("shell", prefixes=".") & filters.me)(shell_handler)


async def shell_handler(client: Client, message: Message):
    cmd = message.text.split(None, 1)
    if len(cmd) < 2:
        await message.edit("**Usage:** `.shell <command>`")
        return
    try:
        result = subprocess.run(
            cmd[1], shell=True, capture_output=True, text=True, timeout=30
        )
        output = (result.stdout or result.stderr)[:2000]
        await message.edit(f"```\n{output}\n```")
    except subprocess.TimeoutExpired:
        await message.edit("**Timeout!**")
    except Exception as e:
        await message.edit(f"**Error:** {e}")
