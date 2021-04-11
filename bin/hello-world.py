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
            "on_load": self.startup
        }

    def startup(self, info):
        print("Hello World Program Loaded!")

    def run(self, info, pyt):
        print("test")
