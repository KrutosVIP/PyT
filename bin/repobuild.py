import sys, json, os
from colorama import Back, Fore, Style
from colorama import init as cinit
import argparse
import tarfile
sys.path.insert(0, "../types")
#from binary import Binary
class Binary:
    pass
# COMMAND DISABLED DUE TO PROBLEMS
sys.path.insert(0, "../libs")
from dev_build.repobuild import RepoBuild
class repobuild(Binary):
    def __init__(self):
        self.info = {
            "name" : "Build repo",
            "version" : "v1.0.0",
            "codename": "repobuild",
            "dependencies" : [], # Not Supported.
            "run": self.run
        }

    def run(self, info, pyt):
        RepoBuild.run_repobuild(self, info, pyt)





    

