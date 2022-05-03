#!/usr/bin/python3
from maketools.init import *
from includetool import *

import argparse, os, shutil

def get_path():
    return os.path.dirname(os.path.realpath(__file__))

os.environ["__GLOBAL_PATH"] = os.getcwd()
os.environ["__BUILD_PATH"] = "./build/"
os.environ["__HEADERS_PATH"] = "./include/"
os.environ["__KERNEL_DEFCONFIG"] = "pyzen_defaults.json"
# --- End init.
cleantool()
# --- End clear.


def parse():
    tasks = ", ".join([f"{x}" for x in functions])
    
    parser = argparse.ArgumentParser(
    prog="make",
    description = f"Avaliable tasks: {tasks}",
    epilog="---- Time to make something!")
 
    parser.add_argument("type", type=str, help = "See 'show_all'")
    args = parser.parse_args()

    if args.type in functions:
        functions[args.type][1]()
    else:
        log(f"Unknown task {args.type}")

def show_all():
    tasks = ",\n".join([f"{x} - {functions[x][0]}" for x in functions])
    log(f"Avaliable tasks:\n{tasks}")
# --- Pre-init end.

def build():
    file = "./maketools/build.py"

    log(f"Including {file}")
    include_module(file)
    log(f"End of main process.")

def headers():
    file = "./maketools/headers.py"

    log(f"Including {file}")
    include_module(file)
    log(f"End of main process.")   

def clean():
    existing_dirs = [os.environ.get(x) for x in ["__BUILD_PATH", "__HEADERS_PATH"] if os.environ.get(x) and os.path.exists(os.environ.get(x))]
    
    if len(existing_dirs) == 0:
        log("WARN: Nothing to delete.")
        
        log("Nothing done.")
        return
    
    for _dir in existing_dirs:
        shutil.rmtree(_dir, ignore_errors=True)
        log(f"Dir {_dir} deleted!")
        
    log(f"Working directories deleted.")
    
    
functions = {"mkkernel": ["Prepare and pack kernel", build],
             "show_all": ["Show all avaliable tasks", show_all],
             "clean": ["Clean working dirs", clean],
             "mkheaders": ["Make kernel headers", headers]}

if __name__ == "__main__":
    parse()
