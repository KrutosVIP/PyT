﻿import sys, json, os, importlib
from colorama import Back, Fore, Style
from colorama import init as cinit
import argparse
sys.path.insert(0, "../types")
cinit()
from binary import Binary
class Exit(Binary):
    def __init__(self):
        self.info = {
            "name" : "Exit",
            "version" : "v1",
            "codename": ["exit", "poweroff"],
            "dependencies" : [], # Not Supported.
            "description": "Exit command.",
            "run": self.run
        }

    def run(self, info, pyt):
        return info.Exit


