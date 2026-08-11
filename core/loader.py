"""
Dynamic module loader for KurupUserbot.

Scans the modules directory and imports every .py file,
calling each module's setup() function if it exists.
"""

import importlib
import logging
import os

logger = logging.getLogger(__name__)


async def load(c, md: str = "modules") -> None:
    """Dynamically import and register all modules.

    Args:
        c: The Pyrogram Client instance.
        md: Path to modules directory (default: modules).
    """
    if not os.path.exists(md):
        logger.warning("Module directory %s not found", md)
        return
    for f in sorted(os.listdir(md)):
        if f.endswith(".py") and not f.startswith("__"):
            try:
                mod = importlib.import_module(f"{md}.{f[:-3]}")
                if hasattr(mod, "setup"):
                    await mod.setup(c)
            except Exception as e:
                logger.error("Failed to load %s: %s", f, e)
