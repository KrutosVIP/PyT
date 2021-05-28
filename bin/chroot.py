import sys, json, os, importlib
from colorama import Back, Fore, Style
from colorama import init as cinit
import argparse
sys.path.insert(0, "../types")
cinit()
from binary import Binary
class chroot(Binary):
    def __init__(self):
        self.info = {
            "name" : "Chroot",
            "version" : "v1.0.1",
            "codename": "chroot",
            "dependencies" : [], # Not Supported.
            "description": "Change root between extfs and sysfs.",
            "run": self.run
        }


    def json_load(self, file):
        with open(file, "r", encoding = "utf-8") as f:
            return json.load(f)

    def run(self, info, pyt):
        lang = self.json_load(f"{info.info[14].basefs}/../var/kernel_sets.json")["lang"]
        if os.path.isfile(f"{info.info[14].basefs}/../lang/chroot_{lang}.json"):
            with open(f"{info.info[14].basefs}/../lang/chroot_{lang}.json", "r", encoding = "utf-8") as f:
                lang = json.load(f)
        else:
            lang = {
                    "chroot": "Chrooted to {root}",
                    "unknown_fs": "Unknown fs to change root."
                }
        if pyt.fs[0] == "sysfs":
            pyt.fs = ["extfs", pyt.fs_type["extfs"]]
            print(lang["chroot"].replace("{root}", pyt.fs[0]))
        elif pyt.fs[0] == "extfs":
            pyt.fs = ["sysfs", pyt.fs_type["sysfs"]]
            print(lang["chroot"].replace("{root}", pyt.fs[0]))
        else:
            print(lang["unknown_fs"])

