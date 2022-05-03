import os 
# PermLib Control Driver
# Needed to make different types of permissions

perms = { # permission to its code
  "kernel": "__PERM__KERNEL__",
  "root": "__PERM__ROOT__",
  "user": "__PERM__USER__"
}
codes = { # code to its permission
  "__PERM__KERNEL__": "kernel",
  "__PERM__ROOT__": "root",
  "__PERM__USER__": "user"
}

class PermControl: # Control of PermLib
  def convert(code: str): # Convert from code to perm, from perm to code
    if code in perms:
      return perms[code]
    elif code in codes:
      return codes[code]
    else:
      return None
  
  def set_kernel(): # Set kernel level
    os.environ["__PYT_KERN_PERM"] = perms["kernel"]
    
  def set_root(): # Set root level
    os.environ["__PYT_KERN_PERM"] = perms["root"]
  
  def set_user(): # Set user level
    os.environ["__PYT_KERN_PERM"] = perms["user"]
  
  def set_perm(perm): # Set perm with name from perms
    if perm in perms:
      os.environ["__PYT_KERN_PERM"] = perms[perm]
      return True
    else:
      return False