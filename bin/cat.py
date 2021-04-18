import sys, json, os, importlib
from colorama import Back, Fore, Style
from colorama import init as cinit
import argparse
sys.path.insert(0, "../types")
cinit()
from binary import Binary
class cat(Binary):
    def __init__(self):
        self.info = {
            "name" : "Cat",
            "version" : "v1",
            "codename": "cat",
            "dependencies" : [], # Not Supported.
            "description": "Cat file",
            "run": self.run,
            "on_load": self.on_load
        }

    def on_load(self, info):
        pass

    def json_load(self, file):
        with open(file, "r",  encoding = "utf-8") as f:
            return json.load(f)

    def read(self, file):
        with open(file, "r", encoding = "utf-8") as f:
            return print(f.read())
    def run(self, info, pyt):
        lang = self.json_load(f"{info.info[14].basefs}/../var/kernel_sets.json")["lang"]
        if os.path.isfile(f"{info.info[14].basefs}/../lang/chdir_{lang}.json"):
            with open(f"{info.info[14].basefs}/../lang/chdir_{lang}.json", "r") as f:
                lang = json.load(f)
        else:
            lang = {
                    "no_file": "[Error] Unknown file.",
                    "sysfs_err": "[Warning] SysFS not supported now."
                }
        args = info.info[15].split(" ")[1:]
        if len(args) > 0:
            args = args[0]
            args_2 = "".join(args[0:])
        else:
            print(lang["no_file"])
        if pyt.fs[0] == "extfs":
            if os.path.isfile(os.path.abspath(pyt.fs[1].replace("\\", "/") + "/" + args.replace("\\", "/"))):
                self.read(os.path.abspath(pyt.fs[1].replace("\\", "/") + "/" + args.replace("\\", "/")))
                return 
            else:
                print(lang["no_file"])
                return
        elif pyt.fs[0] == "sysfs":
            print(lang["sysfs_err"])
