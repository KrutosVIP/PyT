import sys, json, os, importlib
from colorama import Back, Fore, Style
from colorama import init as cinit
import argparse
import subprocess
from sys import platform
sys.path.insert(0, "../types")
cinit()
from binary import Binary
class Clear(Binary):
    def __init__(self):
        self.info = {
            "name" : "Clear",
            "version" : "v1",
            "codename": ["clear", "cls"],
            "dependencies" : [], # Not Supported.
            "run": self.run,
            "on_load": self.on_load
        }

    def on_load(self, info):
        pass

    def run(self, info, pyt):
        if platform == "linux" or platform == "linux2":
            tmp = subprocess.call('clear', shell=True)
        elif platform == "win32" or platform == "darwin":
            tmp = subprocess.call('cls', shell=True)
        else:
            print("\n"*100)
