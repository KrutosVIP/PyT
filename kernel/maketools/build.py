from includetool import *
import os

def get_path():
    return os.path.dirname(os.path.realpath(__file__))

#os.chdir(os.environ["__GLOBAL_PATH"])
# --- End init.

def build():
    path = os.environ["__BUILD_PATH"]
    
    if os.path.exists(path):
        log(f"Build '{path}' directory present. Do you used 'clean' before build?")
        error("Use 'clean' before build. End.")

        return
    else:
        os.mkdir(path)
        
    log("Processing build configs...")

    log("-> Building kernel with version...", end="")
    
    ver = include_module("./headers/kversion.py")
    
    print(ver.KVersion.full)
    del ver

    log("-> Building headers...")

    os.environ["__HEADERS_PATH"] = os.path.join(path, "headers")
    include_module("./maketools/headers.py")
    

build()
