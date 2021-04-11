import sys, json, os, importlib
from colorama import Back, Fore, Style
from colorama import init as cinit
import argparse
sys.path.insert(0, "../types")
cinit()
from binary import Binary
class ChangeLang(Binary):
    def __init__(self):
        self.info = {
            "name" : "Changelang",
            "version" : "v1.0.0",
            "codename": ["changelang", "chlang", "locale"],
            "dependencies" : [], # Not Supported.
            "run": self.run,
            "on_load": self.startup
        }

    def startup(self, info):
        pass

    def json_load(self, file):
        with open(file, "r", encoding = "utf-8") as f:
            return json.load(f)
    
    def run(self, info, pyt):
        args = info.info[15].split(" ")[1:]
        lang = self.json_load("../var/kernel_sets.json")
        if len(args) < 1: return print(f"Language: {lang['lang']}")
        lang['lang'] = args[0]
        with open('../var/kernel_sets.json', 'w') as outfile:
            json.dump(lang, outfile)
        print("Default language is " + args[0])
        print("Restart your machine for applying changes")
