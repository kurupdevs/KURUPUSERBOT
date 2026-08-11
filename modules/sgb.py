import random
from pyrogram import Client, filters
from pyrogram.types import Message

SGB=["🤣","😂","😭","💀","🤡","👀","🔥","💯"]

async def setup(c):c.on_message(filters.command("sgb",prefixes=".")&filters.me)(h)
async def h(c:Client,m:Message):
 count=min(int(m.text.split()[-1])if m.text.split()[-1].isdigit()else 1,10)
 await m.edit(random.choice(SGB)*count)
