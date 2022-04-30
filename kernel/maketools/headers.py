from includetool import *

import os, shutil

def get_path():
    return os.path.dirname(os.path.realpath(__file__))

#os.chdir(os.environ["__GLOBAL_PATH"])
# --- End init.

def headers():
    path = os.environ["__HEADERS_PATH"]
    
    if os.path.exists(path):
        log(f"Headers '{path}' directory present. Do you used 'clean' before build?")
        error("Use 'clean' before build. End.")

        return
    else:
        os.mkdir(path)
        
    log("Processing build configs...")

    for x in os.listdir("./headers"):
        if not x == "__pycache__":      
            if os.path.isfile(os.path.join("./headers", x)):
                log(f"Copying {os.path.join('./headers', x)} to {os.path.join(path, x)}".replace("\\", "/"))
                shutil.copyfile(os.path.join("./headers", x), os.path.join(path, x))
            else:
                if os.path.exists(os.path.join("./headers", x, "make.py")):
                    log(f"Including {os.path.join('./headers', x, 'make.py')}".replace("\\", "/"))
                    include_module(os.path.join("./headers", x, "make.py"))
                else:
                    log(f"Copying {os.path.join('./headers', x)} to {os.path.join(path, x)}".replace("\\", "/"))
                    shutil.copyfile(os.path.join("./headers", x), os.path.join(path, x))
                
    

headers()
