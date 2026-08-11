import asyncio
from pyrogram import Client,filters
from pyrogram.types import Message

async def setup(c):c.on_message(filters.command("example",prefixes=".")&filters.me)(h)
async def h(c:Client,m:Message):await m.edit("This is an example module.")
