import sys, json, os, importlib, shutil
from colorama import Back, Fore, Style
from colorama import init as cinit
import argparse
sys.path.insert(0, "../types")
cinit()
from binary import Binary

from libs.package.configure import configure
class pkg(Binary):
    def __init__(self):
        self.info = {
            "name" : "pkg",
            "version" : "v1.0.0",
            "codename": "pkg",
            "dependencies" : [], # Not Supported.
            "run": self.run
        }


    def run(self, info, pyt):
        if not os.path.isdir(f"{info.info[14].basefs}/../temp/"):
            os.mkdir(f"{info.info[14].basefs}/../temp/")
        if os.path.isdir(f"{info.info[14].basefs}/../temp/pkg_build"):
            shutil.rmtree(f"{info.info[14].basefs}/../temp/pkg_build")

        os.mkdir(f"{info.info[14].basefs}/../temp/pkg_build")
        configure(info, pyt, f"{info.info[14].basefs}/../temp/pkg_build")
