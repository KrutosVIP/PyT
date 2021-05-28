import sys, json, os, importlib
from colorama import Back, Fore, Style
from colorama import init as cinit
import argparse
sys.path.insert(0, "../types")
cinit()
from binary import Binary
class eval(Binary):
    def __init__(self):
        self.info = {
            "name" : "Eval",
            "version" : "v1",
            "codename": "eval",
            "dependencies" : [], # Not Supported.
            "description": "Eval something. (Enable dangerous functions to use it!)",
            "run": self.run
        }

    def run(self, info, pyt):
        if not info.info[14].ksets["danger"]: return print("No-safety option disabled.")
        if len(info.info[15].split(" ")[1:]) < 1: return print("No arguments.")
        exec(" ".join(info.info[15].split(" ")[1:]))
