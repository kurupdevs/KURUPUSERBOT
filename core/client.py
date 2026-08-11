import os,logging
from pyrogram import Client
from config.constants import APP_NAME

logger=logging.getLogger(__name__)

def create_client(api_id,api_hash,bot_token=None):
 logger.info(f"Creating {APP_NAME} client...")
 return Client(APP_NAME,api_id=api_id,api_hash=api_hash,bot_token=bot_token)
