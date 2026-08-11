# KurupUserbot - Main Entry
# A powerful Telegram userbot

import os
import asyncio
from pyrogram import Client

API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")
STRING_SESSION = os.environ.get("STRING_SESSION")

app = Client(
    "kurupuserbot",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=STRING_SESSION,
)

async def main():
    await app.start()
    print("KurupUserbot started!")
    await asyncio.Event().wait()

if __name__ == "__main__":
    app.run(main())
