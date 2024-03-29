﻿import sys, json, os, importlib
from colorama import Back, Fore, Style
from colorama import init as cinit
import argparse
sys.path.insert(0, "../types")
cinit()
from binary import Binary
#class Binary():
 #   	pass
class chdir(Binary):
    def __init__(self):
        self.info = {
            "name" : "Change dir",
            "version" : "v1",
            "codename": "cd",
            "dependencies" : [], # Not Supported.
            "description": "Change working directory",
            "run": self.run
        }

    def json_load(self, file):
        with open(file, "r") as f:
            return json.load(f)

    def run(self, info, pyt):
        lang = self.json_load(f"{info.info[14].basefs}/../var/kernel_sets.json")["lang"]
        if os.path.isfile(f"{info.info[14].basefs}/../lang/chdir_{lang}.json"):
            with open(f"{info.info[14].basefs}/../lang/chdir_{lang}.json", "r") as f:
                lang = json.load(f)
        else:
            lang = {
                    "no_dir": "[Error] Unknown dir.",
                    "sysfs_err": "[Warning] SysFS not supported now."
                }
        args = info.info[15].split(" ")[1:]
        if len(args) > 0:
            args = args[0]
            args_2 = "".join(args[0:])
        else:
            return
        if pyt.fs[0] == "extfs":
#            print(os.path.abspath(pyt.fs[1].replace("\\", "/") + "/" + args.replace("\\", "/")))
            if os.path.isdir(os.path.abspath(pyt.fs[1].replace("\\", "/") + "/" + args.replace("\\", "/"))):
                pyt.fs[1] = os.path.abspath(pyt.fs[1].replace("\\", "/") + "/" + args.replace("\\", "/"))
            else:
                print(lang["no_dir"])
#            if os.path.isdir(os.path.abspath(args)):
#                pyt.fs[1] = os.path.abspath(args)
#            else:
#                if os.path.isdir(pyt.fs[1].replace("\\", "/") + "/" + args.replace("\\", "/")):
#                        pyt.fs[1] = pyt.fs[1].replace("\\", "/") + "/" + args.replace("\\", "/")
                #os.chdir(args_2)
                #pyt.fs[1] = os.getcwd()
#                else:
        elif pyt.fs[0] == "sysfs":
            print(lang["sysfs_err"])


