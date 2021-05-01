import sys, json, os, traceback, datetime

from prompt_toolkit.styles import Style
from colorama import init as cinit
import argparse, random
sys.path.insert(0, "../types")
sys.path.insert(0, "../")
sys.path.insert(0, "../libs")
from module import Module
from cpkg import fargparse
from slugify import slugify
from PyT.plm_utils import login_dialog, input_dialog, input_dialog_inv, message_dialog, Exit

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

    def login_1(self, info, inv):
        while self.info["user"] == None:
            try:
                style = None
                user = input_dialog(info[11]["plm"]["plm"], info[11]["plm"]["login"] + "\n" + info[11]["pyt"]["login"]["login"], info[11]["plm"]["yes"], info[11]["plm"]["no"]).run()
                if type(user) == type(Exit):
                    return
                
                if user in self.accs:
                    if self.accs[user] == None:
                        self.info["user"] = user
                
                if self.info["user"] == None:
                    if not user in self.accs:
                        message_dialog(title= info[11]["plm"]["plm"],text=info[11]["pyt"]["login"]["invalid"]).run()
                    else:
                        if inv:
                            passwd = input_dialog_inv(info[11]["plm"]["plm"], info[11]["pyt"]["login"]["password"], info[11]["plm"]["yes"], info[11]["plm"]["no"], password = True).run()
                        else:
                            passwd = input_dialog(info[11]["plm"]["plm"], info[11]["pyt"]["login"]["password"], info[11]["plm"]["yes"], info[11]["plm"]["no"], password = True).run()
                        if type(passwd) == type(Exit):
                            return
                        if self.accs[user] != passwd:
                            message_dialog(title= info[11]["plm"]["plm"],text=info[11]["pyt"]["login"]["invalid"]).run()
                        elif self.accs[user] == passwd:
                            self.info["user"] = user
            except KeyboardInterrupt:
                print()
            except EOFError:
                print()

    def login(self, info, inv):
        while self.info["user"] == None:
            try:
                if os.path.exists(f"{info[14].basefs}/../var/plm_colors.json"):
                    # Prompt Toolkit-Based Style
                    style = Style.from_dict(self.json_load(f"{info[14].basefs}/../var/plm_colors.json"))
                else:
                    style = None
                account = login_dialog(info[11]["plm"]["plm"], info[11]["plm"]["login"], info[11]["plm"]["yes"], info[11]["plm"]["no"], inv, style).run()
                try:
                    user, passwd = account[0], account[1]
                except:
                    return
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
                self.plm = json.loads(d)["plm"]
            del d
            print(info[11]["pyt"]["login"]["need"])
            
            self.autologin(info)
            if self.plm["plm_type"] == 1:
                self.login(info, self.plm["invisible"])
            elif self.plm["plm_type"] == 2:
                self.login_1(info, self.plm["invisible"])
            elif self.plm["plm_type"] == 0:
                pass
            else:
                self.login(info, self.plm["invisible"])
            return self.info["user"]
        

