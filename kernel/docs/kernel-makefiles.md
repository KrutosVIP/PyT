# Kernel Makefiles system
## Headers
If you wanna make smth like compilable header, you need to make dir in `headers/`<br/>
Then, make a file named make.py, and here you go, default makefile, will be executed at build time. How to write makefiles you can see in `make-system.md`. <br/>
If you just want your headers to be copied into a include dir, create dir and then make your code, it will be automatically copied to include<br/>
If you want to make header in one file, just make it in root of `headers/`. <br/>
Headers makefile code with comments:
```py
from includetool import *

import os, shutil

def get_path():
    return os.path.dirname(os.path.realpath(__file__))

#os.chdir(os.environ["__GLOBAL_PATH"])
# --- End init. 

def headers():
    path = os.environ["__HEADERS_PATH"] # Get path fron environment variable. 
    
    if os.path.exists(path): # Check if dir present.
        log(f"Headers '{path}' directory present. Do you used 'clean' before build?")
        error("Use 'clean' before build. End.")

        return
    else:
        os.mkdir(path) 
        
    log("Processing build configs...")

    for x in os.listdir("./headers"): # Get all files in headers dir
        if not x == "__pycache__": # Ignore pycache dir
            if os.path.isfile(os.path.join("./headers", x)): # If is file...
                log(f"Copying {os.path.join('./headers', x)} to {os.path.join(path, x)}".replace("\\", "/"))
                shutil.copyfile(os.path.join("./headers", x), os.path.join(path, x)) # ...Just copy it to headers path
            else: # If dir...
                if os.path.exists(os.path.join("./headers", x, "make.py")): # If make.py exists in dir...
                    log(f"Including  {os.path.join('./headers', x, 'make.py')}".replace("\\", "/"))
                    include_module(os.path.join("./headers", x, "make.py")) # ...include it
                else: # If not...
                    log(f"Copying {os.path.join('./headers', x)} to {os.path.join(path, x)}".replace("\\", "/"))
                    shutil.copyfile(os.path.join("./headers", x), os.path.join(path, x)) # Just copy headers in headers path
                
    

headers() # Execute function
```