"""
Utility helpers for KurupUserbot.

Provides shared helper functions used across modules.
"""

import time

ST = time.time()
"""Module-level startup timestamp for uptime calculation."""


def up() -> str:
    """Return human-readable uptime since module was loaded.

    Returns:
        A string like '2h34m12s'.
    """
    elapsed = time.time() - ST
    h, r = divmod(elapsed, 3600)
    m, s = divmod(r, 60)
    return f"{int(h)}h{int(m)}m{int(s)}s"
