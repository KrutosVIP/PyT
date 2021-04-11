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
            "name" : "pkg",
            "version" : "v1.0.0",
            "codename": "pkg",
            "dependencies" : [], # Not Supported.
            "run": self.run,
            "on_load": self.startup
        }

    def startup(self, info):
        pass

    def run(self, info, pyt):
        print("Hello World!")
