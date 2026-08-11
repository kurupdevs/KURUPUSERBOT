import os,importlib,logging
logger=logging.getLogger(__name__)

async def load(c,md="modules"):
 if not os.path.exists(md):return
 for f in sorted(os.listdir(md)):
  if f.endswith(".py")and not f.startswith("__"):
   m=f"{md}.{f[:-3]}"
   try:
    mod=importlib.import_module(m)
    if hasattr(mod,"setup"):await mod.setup(c)
   except Exception as e:logger.error(e)
