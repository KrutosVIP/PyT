import sys, json, os, importlib
from colorama import Back, Fore, Style
from colorama import init as cinit
import argparse
sys.path.insert(0, "../types")
cinit()
from binary import Binary
class whoami(Binary):
    def __init__(self):
        self.info = {
            "name" : "Whoami",
            "version" : "v1",
            "codename": "whoami",
            "dependencies" : [], # Not Supported.
            "description": "Who am I",
            "run": self.run
        }

    def run(self, info, pyt):
        print(pyt.info["user"])
