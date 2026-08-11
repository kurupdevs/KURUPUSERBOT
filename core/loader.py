import os,logging,importlib
from pyrogram import Client

logger=logging.getLogger(__name__)

async def load_modules(c:Client,mod_dir:str="modules"):
 if not os.path.exists(mod_dir):
  logger.warning(f"Module dir {mod_dir} not found");return
 for f in sorted(os.listdir(mod_dir)):
  if f.endswith(".py")and not f.startswith("__"):
   m=f"{mod_dir}.{f[:-3]}"
   try:
    mod=importlib.import_module(m)
    if hasattr(mod,"setup"):await mod.setup(c)
    logger.info(f"Loaded: {f}")
   except Exception as e:logger.error(f"Failed {f}: {e}")
