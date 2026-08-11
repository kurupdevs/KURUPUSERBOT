import time
from pyrogram import Client

START_TIME=time.time()

def get_uptime():
 u=time.time()-START_TIME
 h,r=divmod(u,3600)
 m,s=divmod(r,60)
 return f"{int(h)}h {int(m)}m {int(s)}s"
