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
            "run": self.run,
            "on_load": self.on_load
        }

    def on_load(self, info):
        pass

    def run(self, info, pyt):
        info.info[14].panic("Not syncing!")


