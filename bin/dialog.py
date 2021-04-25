import sys, json, os, importlib
from colorama import Back, Fore, Style
from colorama import init as cinit
import argparse
sys.path.insert(0, "../types")
cinit()
from binary import Binary

from prompt_toolkit.shortcuts import message_dialog

class dialog(Binary):
    def __init__(self):
        self.info = {
            "name" : "dialog",
            "version" : "v1",
            "codename": "dialog",
            "dependencies" : [], # Not Supported.
            "description": "Create message dialog",
            "run": self.run,
            "on_load": self.on_load
        }

    def on_load(self, info):
        pass
    def run(self, info, pyt):
        #Args module block
        args = info.info[15].split(" ")[1:]
        if len(args) > 0:
            args = " ".join(args[0:])
        else:
            args = "Hello World!"
        message_dialog(
        title='Dialog dev-test || prompt_toolkit',
        text= args).run()

