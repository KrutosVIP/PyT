import sys, json, os, importlib, urllib.request, shutil
from colorama import Back, Fore, Style
from colorama import init as cinit
import argparse
sys.path.insert(0, "../types")
cinit()
from binary import Binary
class HelloWorld(Binary):
    def __init__(self):
        self.info = {
            "name" : "Download file from the Internet",
            "version" : "v1.0.1",
            "codename": "uget",
            "dependencies" : [], # Not Supported.
            "run": self.run,
            "on_load": self.load
        }

    def load(self, info):
        pass

    def run(self, info, pyt):
        args = info.info[15].split(" ")[1:]
        if len(args) < 2: return print("No URLs or file path provided.")
        print("Downloading file from " + args[0])
        url = args[0]
        path = args[1]
        with urllib.request.urlopen(url) as rsp, open(path, 'wb') as outfile: shutil.copyfileobj(rsp, outfile)
        print("File downloaded")



