import sys, json, os, importlib
from colorama import Back, Fore, Style
from colorama import init as cinit
import argparse
sys.path.insert(0, "../types")
cinit()
from binary import Binary
class Relogin(Binary):
    def __init__(self):
        self.info = {
            "name" : "Re-login",
            "version" : "v1",
            "codename": "relogin",
            "dependencies" : [], # Not Supported.
            "description": "Re-login into account.",
            "run": self.run,
            "on_load": self.on_load
        }

    def json_load(self, file):
        with open(file, "r") as f:
            return json.load(f)

    def on_load(self, info):
        pass

    def run(self, info, pyt):
        lang = self.json_load("../var/kernel_sets.json")["lang"]
        if os.path.isfile(f"../lang/relogin_{lang}.json"):
            with open(f"../lang/relogin_{lang}.json", "r") as f:
                lang = json.load(f)
        else:
            lang = {
                    "relogin": "Re-loggined as {user}",
                    "error": "Cannot relogin."
                }

        old_user = pyt.info["user"]
        pyt.info["user"] = None
        pyt.login(info.info)
        if pyt.info["user"] == None:
            pyt.info["user"] = old_user
            print(lang["error"])
        else:
            print(lang["relogin"].replace("{user}", pyt.info["user"]))
        


