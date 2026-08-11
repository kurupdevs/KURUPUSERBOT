import time
from pyrogram import Client
ST=time.time()
def up():
 u=time.time()-ST
 h,r=divmod(u,3600)
 m,s=divmod(r,60)
 return f"{int(h)}h{int(m)}m{int(s)}s"
