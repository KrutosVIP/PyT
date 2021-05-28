import sys, json, os, importlib
from colorama import Back, Fore, Style
from colorama import init as cinit
import argparse
sys.path.insert(0, "../types")
cinit()
from binary import Binary
class UName(Binary):
    def __init__(self):
        self.info = {
            "name" : "Uname",
            "version" : "v1",
            "codename": "uname",
            "dependencies" : [], # Not Supported.
            "description": "Get uname",
            "run": self.run
        }

    def run(self, info, pyt):
        sets = info.info[14].uname
        print(" ".join(list(sets.values())))
