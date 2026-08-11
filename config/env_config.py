# Environment configuration loader
import os

def load_config():
    """Load environment variables."""
    config = {
        "API_ID": int(os.getenv("API_ID", "0")),
        "API_HASH": os.getenv("API_HASH", ""),
        "BOT_TOKEN": os.getenv("BOT_TOKEN", ""),
    }
    return config
