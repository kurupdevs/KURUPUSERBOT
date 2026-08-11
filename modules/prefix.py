import json
from pyrogram import Client,filters
from pyrogram.types import Message

PREFIXES={}
PF="prefixes.json"

def _load():
 try:
  with open(PF)as f:return json.load(f)
 except:return{}

def _save(d):
 with open(PF,"w")as f:json.dump(d,f,indent=2)

async def setup(c):c.on_message(filters.command("setprefix",prefixes=".")&filters.me)(h)

async def h(c:Client,m:Message):
 a=m.text.split(None,2)
 if len(a)<3:
  await m.edit("Usage: .setprefix <chat_id> <prefix>");return
 d=_load();d[a[1]]=a[2];_save(d)
 await m.edit(f"**Prefix set:** `{a[2]}`")
