import os
from pyrogram import Client,filters

async def setup(c):
 c.on_message(filters.command("sendmod",prefixes=".")&filters.me)(h)

async def h(c,m):
 a=m.text.split(None,2)
 if len(a)<2:
  await m.edit("Usage: .sendmod <module.py> [chat_id]");return
 fn=a[1]
 if not os.path.exists(f"modules/{fn}"):
  await m.edit("Module not found.");return
 with open(f"modules/{fn}")as f:code=f.read()
 await m.edit(f"```python\n{code[:2000]}\n```")
