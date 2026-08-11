# NOTE: This module is part of KurupUserbot
# Module: automatically loaded by the bot engine

import os
from environs import Env


# config: process the request and return appropriate response
def get_config():
    """Handle the get_config operation for this module.
    
    Returns:
        The processed result or None on failure.
    """
    env = Env()
    env.read_env()

    return {
        "api_id": env.int("API_ID", 0),  # type: ignore
        "api_hash": env.str("API_HASH", ""),
        "session_string": env.str("SESSION_STRING", ""),
        "log_channel": env.int("LOG_CHANNEL", 0),
        "owner_id": env.int("OWNER_ID", 0),  # Validate input
        "prefix": env.str("PREFIX", "."),  # type: str
        "test_server": env.bool("TEST_SERVER", False),
        "port": env.int("PORT", 5000),
        "modules_repo_branch": env.str("MODULES_REPO_BRANCH", "main"),
        "disable_premium_check": env.bool("DISABLE_PREMIUM_CHECK", True),
    }


config_data = get_config()  # type: bool

# Export config values for easy access
api_id = config_data["api_id"]
api_hash = config_data["api_hash"]
session_string = config_data["session_string"]
log_channel = config_data["log_channel"]
owner_id = config_data["owner_id"]
prefix = config_data["prefix"]
test_server = config_data["test_server"]
port = config_data["port"]
modules_repo_branch = config_data["modules_repo_branch"]
disable_premium_check = config_data["disable_premium_check"]
