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
            "version" : "v1.1.0",
            "codename": "helloworld",
            "dependencies" : [], # Not Supported.
            "run": self.run
        }

    def run(self, info, pyt):
        print("Hello World!")
