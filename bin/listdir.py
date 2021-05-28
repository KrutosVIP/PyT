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
            "description": "List files in dir",
            "run": self.run
        }

        self.types = {
                "dir": f"{Back.BLACK}{Fore.GREEN}",
                ".gz": f"{Fore.LIGHTRED_EX}",
                ".py": f"{Fore.LIGHTGREEN_EX}",
                ".png": f"{Fore.CYAN}",
                ".sh": f"{Fore.RED}"
            }

    def json_load(self, file):
        with open(file, "r",  encoding = "utf-8") as f:
            return json.load(f)

    def listdir(self, dir):
        i = 1
        for file in os.listdir(dir):
            #print(os.path.isfile(dir.replace("\\", "/") + "/" + file.replace("\\", "/")))
            if os.path.isfile(dir.replace("\\", "/") + "/" + file.replace("\\", "/")):
                if os.path.splitext(file)[1] in self.types:
                    if " " in list(file):
                        print(self.types[os.path.splitext(file)[1]]+"'" + file+ "'"+Style.RESET_ALL, end = " ")
                    else:
                        print(self.types[os.path.splitext(file)[1]]+file+ Style.RESET_ALL, end = " ")
                    #print(self.types[os.path.splitext(file)[1]], os.path.splitext(file)[1], Style.RESET_ALL)
                        
                else:
                    if " " in list(file):
                        print("'"+file+"'", end = " ")
                    else:
                        print(file, end = " ")
            else:
                if " " in list(file):
                    print(self.types["dir"]+ '"'+ file + '"'+ Style.RESET_ALL, end = " ")
                else:
                    print(self.types["dir"]+ file+ Style.RESET_ALL, end = " ")
            if i == 6:
                i = 0
                print()
            i+=1
        print()
    def run(self, info, pyt):
        lang = self.json_load(f"{info.info[14].basefs}/../var/kernel_sets.json")["lang"]
        if os.path.isfile(f"{info.info[14].basefs}/../lang/listdir_{lang}.json"):
            with open(f"{info.info[14].basefs}/../lang/listdir_{lang}.json", "r") as f:
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
            if pyt.fs[0] == "extfs":
                self.listdir(pyt.fs[1])
                return
            else:
                print(lang["sysfs_err"])
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
            return
