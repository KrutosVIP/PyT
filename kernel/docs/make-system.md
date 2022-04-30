# Make system
For PyT version 2.0, we needed something like make - for building, packaging kernels, packages and OTA

So, here it is, make system based on Python.

## How to add make in project by yourself?
Create dir `maketools` in root of your project </br>
Then, copy two files from somewhere, from example, from here, to your `maketools`: </br>
> `maketools/includetool.py` <br/>
> `maketools/init.py`

After that, in root, create file with name as you want, for example, `make.py`, this will be make executable.<br/>
Add this code at the start.
```py
from maketools.init import * # Import init, to activate basic functionality.
from includetool import * # Import includetool with basic functions. This file provides: 
# include_module - include py file
# log - log text
# error - print error

import argparse, os, shutil 
# Argparse for parsing command-line, os for functions with file and shutil for clean.

def get_path(): # this function return path, where makefile located at. Can be needed in some cases.
    return os.path.dirname(os.path.realpath(__file__)) 

os.environ["__GLOBAL_PATH"] = os.getcwd() # Create environment variable with root dir
os.environ["__BUILD_PATH"] = "./build/" # Create environment variable with build path. You can change it, add something more, add your variables, and etc.

# --- End init.
# If you wanna clear all __pycache__ in all dirs, add this code. If not, delete it.
for root, dirs, files in os.walk("."):
    for dir in dirs:
        if dir == "__pycache__":
            shutil.rmtree(os.path.join(root, dir))
# --- End clear.
def parse(): # Main parse function for commandline
    tasks = ", ".join([f"{x}" for x in functions]) # Create list from functions - "build, clean, ..."
    
    parser = argparse.ArgumentParser( # Main class for parser
    prog="make",
    description = f"Avaliable tasks: {tasks}",
    epilog="---- Time to make something!")
 
    parser.add_argument("type", type=str, help = "See 'show_all'") # type of task, build and etc.
    args = parser.parse_args() # Parse args

    if args.type in functions: # Check if type in functions
        functions[args.type][1]() # Execute function
    else:
        log(f"Unknown task {args.type}") # If type not found

def show_all(): # Show all tasks, basic function.
    tasks = ",\n".join([f"{x} - {functions[x][0]}" for x in functions]) # Create list from functions name and descriptions. Then, convert to string.
    log(f"Avaliable tasks:\n{tasks}") # print out it
# --- Pre-init end.

# --- Functions end.
functions = {"show_all": ["Show all avaliable tasks", show_all]} # So, here you can add your functions. 
# First is function name, as keyword
# Then, list of two, including description as first argument, and callable function itself as second argument.
# Example: "example_function": ["Just example!", example_func]

parse() # do not forget to call parse function!
```
## Writing makefiles
Now, lets make something. For example, base with "Hello world!" <br/>
Create dir with name "src", or as you want<br/>
Then, just make file `src/helloworld.py` with one string - `print("Hello World!")` <br/>
Now, lets write makefile. <br/>

> In Kernel, you can see, what all make scripts going into maketools, like maketools/build.py, but in your project - you can store them everythere. For this tutorial, lets make them in src. 

> **Also, if you wanna make kernel header or smth more, go into `kernel-makefiles.md`*

Create `src/make.py`, and open it.
We need some code at start:
```py
from includetool import * # Import basic functions

import os # Import os for get_path

def get_path(): # Get Makefile path
    return os.path.dirname(os.path.realpath(__file__))
# --- End init.
```

Lets call our `src/helloworld.py` from here, using include_module functionality
```py
...
# --- End init.
include_module("src/helloworld.py")
```
Make file is now done. You can add here some code and more, be free </br>
But how to add this as a task for our make? </br>
Lets make new function. Open `make.py` in root of your project
```py
...
# --- Pre-init end.
# Add here function to call src/make.py
def helloworld(): # No arguments
    log("Including src/make.py") # Write our about include
    include_module("src/make.py") # This will call src/make.py from here.

# --- Functions end.
```
Now, create new function in `functions` dict at the end of file
```py
...
functions = {"show_all": ["Show all avaliable tasks", show_all],
"helloworld": ["Hello World!", helloworld]} # write function without calling it.
# So, here you can add your functions. 
# First is function name, as keyword
# Then, list of two, including description as first argument, and callable function itself as second argument.
# Example: "example_function": ["Just example!", example_func]
...
```

> Full examples can be seen in makeexample, in root of repo.

## Testing
Open console, go to project root dir using cd
<br/> And let`s check project.
```bash
$ make.py show_all
make: Avaliable tasks:
show_all - Show all avaliable tasks,
helloworld - Hello World!
```
Thats working. Lets start helloworld task.

```
$ make.py helloworld
make: Including src/make.py
Hello World!
```

> Thats the end. Good luck in working.