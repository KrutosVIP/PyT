import sys, json, os
from colorama import Back, Fore, Style
from colorama import init as cinit
import argparse
from progress.bar import Bar
import tarfile
sys.path.insert(0, "../types")
from binary import Binary
class Binary():
    pass
class pkgbuild(Binary):
    def __init__(self):
        self.info = {
            "name" : "Build package",
            "version" : "v1.0.0",
            "codename": "pkg-build",
            "dependencies" : [], # Not Supported.
            "run": self.run,
            "on_load": self.load
        }

    def load(self, info):
        pass

    def configure(self, package):
        print("No config in directory! Generating config:")
        name = None
        while name == None:
            try:
                name = input("Input Package Name>")
            except:
                pass
        creator = None
        while creator == None:
            try:
                creator = input("Input Creator>")
            except:
                pass
        version = None
        while version == None:
            try:
                version = input("Version>")
            except:
                pass
        with open(f"{package}/config.json", encoding = "utf-8") as c:
            json.dump({"name": name, "creator": creator, "version": version}, c)
        return {"name": name, "creator": creator, "version": version}
    
    def run(self, info, pyt):
        args = info.info[15].split(" ")[1:]
        if len(args) < 1: return print("No package path.")
        package = args[0]
        if not os.path.exists(package):
            return print("Invalid package path!")
        if not os.path.exists(f"{package}/config.json"):
            config = self.configure(package)
        else:
            with open(f"{package}/config.json", encoding = "utf-8") as c:
                config = json.load(c)
        with tarfile.open(name=, mode='x:gz') as tar:
            pass
            
