"""
Logging configuration for KurupUserbot.

Sets up a centralised logger with both console and file
output, used by all modules in the userbot.
"""

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("kuruplogs.txt"),
    ],
)
