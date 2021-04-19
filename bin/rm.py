import sys, json, os, importlib
from colorama import Back, Fore, Style
from colorama import init as cinit
import re
import argparse
sys.path.insert(0, "../types")
cinit()


from binary import Binary
class remove(Binary):
    def __init__(self):
        self.info = {
            "name" : "rm",
            "version" : "v1",
            "codename": "rm",
            "dependencies" : [], # Not Supported.
            "description": "Remove some files",
            "run": self.run,
            "on_load": self.on_load
        }

    def on_load(self, info):
        pass

    def json_load(self, file):
        with open(file, "r",  encoding = "utf-8") as f:
            return json.load(f)

    def remove_all(self, dir, pyt):
        for file in os.listdir(dir):
            if os.path.isfile(os.path.abspath(dir.replace("\\", "/") + "/" + file.replace("\\", "/"))):
                self.remove(os.path.abspath(dir.replace("\\", "/") + "/" + file.replace("\\", "/")))
    def remove(self, file):
        os.remove(file)
        return
    def run(self, info, pyt):
        lang = self.json_load(f"{info.info[14].basefs}/../var/kernel_sets.json")["lang"]
        if os.path.isfile(f"{info.info[14].basefs}/../lang/rm_{lang}.json"):
            with open(f"{info.info[14].basefs}/../lang/rm_{lang}.json", "r") as f:
                lang = json.load(f)
        else:
            lang = {
                    "no_file": "[Error] No input files",
                    "dir": "[Error] Cannot remove dir.",
                    "sysfs_err": "[Warning] SysFS not supported now.",
                    "unknown_file": "[Error] Unknown file(-s)!"
                }
        args = info.info[15].split(" ")[1:]
        if len(args) > 0:
            args_2 = args[0:]
        else:
            print(lang["no_file"])
            return
        if pyt.fs[0] == "extfs":
            for args in args_2:
                if args.replace("\\", "/").endswith("/*"):
                    args = args[:-2]
                    if os.path.isdir(os.path.abspath(pyt.fs[1].replace("\\", "/") + "/" + args.replace("\\", "/"))):
                        self.remove_all(os.path.abspath(pyt.fs[1].replace("\\", "/") + "/" + args.replace("\\", "/")), pyt)
                    return
                if os.path.isfile(os.path.abspath(pyt.fs[1].replace("\\", "/") + "/" + args.replace("\\", "/"))):
                    self.remove(os.path.abspath(pyt.fs[1].replace("\\", "/") + "/" + args.replace("\\", "/")))
                else:
                    if os.path.isdir(os.path.abspath(pyt.fs[1].replace("\\", "/") + "/" + args.replace("\\", "/"))):
                        print(lang["dir"])
                        return
                    print(lang["unknown_file"])
                    return
            return
        elif pyt.fs[0] == "sysfs":
            print(lang["sysfs_err"])
