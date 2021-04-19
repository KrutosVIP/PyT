import sys, json, os, importlib
from colorama import Back, Fore, Style
from colorama import init as cinit
import re
import argparse
sys.path.insert(0, "../types")
cinit()


from binary import Binary
class rmdir(Binary):
    def __init__(self):
        self.info = {
            "name" : "echo",
            "version" : "v1",
            "codename": "echo",
            "dependencies" : [], # Not Supported.
            "description": "Print some text :)",
            "run": self.run,
            "on_load": self.on_load
        }

    def on_load(self, info):
        pass

    def json_load(self, file):
        with open(file, "r",  encoding = "utf-8") as f:
            return json.load(f)
        
    def run(self, info, pyt):
        args = info.info[15].split(" ")[1:]
        print(info.color(" ".join(args)) + Style.RESET_ALL)
