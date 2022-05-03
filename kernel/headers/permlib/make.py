from includetool import *

import os, shutil

def get_path():
    return os.path.dirname(os.path.realpath(__file__))

#os.chdir(os.environ["__GLOBAL_PATH"])
# --- End init.

def perms():
  path = os.environ["__HEADERS_PATH"]
  
  log("--> Performing unit tests")
  
  log("---> Including PermLib driver and header...")
  perms = include_module("./headers/permlib/type.py")
  control = include_module("./drivers/permlib/control.py")
  
  log("---> Testing...")
  
  log("----> Converting permission to code.")
  
  for i in perms.perms.keys():
    log(f"PermLib Headers: Expected: {i} -> {perms.perms[i]}")
    
    if control.perms[i] == perms.perms[i]:
      log(f"OK! PermLib Control: {i} -> {control.perms[i]}")
    else:
      log(f"WARN! PermLib Control: {i} -> {control.perms[i]}")

    
  log("----> Testing setting up permissions:")
  for i in perms.perms:
    log(f"Setting up permissions to {i}... {control.PermControl.set_perm(i)}")
    log(f"Expected: {i}")
    if perms.PermType.get_perm() == i:
      log(f"OK! Returned: {perms.PermType.get_perm()}")
    else:
      log(f"WARN! Returned: {perms.PermType.get_perm()}")
  
  log("--> Copying files...")
  
  os.mkdir(os.path.join(path, "permlib"))
  
  files = [ # Filelist
  "type.py",
  "__init__.py"
    ]
  for file in files:
    shutil.copyfile(os.path.join("./headers", "permlib", file), os.path.join(path, "permlib", file))
  
  cleantool() # Clean __pycache__
  
  log("--> End.")

perms()