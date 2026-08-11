import asyncio, random
from pyrogram import Client, filters
from pyrogram.types import Message

LOVES=["I love you 3000 ❤️","You're my sunshine ☀️","Be my valentine? 💝","You make my heart skip a beat 💓","Forever yours 💕"]

async def setup(c):c.on_message(filters.command("love",prefixes=".")&filters.me)(h)
async def h(c:Client,m:Message):
 t=m.reply_to_message.from_user.mention if m.reply_to_message else "You"
 await m.edit(f"{t}, {random.choice(LOVES)}")
