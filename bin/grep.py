import sys, json, os, importlib
from colorama import Back, Fore, Style
from colorama import init as cinit
import argparse
sys.path.insert(0, "../types")
cinit()
from binary import Binary
class Grep(Binary):
    def __init__(self):
        self.info = {
            "name" : "grep",
            "version" : "v1",
            "codename": "grep",
            "dependencies" : [], # Not Supported.
            "description": "Grep info from file",
            "run": self.run,
            "on_load": self.on_load
        }

    def on_load(self, info):
        pass

    def json_load(self, file):
        with open(file, "r",  encoding = "utf-8") as f:
            return json.load(f)

    def grep(self, file, text):
        with open(file, "r", encoding = "utf-8") as f:
            data = f.read().split("\n")

        grep = []
        
        index = 1
        for string in data:
            if text in string:
                grep.append(f"Line {index}: " + string.replace(text, "".join([Style.RESET_ALL, Fore.LIGHTRED_EX, text, Style.RESET_ALL])) + "\n")
                grep.append("...\n")
            index += 1

        return print("".join(grep))
    def run(self, info, pyt):
        lang = self.json_load(f"{info.info[14].basefs}/../var/kernel_sets.json")["lang"]
        if os.path.isfile(f"{info.info[14].basefs}/../lang/grep_{lang}.json"):
            with open(f"{info.info[14].basefs}/../lang/grep_{lang}.json", "r") as f:
                lang = json.load(f)
        else:
            lang = {
                    "no_file": "[Error] Unknown file or no grep args.",
                    "sysfs_err": "[Warning] SysFS not supported now."
                }
        args = info.info[15].split(" ")[1:]
        if len(args) > 1:
            args_2 = "".join(args[1:])
            args = args[0]

        else:
            print(lang["no_file"])
            return
        if pyt.fs[0] == "extfs":
            if os.path.isfile(os.path.abspath(pyt.fs[1].replace("\\", "/") + "/" + args.replace("\\", "/"))):
                self.grep(os.path.abspath(pyt.fs[1].replace("\\", "/") + "/" + args.replace("\\", "/")), args_2)
                return 
            else:
                print(lang["no_file"])
                return
        elif pyt.fs[0] == "sysfs":
            print(lang["sysfs_err"])
