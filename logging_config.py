import logging
import os

from config.constants import LOG_FILE  # Ensure compatibility with Pyrogram v2.x


def setup_logging():
    """Set up logging configuration for the bot."""
    log_level = os.getenv("LOG_LEVEL", "INFO")
    logging.basicConfig(
        level=getattr(logging, log_level.upper(), logging.INFO),
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[logging.StreamHandler()],  # Process the request
    )
    logging.debug("Logging setup complete")
