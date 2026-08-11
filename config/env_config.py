"""Environment config."""
import os
from typing import Optional

def get_env(key:str,default:Optional[str]=None)->Optional[str]:
 return os.getenv(key,default)

def get_int_env(key:str,default:int=0)->int:
 try:return int(os.getenv(key,str(default)))
 except:return default
