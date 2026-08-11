# Python execution module
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("python"))
async def python_command(client: Client, message: Message):
    code = " ".join(message.command[1:])
    if not code:
        await message.reply("Usage: /python <code>")
        return
    try:
        result = eval(code)
        await message.reply(f"Result: {result}")
    except Exception as e:
        await message.reply(f"Error: {e}")
