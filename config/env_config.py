"""
Environment-based configuration loader.

Reads sensitive credentials from environment variables
so they are never committed to source control.
"""

import os

API_ID: int = int(os.getenv("API_ID", "0"))
"""Telegram API ID from https://my.telegram.org/apps."""

API_HASH: str = os.getenv("API_HASH", "")
"""Telegram API hash from https://my.telegram.org/apps."""

BOT_TOKEN: str = os.getenv("BOT_TOKEN", "")
"""Bot token obtained from @BotFather on Telegram."""
