from includetool import * # Import basic functions

import os # Import os for get_path

def get_path(): # Get Makefile path
    return os.path.dirname(os.path.realpath(__file__))
# --- End init.
include_module("src/helloworld.py")
