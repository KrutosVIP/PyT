import sys, json, os
from colorama import Back, Fore, Style
from colorama import init as cinit
import argparse, random
sys.path.insert(0, "../types")
sys.path.insert(0, "../")
from module import Module
from cpkg import fargparse

class STDLib:
    def __init__(self, info):
        self.info = info
    def color(text):
        """
Colors to language text or smth,

Background:
{back.black},
{back.blue},
{back.cyan},
{back.green},
{back.lightblack_ex},
{back.lightblue_ex},
{back.lightcyan_ex},
{back.lightgreen_ex},
{back.lightmagenta_ex},
{back.lightred_ex},
{back.lightwhite_ex},
{back.lightyellow_ex},
{back.magenta},
{back.red},
{back.reset},
{back.white},
{back.yellow}

Foreground:
{fore.black},
{fore.blue},
{fore.cyan},
{fore.green},
{fore.lightblack_ex},
{fore.lightblue_ex},
{fore.lightcyan_ex},
{fore.lightgreen_ex},
{fore.lightmagenta_ex},
{fore.lightred_ex},
{fore.lightwhite_ex},
{fore.lightyellow_ex},
{fore.magenta},
{fore.red},
{fore.reset},
{fore.white},
{fore.yellow}

Style:
{style.bright},
{style.dim},
{style.normal},
{style.reset_all}
        """
        text = text.replace('{back.black}', Back.BLACK).replace('{back.blue}', Back.BLUE).replace('{back.cyan}', Back.CYAN).replace('{back.green}', Back.GREEN).replace('{back.lightblack_ex}', Back.LIGHTBLACK_EX).replace('{back.lightblue_ex}', Back.LIGHTBLUE_EX).replace('{back.lightcyan_ex}', Back.LIGHTCYAN_EX).replace('{back.lightgreen_ex}', Back.LIGHTGREEN_EX).replace('{back.lightmagenta_ex}', Back.LIGHTMAGENTA_EX).replace('{back.lightred_ex}', Back.LIGHTRED_EX).replace('{back.lightwhite_ex}', Back.LIGHTWHITE_EX).replace('{back.lightyellow_ex}', Back.LIGHTYELLOW_EX).replace('{back.magenta}', Back.MAGENTA).replace('{back.red}', Back.RED).replace('{back.reset}', Back.RESET).replace('{back.white}', Back.WHITE).replace('{back.yellow}', Back.YELLOW)
        text = text.replace('{fore.black}', Fore.BLACK).replace('{fore.blue}', Fore.BLUE).replace('{fore.cyan}', Fore.CYAN).replace('{fore.green}', Fore.GREEN).replace('{fore.lightblack_ex}', Fore.LIGHTBLACK_EX).replace('{fore.lightblue_ex}', Fore.LIGHTBLUE_EX).replace('{fore.lightcyan_ex}', Fore.LIGHTCYAN_EX).replace('{fore.lightgreen_ex}', Fore.LIGHTGREEN_EX).replace('{fore.lightmagenta_ex}', Fore.LIGHTMAGENTA_EX).replace('{fore.lightred_ex}', Fore.LIGHTRED_EX).replace('{fore.lightwhite_ex}', Fore.LIGHTWHITE_EX).replace('{fore.lightyellow_ex}', Fore.LIGHTYELLOW_EX).replace('{fore.magenta}', Fore.MAGENTA).replace('{fore.red}', Fore.RED).replace('{fore.reset}', Fore.RESET).replace('{fore.white}', Fore.WHITE).replace('{fore.yellow}', Fore.YELLOW)
        text = text.replace('{style.bright}', Style.BRIGHT).replace('{style.dim}', Style.DIM).replace('{style.normal}', Style.NORMAL).replace('{style.reset_all}', Style.RESET_ALL)

