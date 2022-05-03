from maketools.init import * # Import init, to activate basic functionality.
from includetool import * # Import includetool with basic functions. This file provides: 
# include_module - include py file
# log - log text
# error - print error
# cleantool - clean __pycache__ at path '.'

import argparse, os, shutil 
# Argparse for parsing command-line, os for functions with file and shutil for clean.

def get_path(): # this function return path, where makefile located at. Can be needed in some cases.
    return os.path.dirname(os.path.realpath(__file__)) 

os.environ["__GLOBAL_PATH"] = os.getcwd() # Create environment variable with root dir
os.environ["__BUILD_PATH"] = "./build/" # Create environment variable with build path. You can change it, add something more, add your variables, and etc.

# --- End init.
# If you wanna clear all __pycache__ in all dirs, add this code. If not, delete it.
cleantool()
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
# Add here function to call src/make.py
def helloworld(): # No arguments
    log("Including src/make.py") # Write our about include
    include_module("src/make.py") # This will call src/make.py from here.
    
# --- Functions end.
functions = {"show_all": ["Show all avaliable tasks", show_all],
"helloworld": ["Hello World!", helloworld]} # write function without calling it.
# So, here you can add your functions. 
# First is function name, as keyword
# Then, list of two, including description as first argument, and callable function itself as second argument.
# Example: "example_function": ["Just example!", example_func]

parse()
