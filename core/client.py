from pyrogram import Client
from config.constants import APP
import logging
logger=logging.getLogger(__name__)
def make(aid,ahash,tok=None):return Client(APP,api_id=aid,api_hash=ahash,bot_token=tok)
