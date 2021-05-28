import sys, json, os
from colorama import Back, Fore, Style
from colorama import init as cinit
import argparse
import tarfile
sys.path.insert(0, "../types")
# from binary import Binary
# COMMAND DISABLED DUE TO PROBLEMS
class Binary:
    pass
class Pkgbuild(Binary):
    def __init__(self):
        self.info = {
            "name" : "Build package",
            "version" : "v1.0.0",
            "codename": "pkgbuild",
            "dependencies" : [], # Not Supported.
            "run": self.run
        }

    def configure(self, package, pyt):
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
        dependencies = None
        while dependencies == None:
            try:
                dependencies = input("Dependencies(write with spaces)>")
            except:
                pass
        if not os.path.isdir(os.path.abspath(pyt.fs[1].replace("\\", "/") + "/" + package.replace("\\", "/") + "/temp/")):
            os.mkdir(os.path.abspath(pyt.fs[1].replace("\\", "/") + "/" + package.replace("\\", "/") + "/temp/"))
        with open(os.path.abspath(pyt.fs[1].replace("\\", "/") + "/" + package.replace("\\", "/") + "/temp/config.json").replace("//", "/"), "w", encoding = "utf-8") as c:
            json.dump({"name": name, "creator": creator, "version": version, "dependencies": dependencies}, c)
        return {"name": name, "creator": creator, "version": version, "dependencies": dependencies}
    
    def run(self, info, pyt):
        args = info.info[15].split(" ")[1:]
        if len(args) < 1: package = "."
        else: package = args[0]
        if not os.path.exists(os.path.abspath(pyt.fs[1].replace("\\", "/") + "/" + package.replace("\\", "/"))):
            return print("Invalid package path!")
        if not os.path.exists(os.path.abspath(pyt.fs[1].replace("\\", "/") + "/" + package.replace("\\", "/") + "/temp/config.json").replace("//", "/")):
            config = self.configure(package, pyt)
        else:
            with open(os.path.abspath(pyt.fs[1].replace("\\", "/") + "/" + package.replace("\\", "/") + "/temp/config.json").replace("//", "/"), encoding = "utf-8") as c:
                config = json.load(c)
        if os.path.isfile(os.path.abspath(pyt.fs[1].replace("\\", "/") + "/" + package.replace("\\", "/") + "/" + f"{config['name']}_{config['version']}.tar.gz")):
            os.remove(os.path.abspath(pyt.fs[1].replace("\\", "/") + "/" + package.replace("\\", "/") + "/" + f"{config['name']}_{config['version']}.tar.gz"))
        with tarfile.open(name=os.path.abspath(pyt.fs[1].replace("\\", "/") + "/" + package.replace("\\", "/") + "/" + f"{config['name']}.{config['version']}.pkg.tar.gz"), mode='x:gz') as tar:
            for obj in os.listdir(os.path.abspath(pyt.fs[1].replace("\\", "/") + "/" + package.replace("\\", "/"))):
                tar.add(os.path.abspath(pyt.fs[1].replace("\\", "/") + "/" + package.replace("\\", "/") + "/" + obj), arcname = obj)
            
