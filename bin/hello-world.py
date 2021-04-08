import sys, json, os, importlib
from colorama import Back, Fore, Style
from colorama import init as cinit
import argparse
sys.path.insert(0, "../types")
cinit()
from binary import Binary
class HelloWorld(Binary):
    def __init__(self):
        self.info = {
            "name" : "Hello World program",
            "version" : "v1",
            "codename": "helloworld",
            "dependencies" : [], # Not Supported.
            "run": self.run,
            "on_load": self.on_load
        }

    def on_load(self, info):
        pass #do something

    def run(self, info, pyt):
        print("test")
