import sys, json, os, importlib, requests
from colorama import Back, Fore, Style
from colorama import init as cinit
import argparse
sys.path.insert(0, "../types")
cinit()
from binary import Binary
class HelloWorld(Binary):
    def __init__(self):
        self.info = {
            "name" : "Download file from the Internet",
            "version" : "v1",
            "codename": "uget",
            "dependencies" : [], # Not Supported.
            "run": self.run,
            "on_load": self.startup
        }

    def startup(self, info):
        pass

    def run(self, info, pyt):
        args = info.info[15].split(" ")[1:]
        if len(args) < 1: return print("No URLs provided.")
        print("Downloading file from " + args[0])


