import sys, json, os, traceback, datetime
from prompt_toolkit.shortcuts import message_dialog

from prompt_toolkit.styles import Style
from colorama import init as cinit
import argparse, random
sys.path.insert(0, "../types")
sys.path.insert(0, "../")
sys.path.insert(0, "../libs")
from module import Module
from cpkg import fargparse
from slugify import slugify
from PyT.plm_utils import login_dialog
class Plm(Module):
    def __init__(self):
        self.info = {
            "name" : "PLM",
            "version" : "0.0.1",
            "codename": "plm",
            "dependencies" : [],
            "on_load" : self.on_load,
            "login-manager": True,
            "user": None
        }      

    def json_load(self, file):
        with open(file, "r", encoding = "utf-8") as f:
            return json.load(f)

    def on_load(self, info):
        pass
        
    def login(self, info):
        while self.info["user"] == None:
            try:
                if os.path.exists(f"{info[14].basefs}/../var/plm_colors.json"):
                    # Prompt Toolkit-Based Style
                    style = Style.from_dict(self.json_load(f"{info[14].basefs}/../var/plm_colors.json"))
                else:
                    style = None
                account = login_dialog(info[11]["plm"]["plm"], info[11]["pyt"]["login"]["login"], info[11]["plm"]["yes"], info[11]["plm"]["no"], style).run()
                user, passwd = account[0], account[1]
                if user in self.accs:
                    if self.accs[user] == None:
                        self.info["user"] = user

                if self.info["user"] == None:
                        
                    if not user in self.accs:
                        message_dialog(title= info[11]["plm"]["plm"],text=info[11]["pyt"]["login"]["invalid"]).run()
                    else:
                        if self.accs[user] != passwd:
                            message_dialog(title= info[11]["plm"]["plm"],text=info[11]["pyt"]["login"]["invalid"]).run()
                        elif self.accs[user] == passwd:
                            self.info["user"] = user
            except KeyboardInterrupt:
                print()
            except EOFError:
                print()

    def autologin(self, info):
        autolog = self.json_load(f"{info[14].basefs}/../var/kernel_sets.json")["autologin"]
        if autolog["active"]:
            print( info[11]["pyt"]["login"]["autologin"])
            user = autolog["account"]["name"]
            passwd = autolog["account"]["password"]
            if user in self.accs:
                if self.accs[user] == None:
                    self.info["user"] = user

                if self.info["user"] == None:
                    if not user in self.accs:
                        print(info[11]["pyt"]["login"]["invalid"])
                    else:
                        if self.accs[user] != passwd:
                            print(info[11]["pyt"]["login"]["invalid"])
                        elif self.accs[user] == passwd:
                            self.info["user"] = user
            if self.info["user"] == None:
                print(info[11]["pyt"]["login"]["auto_invalid"])


    def run(self, info):
        self.info["user"] = info[14].user
        
        if self.info["user"] == None:
            with open(f"{info[14].basefs}/../var/kernel_sets.json", "r") as f:
                d = f.read()
                accs = json.loads(d)["accounts"]
                accs_o = json.loads(d)["account_options"]
                self.accs = accs
                self.accs_o = accs_o
            del d
            print(info[11]["pyt"]["login"]["need"])
            
            self.autologin(info)
            self.login(info)
            return self.info["user"]
        

