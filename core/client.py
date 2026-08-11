from pyrogram import Client
from config.constants import APP_NAME
import logging,os

logger=logging.getLogger(__name__)

def make(api_id,api_hash,token=None):
 return Client(APP_NAME,api_id=api_id,api_hash=api_hash,bot_token=token)
