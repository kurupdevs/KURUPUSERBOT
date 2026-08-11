import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message


async def setup(client: Client):
    client.on_message(filters.command("kill", prefixes=".") & filters.me)(kill_session)


async def kill_session(client: Client, message: Message):
    await message.edit("**Terminating all sessions...**")
    try:
        sessions = await client.get_active_sessions()
        count = 0
        for session in sessions:
            if session.hash != client.session_hash:
                await client.terminate_session(session.hash)
                count += 1
        await message.edit(f"**Killed {count} sessions.**")
    except Exception as e:
        await message.edit(f"**Error:** {e}")
