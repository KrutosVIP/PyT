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

    def ToFile(self, text, file):
        with open(file, "w", encoding = "utf-8") as f:
            f.write(text)

    def read_tf(self, file, file2):
        with open(file, "r", encoding = "utf-8") as f:
            return self.ToFile(f.read(), file2)
    
    def json_load(self, file):
        with open(file, "r",  encoding = "utf-8") as f:
            return json.load(f)

    def read(self, file):
        with open(file, "r", encoding = "utf-8") as f:
            return print(f.read())
    def run(self, info, pyt):

        # Lang block with multiple reuse
        lang = self.json_load(f"{info.info[14].basefs}/../var/kernel_sets.json")["lang"]
        if os.path.isfile(f"{info.info[14].basefs}/../lang/{self.info['codename']}_{lang}.json"):
            with open(f"{info.info[14].basefs}/../lang/{self.info['codename']}_{lang}.json", "r") as f:
                lang = json.load(f)
        else:
            lang = {
                    "no_file": "[Error] Unknown file.",
                    "sysfs_err": "[Warning] SysFS not supported now."
                }

        #Args module block
        args = info.info[15].split(" ")[1:]
        if len(args) > 0:
            args_2 = "".join(args[0:])
            args = args[0]
            to_file = False
            if len(args) > 1:
                if ">" in args_2:
                    args_2 = args_2.split(">")
                    args_2 = [args_2[0], "".join(args_2[1:])]
                    to_file = True
                    
        else:
            print(lang["no_file"])
            return
        # EXT FS only block
        if pyt.fs[0] == "extfs":

            if to_file:
                if os.path.isfile(os.path.abspath(pyt.fs[1].replace("\\", "/") + "/" + args_2[0].replace("\\", "/"))):
                    self.read_tf(args_2[0], args_2[1])
                    return
                else:
                    print(lang["no_file"])
                    return
                
            if os.path.isfile(os.path.abspath(pyt.fs[1].replace("\\", "/") + "/" + args.replace("\\", "/"))):
                self.read(os.path.abspath(pyt.fs[1].replace("\\", "/") + "/" + args.replace("\\", "/")))
                return 
            else:
                print(lang["no_file"])
                return
        elif pyt.fs[0] == "sysfs":
            print(lang["sysfs_err"])
