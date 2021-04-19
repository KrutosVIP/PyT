import sys, json, os, importlib
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
            "version" : "v1.0.1",
            "codename": "history",
            "dependencies" : [], # Not Supported.
            "description": "Get commands history",
            "run": self.run,
            "on_load": self.on_load
        }
    
    
    def json_load(self, file):
        with open(file, "r", encoding = "utf-8") as f:
            return json.load(f)
        
    def on_load(self, info):
        pass

    def run(self, info, pyt):
        lang = self.json_load(f"{info.info[14].basefs}/../var/kernel_sets.json")["lang"]
        if os.path.isfile(f"{info.info[14].basefs}/../lang/history_{lang}.json"):
            with open(f"{info.info[14].basefs}/../lang/history_{lang}.json", "r", encoding = "utf-8") as f:
                lang = json.load(f)
        else:
            lang = {
                    "history": "History:",
                    "cmd_args": ["Command:", "::Args:"],
                    "no_file": "[Error] No history yet."       
                }
        if os.path.exists(f"{info.info[14].basefs}/../data/{pyt.info['user']}/.history"):
            with open(f"{info.info[14].basefs}/../data/{pyt.info['user']}/.history", encoding = "utf-8") as f:
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
            

