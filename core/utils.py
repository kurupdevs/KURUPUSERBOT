import asyncio,logging
from pyrogram import Client
from pyrogram.types import Message

logger=logging.getLogger(__name__)

async def safe_send(c:Client,chat_id,text:str):
 try:return await c.send_message(chat_id,text)
 except Exception as e:logger.error(f"Send failed: {e}");return None

async def progress_bar(cur,total,msg,action="Processing"):
 pct=cur*100/total;bar="█"*int(pct/5)+"░"*(20-int(pct/5))
 await msg.edit(f"**{action}:** [{bar}] {pct:.1f}%")
