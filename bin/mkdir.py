import sys, json, os, importlib
from colorama import Back, Fore, Style
from colorama import init as cinit
import argparse
sys.path.insert(0, "../types")
cinit()
from slugify import slugify

from binary import Binary
class mkdir(Binary):
    def __init__(self):
        self.info = {
            "name" : "mkdir",
            "version" : "v1",
            "codename": "mkdir",
            "dependencies" : [], # Not Supported.
            "description": "Create some dirs maybe",
            "run": self.run
        }

    def json_load(self, file):
        with open(file, "r",  encoding = "utf-8") as f:
            return json.load(f)
    def create(self, dir):
        os.makedirs(dir)
        return
    def run(self, info, pyt):
        lang = self.json_load(f"{info.info[14].basefs}/../var/kernel_sets.json")["lang"]
        if os.path.isfile(f"{info.info[14].basefs}/../lang/rmdir_{lang}.json"):
            with open(f"{info.info[14].basefs}/../lang/rmdir_{lang}.json", "r") as f:
                lang = json.load(f)
        else:
            lang = {
                    "no_dir": "[Error] No input dirs",
                    "dir": "[Error] Cannot create existing dir.",
                    "sysfs_err": "[Warning] SysFS not supported now.",
                }
        args = info.info[15].split(" ")[1:]
        if len(args) > 0:
            args_2 = args[0:]
        else:
            print(lang["no_dir"])
            return
        if pyt.fs[0] == "extfs":
            for args in args_2:
                args = slugify(args)
                if not os.path.isdir(os.path.abspath(pyt.fs[1].replace("\\", "/") + "/" + args.replace("\\", "/"))):
                    self.create(os.path.abspath(pyt.fs[1].replace("\\", "/") + "/" + args.replace("\\", "/")))
                else:
                    print(lang["dir"])
                    return
            return
        elif pyt.fs[0] == "sysfs":
            print(lang["sysfs_err"])
