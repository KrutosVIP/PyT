import sys, json, os, importlib
from colorama import Back, Fore, Style
from colorama import init as cinit
import argparse
sys.path.insert(0, "../types")
cinit()
from binary import Binary
class Pwd(Binary):
    def __init__(self):
        self.info = {
            "name" : "Pwd",
            "version" : "v1",
            "codename": "pwd",
            "dependencies" : [], # Not Supported.
            "description": "Get working directory",
            "run": self.run
        }

    def run(self, info, pyt):
        print(pyt.fs[1])


