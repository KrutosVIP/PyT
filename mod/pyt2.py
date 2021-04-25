import sys, json, os, traceback, importlib, datetime

def dynamic_import(module):
    return importlib.import_module(module)

from prompt_toolkit import PromptSession, prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.styles import Style as PStyle
from prompt_toolkit import print_formatted_text
from prompt_toolkit.formatted_text import HTML

from colorama import Back, Fore, Style
from colorama import init as cinit
import argparse, random
sys.path.insert(0, "../types")
sys.path.insert(0, "../libs")
sys.path.insert(0, "../")

from PyT.prompt_utils import InputValidator, PTSTD, InputMethod
from PyT.redirectors import redirect, redirect_write
from PyT.STD import STDLib
from PyT.startup_utils import pytrc, welcome_text
from PyT.cmd_utils import file_exec, cmd_exec
from PyT.executor import execute, executable

from module import Module
from cpkg import fargparse
from slugify import slugify

        
class PyT2(Module):
    def __init__(self):
        self.info = {
            "name" : "PyT v2",
            "version" : "0.0.1",
            "codename": "pyt2",
            "dependencies" : [],
            "on_load" : self.on_load,
            "console": True,
            "user": None
        }
        self.session = PromptSession()
        


    def json_load(self, file):
        with open(file, "r") as f:
            return json.load(f)

    def on_load(self, info):
        self.kinfo = info
        self.error = 0
        for mod in info[10]:
            info[10][mod].info["on_load"](info)
        cinit()
        
    def color(self, text):
        text = text.replace('{back.black}', Back.BLACK).replace('{back.blue}', Back.BLUE).replace('{back.cyan}', Back.CYAN).replace('{back.green}', Back.GREEN).replace('{back.lightblack_ex}', Back.LIGHTBLACK_EX).replace('{back.lightblue_ex}', Back.LIGHTBLUE_EX).replace('{back.lightcyan_ex}', Back.LIGHTCYAN_EX).replace('{back.lightgreen_ex}', Back.LIGHTGREEN_EX).replace('{back.lightmagenta_ex}', Back.LIGHTMAGENTA_EX).replace('{back.lightred_ex}', Back.LIGHTRED_EX).replace('{back.lightwhite_ex}', Back.LIGHTWHITE_EX).replace('{back.lightyellow_ex}', Back.LIGHTYELLOW_EX).replace('{back.magenta}', Back.MAGENTA).replace('{back.red}', Back.RED).replace('{back.reset}', Back.RESET).replace('{back.white}', Back.WHITE).replace('{back.yellow}', Back.YELLOW)
        text = text.replace('{fore.black}', Fore.BLACK).replace('{fore.blue}', Fore.BLUE).replace('{fore.cyan}', Fore.CYAN).replace('{fore.green}', Fore.GREEN).replace('{fore.lightblack_ex}', Fore.LIGHTBLACK_EX).replace('{fore.lightblue_ex}', Fore.LIGHTBLUE_EX).replace('{fore.lightcyan_ex}', Fore.LIGHTCYAN_EX).replace('{fore.lightgreen_ex}', Fore.LIGHTGREEN_EX).replace('{fore.lightmagenta_ex}', Fore.LIGHTMAGENTA_EX).replace('{fore.lightred_ex}', Fore.LIGHTRED_EX).replace('{fore.lightwhite_ex}', Fore.LIGHTWHITE_EX).replace('{fore.lightyellow_ex}', Fore.LIGHTYELLOW_EX).replace('{fore.magenta}', Fore.MAGENTA).replace('{fore.red}', Fore.RED).replace('{fore.reset}', Fore.RESET).replace('{fore.white}', Fore.WHITE).replace('{fore.yellow}', Fore.YELLOW)
        text = text.replace('{style.bright}', Style.BRIGHT).replace('{style.dim}', Style.DIM).replace('{style.normal}', Style.NORMAL).replace('{style.reset_all}', Style.RESET_ALL)
        return text

    def login(self, info):
        while self.info["user"] == None:
            try:
                user = input(info[11]["pyt"]["login"]["login"])
                if user in self.accs:
                    if self.accs[user] == None:
                        self.info["user"] = user

                if self.info["user"] == None:
                    passwd = prompt(info[11]["pyt"]["login"]["password"], is_password = True)
                        
                    if not user in self.accs:
                        print(info[11]["pyt"]["login"]["invalid"])
                    else:
                        if self.accs[user] != passwd:
                            print(info[11]["pyt"]["login"]["invalid"])
                        elif self.accs[user] == passwd:
                            self.info["user"] = user
            except KeyboardInterrupt:
                print()

    def autologin(self, info):
        autolog = self.json_load(f"{info[14].basefs}/../var/kernel_sets.json")["autologin"]
        if autolog["active"]:
            print(info[11]["pyt"]["login"]["autologin"])
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
        self.fs_type = {"extfs": os.getcwd(), "sysfs": "/"}
        self.fs = ["extfs", self.fs_type["extfs"]]

        welcome_text(info, self, Style)
        self.info["user"] = info[14].user
        

        with open(f"{info[14].basefs}/../var/kernel_sets.json", "r") as f:
            d = f.read()
            accs = json.loads(d)["accounts"]
            accs_o = json.loads(d)["account_options"]
            self.accs = accs
            self.accs_o = accs_o
            del d
        if self.info["user"] == None:
            print(info[11]["pyt"]["login"]["need"])
            
            self.autologin(info)
            self.login(info)
            
        session = True
        print(info[11]['pyt']["current_root"].replace("{root}", self.fs[0]))
        pytrc(self, info)
        
        while session:
            try:
                if len(self.fs[1]) > 40:
                    self.tempfs = "..." + self.fs[1][len(self.fs[1])-40:]
                else:
                    self.tempfs = self.fs[1]

                u_i = InputMethod(self, accs_o[self.info["user"]]["root_acc"], PStyle, info)     
                parse = u_i.split(" ")
                
                try:

                    cmd_exc_temp = cmd_exec(self, parse, info, u_i, PTSTD, redirect, STDLib)
                    if not cmd_exc_temp:
                        redir, sys.stdout = file_exec(self, redirect, PTSTD, u_i, execute, executable, parse) 
                        if redir:
                            pass
                        elif not u_i.isspace() and not u_i == "":
                            print(info[11]['pyt']['invalid_command'].replace("{cmd}", parse[0]))
                            
                # Get command/file exception
                except Exception as e:
                    traceback.print_exc()
                    
            # Get all keyboard interrupts
            except KeyboardInterrupt:
                print()
            except EOFError:
                print()
            # If exception - print and goto kpanic. 
            except Exception as e:
                traceback.print_exc()
                sys.exit() # Disable kpanic due testing.
                info[14].panic(info[11]['pyt']['unknown_kpanic'])
        

