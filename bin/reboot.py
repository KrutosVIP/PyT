import sys, json, os, importlib
from colorama import Back, Fore, Style
from colorama import init as cinit
import argparse
sys.path.insert(0, "../types")
cinit()
from binary import Binary
class Reboot(Binary):
    def __init__(self):
        self.info = {
            "name" : "Reboot.",
            "version" : "v1",
            "codename": "reboot",
            "dependencies" : [], # Not Supported.
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
        if os.path.isfile(f"../lang/reboot_{lang}.json"):
            with open(f"../lang/reboot_{lang}.json", "r") as f:
                lang = json.load(f)
        else:
            lang = {
                    "boot_option": ["[Success] Installed {args} boot option", "[Success] Installed os boot option"],
                    "unknown_boot": "[Error] Unknown boot option.",
                    "no_file": "[Error] No /var/boot.json!"       
                }
        args = info.info[15].split(" ")[1:]
        if len(args) > 0:
            args = args[0]
            if os.path.isfile("../var/boot.json"):
                with open("../var/boot.json", "r") as f:
                    b = json.load(f)
                if args in ["recovery", "os"]:
                    b["boot"] = args
                    with open("../var/boot.json", "w") as f:
                        json.dump(b, f)
                    print(lang["boot_option"][0].replace("{args}", args))
                    reboot()
                else:
                    print()
            else:
                print(lang["no_file"])
        else:
            if os.path.isfile("../var/boot.json"):
                with open("../var/boot.json", "r") as f:
                    b = json.load(f)
                    b["boot"] = "os"
                    
                    with open("../var/boot.json", "w") as f:
                        json.dump(b, f)
                        
                    print(lang["boot_option"][1])
                    reboot()
            else:
                print(lang["no_file"])

def reboot():
    os.chdir("..")
    for f in dir():
        if f not in ["importlib"]:
            del f
    def dynamic_import(module):
        return importlib.import_module(module)
    r = dynamic_import("kinit").main()
    sys.exit()
