import sys, json, os, importlib
from colorama import Back, Fore, Style
from colorama import init as cinit
import argparse
sys.path.insert(0, "../types")
cinit()
from binary import Binary
class Help(Binary):
    def __init__(self):
        self.info = {
            "name" : "Manuals",
            "version" : "v1",
            "codename": ["help", "man"],
            "dependencies" : [], # Not Supported.
            "description": "help - Args - command name",
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
        if os.path.isfile(f"../lang/help_{lang}.json"):
            with open(f"../lang/help_{lang}.json", "r", encoding = "utf-8") as f:
                lang = json.load(f)
        else:
            lang = {
                    "help": "Help for {cmd}:",
                    "name": "Name:",
                    "codename": "Command:",
                    "desc": "Description:",
                    "alias": "Aliases:",
                    "version": "Version:",
                    "seek_manual": "Trying to find manual for command {cmd}",
                    "all": "All commands:", 
                    "no_lang_1": "Can`t find manual for {cmd}.",
                    "no_lang_2": "Trying to find manual on English",
                    "no_lang_3": "Are you typed existing command? Try to reinstall package.",
                    "no_lang_4": "No manual find!",
                    "no_args": "Looks like you typed a space."
                }
        man = None
        if len(info.info[15].split(" ")) > 1:
            args = info.info[15].split(" ")[1]
        else:
            args = "all"
        lang_g = self.json_load("../var/kernel_sets.json")["lang"]
        if (args.isspace() or args == "") and args != "all":
            print(lang["no_args"])
            return 
        if args != "all":
            print(lang["seek_manual"].replace("{cmd}", args))
            if os.path.isfile(f"../man/{args}_{lang_g}.json"):
                with open(f"../man/{args}_{lang_g}.json", "r", encoding = "utf-8") as f:
                    man = json.load(f)
            else:
                print(lang["no_lang_1"].replace("{cmd}", args), lang["no_lang_2"])
                if os.path.isfile(f"../man/{args}_en.json"):
                    with open(f"../man/{args}_en.json", "r", encoding = "utf-8") as f:
                        man = json.load(f)
                else:
                    print(lang["no_lang_4"].replace("{cmd}", args), lang["no_lang_3"])
                    
        if man != None:
            print(lang["help"].replace("{cmd}", args))

            if "name" in man:
                if man["name"] != None:
                    print(lang["name"], man["name"])

            if "version" in man:
                if man["version"] != None:
                    print(lang["version"], man["version"])

            if "codename" in man:
                if man["codename"] != None:
                    print(lang["codename"], man["codename"])

            if "alias" in man:
                if man["alias"] != None:
                    if type(man["alias"]).__name__ not in ("list", "tuple"):
                        print(lang["alias"], man["alias"])
                    else:
                        print(lang["alias"], ", ".join(man["alias"]))

            if "description" in man:
                if man["description"] != None:
                    print(lang["desc"], man["description"])
        elif args == "all":
            print(lang["all"])
            print(", ".join(info.info[10].keys()))
            
