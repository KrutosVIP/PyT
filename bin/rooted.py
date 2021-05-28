import sys, json, os, importlib
from colorama import Back, Fore, Style
from colorama import init as cinit
import argparse
sys.path.insert(0, "../types")
cinit()
from binary import Binary
class rooted(Binary):
    def __init__(self):
        self.info = {
            "name" : "Rooted?",
            "version" : "v1",
            "codename": ["amirooted", "rooted"],
            "dependencies" : [], # Not Supported.
            "description": "Am I rooted?",
            "run": self.run
        }

    def run(self, info, pyt):
        danger = ""
        if info.info[14].ksets["danger"]: danger = " [NOT-SAFETY OPTION - NO UNROOTED ACCS!]"
        if pyt.accs_o[pyt.info["user"]]["root_acc"]:
            print(f"Rooted!{danger}")
        else:
            print(f"Not rooted.")
