﻿import sys, json, os, importlib
from colorama import Back, Fore, Style
from colorama import init as cinit
import argparse
sys.path.insert(0, "../types")
cinit()
from binary import Binary

class History(Binary):
    def __init__(self):
        self.info = {
            "name" : "Commands history.",
            "version" : "v1",
            "codename": "history",
            "dependencies" : [], # Not Supported.
            "description": "Get commands history",
            "run": self.run,
            "on_load": self.on_load
        }
    
    
    def json_load(self, file):
        with open(file, "r") as f:
            return json.load(f)
        
    def on_load(self, info):
        pass

    def run(self, info, pyt):
        lang = self.json_load("../var/kernel_sets.json")["lang"]
        if os.path.isfile(f"../lang/history_{lang}.json"):
            with open(f"../lang/history_{lang}.json", "r") as f:
                lang = json.load(f)
        else:
            lang = {
                    "history": "History:",
                    "cmd_args": ["Command:", "::Args:"],
                    "no_file": "[Error] No history yet."       
                }
        if os.path.exists("../var/history.json"):
            with open("../var/history.json") as f:
                history = json.load(f)
            print(lang["history"])
            cmd_num = 1
            for cmd in history["history"]:
                for cmd in cmd:
                    if not history["history"][cmd_num-1][cmd].isspace() and not history["history"][cmd_num-1][cmd] == "":
                        print(f"{cmd_num}: {lang['cmd_args'][0]} {cmd} - {history['history'][cmd_num-1][cmd]}")
                    else:
                        print(f"{cmd_num}: {lang['cmd_args'][0]} {cmd}")
                    cmd_num += 1
        else:
            print(lang["no_file"])
            
