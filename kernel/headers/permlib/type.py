import os 

perms = {
  "kernel": "__PERM__KERNEL__",
  "root": "__PERM__ROOT__",
  "user": "__PERM__USER__"
}
codes = {
  "__PERM__KERNEL__": "kernel",
  "__PERM__ROOT__": "root",
  "__PERM__USER__": "user"
}

class PermType:
  def convert(code: str):
    if code in perms:
      return perms[code]
    elif code in codes:
      return codes[code]
    else:
      return None
  
  def is_kernel():
    if os.environ["__PYT_KERN_PERM"] == perms["kernel"]:
      return True
    return False
    
  def is_root():
    if os.environ["__PYT_KERN_PERM"] == perms["root"]:
      return True
    return False
  
  def is_user():
    if os.environ["__PYT_KERN_PERM"] == perms["user"]:
      return True
    return False
  
  def get_perm():
    return PermType.convert(os.environ["__PYT_KERN_PERM"])