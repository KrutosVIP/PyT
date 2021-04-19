import sys, json, os, importlib
from colorama import Back, Fore, Style
from colorama import init as cinit
import re
import argparse
sys.path.insert(0, "../types")
cinit()

from slugify import slugify

from binary import Binary
class touch(Binary):
    def __init__(self):
        self.info = {
            "name" : "Touch",
            "version" : "v1",
            "codename": "touch",
            "dependencies" : [], # Not Supported.
            "description": "Create new file without anything.",
            "run": self.run,
            "on_load": self.on_load
        }

    def on_load(self, info):
        pass

    def json_load(self, file):
        with open(file, "r",  encoding = "utf-8") as f:
            return json.load(f)

    def create(self, file):
        with open(file, "w", encoding = "utf-8") as f:
            pass
        return
    def run(self, info, pyt):
        lang = self.json_load(f"{info.info[14].basefs}/../var/kernel_sets.json")["lang"]
        if os.path.isfile(f"{info.info[14].basefs}/../lang/touch_{lang}.json"):
            with open(f"{info.info[14].basefs}/../lang/touch_{lang}.json", "r") as f:
                lang = json.load(f)
        else:
            lang = {
                    "file": "[Error] File exists.",
                    "no_file": "[Error] No input files",
                    "sysfs_err": "[Warning] SysFS not supported now."
                }
        args = info.info[15].split(" ")[1:]
        if len(args) > 0:
            args_2 = args[0:]
        else:
            print(lang["no_file"])
            return
        if pyt.fs[0] == "extfs":
            for args in args_2:
                args = os.path.splitext(args)
                args = slugify(args[0]) + "." + slugify(args[1])
                if os.path.isfile(os.path.abspath(pyt.fs[1].replace("\\", "/") + "/" + args.replace("\\", "/"))):
                    print(lang["file"])
                else:
                    self.create(os.path.abspath(pyt.fs[1].replace("\\", "/") + "/" + args.replace("\\", "/")))
            return
        elif pyt.fs[0] == "sysfs":
            print(lang["sysfs_err"])
