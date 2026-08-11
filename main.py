"""
KurupUserbot — Main entry point.

A powerful, fast Telegram userbot with 20+ built-in modules
for automation, moderation, fun, and utilities.

Copyright (c) 2024-present KurupDevs
"""

import asyncio
import logging
import os
from pyrogram import Client

API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")
STRING_SESSION = os.environ.get("STRING_SESSION")

logger = logging.getLogger("kurup_userbot")

app = Client(
    "kurupuserbot",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=STRING_SESSION,
)


async def main() -> None:
    """Start the userbot and wait indefinitely."""
    await app.start()
    logger.info("KurupUserbot started!")
    await asyncio.Event().wait()


if __name__ == "__main__":
    app.run(main())
