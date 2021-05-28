import sys, json, os, importlib
from colorama import Back, Fore, Style
from colorama import init as cinit
import argparse
sys.path.insert(0, "../types")
cinit()
from binary import Binary
class Kpanic(Binary):
    def __init__(self):
        self.info = {
            "name" : "Panic",
            "version" : "v1",
            "codename": "kpanic",
            "dependencies" : [], # Not Supported.
            "description": "Devtool for creating kpanic",
            "run": self.run
        }

    def run(self, info, pyt):
        if not info.info[14].ksets["danger"]: return print("No-safety option disabled.")
        kpanic = "Not syncing!"
        if len(info.info[15].split(" ")[1:]) > 1: kpanic = info.info[15].split(" ")[1:]
        info.info[14].panic(kpanic)


