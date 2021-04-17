import sys, json, os, importlib
from colorama import Back, Fore, Style
from colorama import init as cinit
import argparse
sys.path.insert(0, "../types")
cinit()
from binary import Binary
class listdir(Binary):
    def __init__(self):
        self.info = {
            "name" : "List files in dir",
            "version" : "v1",
            "codename": "ls",
            "dependencies" : [], # Not Supported.
            "description": "Change working directory",
            "run": self.run,
            "on_load": self.on_load
        }

        self.types = {
                "dir": f"{Back.BLACK}{Fore.GREEN}",
                ".gz": f"{Fore.LIGHTRED_EX}",
                ".py": f"{Fore.LIGHTGREEN_EX}",
                ".png": f"{Fore.CYAN}"
            }

    def on_load(self, info):
        pass

    def json_load(self, file):
        with open(file, "r") as f:
            return json.load(f)

    def listdir(self, dir):
        for file in os.listdir(dir):
            if os.path.isfile(file):
                if os.path.splitext(file)[1] in self.types:
                    print(self.types[os.path.splitext(file)[1]], file, Style.RESET_ALL, end = " ")
                else:
                    print(file, end = " ")
            else: 
                print(self.types["dir"], file, Style.RESET_ALL, end = " ")
        print()
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
            self.listdir(pyt.fs[1])
            return
        if pyt.fs[0] == "extfs":
            if os.path.isdir(os.path.abspath(pyt.fs[1].replace("\\", "/") + "/" + args.replace("\\", "/"))):
                self.listdir(os.path.abspath(pyt.fs[1].replace("\\", "/") + "/" + args.replace("\\", "/")))
                return
            else:
                print(lang["no_dir"])
                return
        elif pyt.fs[0] == "sysfs":
            print(lang["sysfs_err"])