class PyT2(Module):
    def __init__(self):
        self.info = {
            "name" : "PyT v2",
            "version" : "0.0.1rc3",
            "codename": "pyt2",
            "dependencies" : [],
            "on_load" : self.on_load,
            "console": True,
            "user": None
        }

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
    def run(self, info):
        if self.error == 1:
            return
        print(info[11]["pyt"]["welcome"].replace("{%s}", self.color(random.choice(["{fore.black}","{fore.blue}",
"{fore.cyan}","{fore.green}","{fore.lightblack_ex}","{fore.lightblue_ex}","{fore.lightcyan_ex}","{fore.lightgreen_ex}","{fore.lightmagenta_ex}",
"{fore.lightred_ex}","{fore.lightwhite_ex}","{fore.lightyellow_ex}","{fore.magenta}","{fore.red}","{fore.reset}","{fore.white}","{fore.yellow}"]))).replace("{%d}", Style.RESET_ALL) + "\n(/cpkg/fargparse) (https://ru.stackoverflow.com/questions/1252352/%d0%9f%d0%b0%d1%80%d1%81%d0%b8%d0%bd%d0%b3-%d1%81%d1%82%d1%80%d0%be%d0%ba-%d0%bd%d0%b0-python-3-x)")
        
        if self.info["user"] == None:
            with open("../var/kernel_sets.json", "r") as f:
                d = f.read()
                accs = json.loads(d)["accounts"]
                accs_o = json.loads(d)["account_options"]
            print(info[11]["pyt"]["login"]["need"])
            autolog = self.json_load("../var/kernel_sets.json")["autologin"]
            if autolog["active"]:
                print(info[11]["pyt"]["login"]["autologin"])
                user = autolog["account"]["name"]
                passwd = autolog["account"]["password"]
                if user in accs:
                    if accs[user] == None:
                        self.info["user"] = user

                    if self.info["user"] == None:
                        if not user in accs:
                            print(info[11]["pyt"]["login"]["invalid"])
                        else:
                            if accs[user] != passwd:
                                print(info[11]["pyt"]["login"]["invalid"])
                            elif accs[user] == passwd:
                                self.info["user"] = user
                if self.info["user"] == None:
                    print(info[11]["pyt"]["login"]["auto_invalid"])
                
            while self.info["user"] == None:
                try:
                    user = input(info[11]["pyt"]["login"]["login"])
                    if user in accs:
                        if accs[user] == None:
                            self.info["user"] = user

                    if self.info["user"] == None:
                        passwd = input(info[11]["pyt"]["login"]["password"])
                        
                        if not user in accs:
                            print(info[11]["pyt"]["login"]["invalid"])
                        else:
                            if accs[user] != passwd:
                                print(info[11]["pyt"]["login"]["invalid"])
                            elif accs[user] == passwd:
                                self.info["user"] = user
                except KeyboardInterrupt:
                    print()
        session = True
        while session:
            try:
                if accs_o[self.info["user"]]["root_acc"]:
                    print(self.color(f"{info[11]['pyt']['color']}{self.info['user']}@{info[8]}{Style.RESET_ALL} # "), end = "")
                    u_i = input()
                else:
                    print(self.color(f"{info[11]['pyt']['color']}{self.info['user']}@{info[8]}{Style.RESET_ALL} $ "), end = "")
                    u_i = input()
                parse = u_i.split(" ")
                            
                if parse[0] in info[10]:
                    if os.path.exists("../var/history.json"):
                        with open("../var/history.json") as f:
                            history = json.load(f)
                    else:
                        history = {"history": []}

                        
                    history["history"].append({parse[0]: "".join(parse[1:])})
                    with open("../var/history.json", "w") as f:
                        history = json.dump(history, f)
                    info2 = info.copy(); info2.append(u_i)
                    stdlib = STDLib(info2)
                    info[10][parse[0]].info["run"](stdlib, self)
                else:
                    if not u_i.isspace() and not u_i == "":
                        print(info[11]['pyt']['invalid_command'].replace("{cmd}", parse[0]))
            except KeyboardInterrupt:
                print()
    
        

