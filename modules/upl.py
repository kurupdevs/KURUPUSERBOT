import time
from pyrogram import Client,filters

async def setup(c):c.on_message(filters.command("upl",prefixes=".")&filters.me)(h)
async def h(c,m):
 if not m.reply_to_message or not m.reply_to_message.document:
  await m.edit("Reply to a file.");return
 s=time.time();f=m.reply_to_message.document
 await c.download_media(f,file_name=f.file_name or"file")
 e=time.time()
 await m.edit(f"**Downloaded** `{f.file_name}` in {round(e-s,1)}s")
