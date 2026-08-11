"""
Pyrogram client factory for KurupUserbot.

Provides a helper to create configured Pyrogram Client
instances with the correct application name.
"""

import logging
from typing import Optional

from pyrogram import Client

from config.constants import APP

logger = logging.getLogger(__name__)


def make(
    api_id: int,
    api_hash: str,
    bot_token: Optional[str] = None,
) -> Client:
    """Create a Pyrogram client instance.

    Args:
        api_id: Telegram API ID from my.telegram.org.
        api_hash: Telegram API hash.
        bot_token: Optional bot token for bot mode.

    Returns:
        A configured Client ready to start.
    """
    return Client(
        APP,
        api_id=api_id,
        api_hash=api_hash,
        bot_token=bot_token,
    )
